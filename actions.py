# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


import logging
import json
import requests
from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet,UserUtteranceReverted,ConversationPaused,Restarted
from rasa_sdk.executor import CollectingDispatcher

logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ActionGreet(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        logger.info(tracker.sender_id)
        dispatcher.utter_message(template="utter_greet")
        return [UserUtteranceReverted()]



class InvoiceLossForm(FormAction):
    """发票：发票丢失"""

    def name(self):
        return "invoice_loss_form"

    @staticmethod
    def required_slots(tracker):
        return ["apply_drug"]
    
    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ]
        }

    # def validate_apply_drug(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker ,domain:Dict[Text, Any]):
    #     from params import drug_dict
    #     if(value not in drug_dict):
    #         dispatcher.utter_message(template="utter_drug_invalid")
    #         return {"apply_drug":None}
    #     else:
    #         return {"apply_drug":value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        evts = []
        # from params import drug_dict
        apply_drug = tracker.get_slot('apply_drug')
        dispatcher.utter_message("您申请的药品是：{}".format(apply_drug))
        # if(apply_drug=='百泽安'):
        #     apply_drug += '初保'
        # if(apply_drug not in drug_dict):
        #     dispatcher.utter_message(template="utter_drug_invalid")
        #     return evts
        # yyc_query = queryApi.yycQuery()
        # post_data = {'drugName':apply_drug}
        # res = yyc_query.query_invoicemissing(post_data)
        # print("res:")
        # print(res)

        # if res.get('success') and res.get('code') == 20000 and res.get('data'):
        #     dispatcher.utter_message(res.get('data') )
        # else:
        #     dispatcher.utter_message("未查询到相关结果，请与人工联系" )
        return evts







class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv("data/" "intent_description_mapping.csv")
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:
        
        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        first_intent_names = [
            intent.get("name", "")
            for intent in intent_ranking
            if intent.get("name", "") != "out_of_scope" and intent.get("name","") != "" and intent.get("name","") in self.intent_mappings.intent.values
        ]

        if(len(first_intent_names) < 1):
            dispatcher.utter_message(template="utter_default")
            return [UserUtteranceReverted()]

        message_title = (
            "不好意思，没太明白您的意思 🤔 您的意思是..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            
            buttons.append(
                {
                    "title": self.get_button_title(intent, entities),
                    "payload": "/{}{}".format(intent, entities_json),
                }
            )

        # buttons.append({"title": "都不是", "payload": "/out_of_scope"})

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (
            self.intent_mappings.entities == entities.keys() & default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:
        # Fallback caused by TwoStageFallbackPolicy
        evts = []
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_message(template="utter_default_with_human")
            evts + [UserUtteranceReverted()]
            # dispatcher.utter_message(template="utter_restart_with_button")

            # return [ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_default")
            
        return evts + [UserUtteranceReverted()]


# 未启用
class ActionRestartTracker(Action):
    """ 单个问题结束后清楚所有slot,下个问题重新开始"""

    def name(self):
        return "action_restart_tracker"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:

        return [Restarted()]

