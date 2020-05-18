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
from api import queryApi

logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ActionGreet(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return [UserUtteranceReverted()]




class QueryReceiptForm(FormAction):
    """查询：发票邮寄地址"""

    def name(self):
        return "query_receipt_form"

    @staticmethod
    def required_slots(tracker):
        
        return [
            "patient_name",
            "phone-number",
            "apply_drug",
        ]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "patient_name": [
                self.from_entity(entity="patient_name"),
                self.from_text()
            ],
            "phone-number": [
                self.from_entity(entity="phone-number"),
            ],
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # post_data = {'name':tracker.get_slot('patient_name'), 'mobile':tracker.get_slot('phone-number'), 'apply_drug':tracker.get_slot('apply_drug')}
        # yyc_query = queryApi.yycQuery()
        # res = yyc_query.query_receipt(post_data)
        # dispatcher.utter_message(res['text'])
        dispatcher.utter_message('name:{}, mobile:{}, apply_drug:{}'.format(tracker.get_slot('patient_name'), tracker.get_slot('phone-number'), tracker.get_slot('apply_drug')))
        return []


class QueryDrugstoreForm(FormAction):
    """查询：领药药房"""

    def name(self):
        return "query_drugstore_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "patient_name",
            "phone-number",
            "apply_drug",
        ]

    def slot_mappings(self):
        return {
            "patient_name": [
                self.from_entity(entity="patient_name"),
                self.from_text(),
            ],
            "phone-number": [
                self.from_entity(entity="phone-number"),
            ],
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # yyc_query = queryApi.yycQuery()
        # post_data = {'name':tracker.get_slot('patient_name'), 'mobile':tracker.get_slot('phone-number'), 'apply_drug':tracker.get_slot('apply_drug')}
        # res = yyc_query.query_drugstore(post_data)
        # dispatcher.utter_message("您的筹药申请已经通过，您的领药地址是：{dr_name}；药房地址：邯郸市中华南大街1号；药房联系电话：{dr_mobile}。 本人直接凭身份证原件及正反两面复印件、处方原件领取药品；亲属代领请携带患者身份证原件及正反两面复印件、处方原件、领药委托书、患者手持一周内报纸拍摄的影像材料、代领人身份证原件及正反两面复印件。".format(**res))
        dispatcher.utter_message("name:{}, mobile:{}, apply_drug:{}".format(tracker.get_slot('patient_name'), tracker.get_slot('phone-number'), tracker.get_slot('apply_drug')))
        return []


class QueryDrugstoreMobileForm(FormAction):
    """查询：领药药房电话"""

    def name(self):
        return "query_drugstore_mobile_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "drugstore_name",
        ]

    def slot_mappings(self):
        return {
            "drugstore_name": [
                # self.from_entity(entity="patient_name"),
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # yyc_query = queryApi.yycQuery()
        # post_data = {'name':tracker.get_slot('patient_name'), 'mobile':tracker.get_slot('phone-number'), 'apply_drug':tracker.get_slot('apply_drug')}
        # res = yyc_query.query_drugstore(post_data)
        # drugstore_name = tracker.get_slot('drugstore_name')
        # dispatcher.utter_message("您药房{}的电话是XXXXXX。".format(drugstore_name))
        # dispatcher.utter_message("非常抱歉，未查询到该药房的电话，建议您下次领药时，可以到药房询问该药房是否有联系方式")
        dispatcher.utter_message("drugstore_name:{}".format(tracker.get_slot('drugstore_name')))
        return []


class QueryApplyCityForm(FormAction):
    """查询：城市药房"""

    def name(self):
        return "query_apply_city_form"
    
    @staticmethod
    def required_slots(tracker):
        return ["apply_city", "apply_drug"]

    def slot_mappings(self):
        return {
            "apply_city": [
                self.from_entity(entity="apply_city"),
                self.from_text(intent="enter_data")
            ],
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ]
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("本地市有合作药房。")
        return []


class QueryAuditProgressForm(FormAction):
    """查询：申请进度"""
    
    def name(self):
        return "query_audit_progress_form"

    @staticmethod
    def required_slots(tracker):
        return ["patient_name", "phone-number", "apply_drug"]

    def slot_mappings(self):
        return {
            "patient_name": [
                self.from_entity(entity="patient_name"),
                self.from_text(),
            ],
            "phone-number": [
                self.from_entity(entity="phone-number"),
            ],
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ]
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("江小白福可维第11次审核通过，您的领药药房：邯郸医药大厦连锁有限公司；药房地址：邯郸市中华南大街1号；领药日期：2019-06-18；药房联系电话：0797-8277239")
        return []


class QueryReceiveDateForm(FormAction):
    """查询：领药日期"""
    
    def name(self):
        return "query_receive_date_form"

    @staticmethod
    def required_slots(tracker):
        slot = tracker.get_slot('apply_drug')
        if( (isinstance(slot,list) and '百泽安' in slot) or slot == '百泽安'):
            return ["apply_drug","bza_type","patient_idsn", ]
        else:
            return ["apply_drug", 'patient_idsn']

    def slot_mappings(self):
        return {
            "patient_idsn": [
                self.from_entity(entity="patient_idsn"),
                self.from_text(),
            ],
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ],
            'bza_type': [
                self.from_entity(entity="bza_type"),
                self.from_text(),
            ]
        }

    def validate_patient_idsn(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker ,domain:Dict[Text, Any]):
        return {'patient_idsn': value}
        # dispatcher.utter_message(“证件号格式不正确”)
        # return {"patient_idsn": None}
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        apply_drug = tracker.get_slot('apply_drug')
        patient_idsn = tracker.get_slot('patient_idsn')
        if(apply_drug=='百泽安'):
            apply_drug = apply_drug + tracker.get_slot('bza_type')
        
        dispatcher.utter_message(apply_drug+' '+patient_idsn+' '+"您好，您的领药日期是：XXXX-XX-XX。")
        return []


class TroubleInvoiceLossForm(FormAction):
    """问题：发票丢失问题"""

    def name(self):
        return "trouble_invoice_loss_form"

    @staticmethod
    def required_slots(tracker):
        return ["apply_drug"]
    
    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ]
        }
    
    def validate_apply_drug(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker ,domain:Dict[Text, Any]):
        from params import drug_dict
        if(value not in drug_dict):
            dispatcher.utter_message('抱歉，无法确认您申请的药品')
            return {"apply_drug":None}
        else:
            return {"apply_drug":value}
        
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        evts = []
        apply_drug = tracker.get_slot('apply_drug')
        from params import drug_dict
        if(apply_drug in drug_dict):
            dispatcher.utter_message(template="utter_invoice_loss_"+drug_dict[apply_drug])
        else:
            dispatcher.utter_message('抱歉，无法确认您申请的药品')
            evts + [SlotSet("apply_drug",None)]
        return evts


class TroubleInvoiceReimbursementForm(FormAction):
    """问题：发票已报销(福可维限定)"""
    
    def name(self):
        return "trouble_invoice_reimbursement_form"

    @staticmethod
    def required_slots(tracker):
        slot = tracker.get_slot('apply_drug')
        if( slot == '福可维'):
            return ["apply_drug", "is_reimburse"]
        else:
            return ["apply_drug"]
    
    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ],
            "is_reimburse": [
                self.from_intent(intent="affirm",value=True),
                self.from_intent(intent="deny",value=False),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        slot = tracker.get_slot('apply_drug')
        if( slot == '福可维'):
            if(tracker.get_slot("is_reimburse") == True):
                dispatcher.utter_message(template="utter_is_reimburse_fkw_yes")
            else:
                dispatcher.utter_message(template="utter_is_reimburse_fkw_no")
        else:
            dispatcher.utter_message(template="utter_question_not_fit")
                
        return []




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
            if intent.get("name", "") != "out_of_scope" and intent.get("name","") != None
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
            logger.info(intent)
            logger.info(entities)
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
        logger.info('tracker.events')
        logger.info(tracker.events)
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