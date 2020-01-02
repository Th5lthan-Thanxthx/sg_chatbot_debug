# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
import logging
import json
from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted

from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# class ActionQueryReceiptAddress(Action):

#     def name(self):
#         return "action_query_receipt_address"

#     def run(self, dispatcher, tracker, domain):
#         logger.info("ActionQueryReceiptAddress run()")
#         dispatcher.utter_message("您的筹药申请已经通过，请将发票邮寄到如下地址： 武汉市武昌区邮政速递水果湖揽投部 收件人：医药筹福可维 联系电话 ：027-59425239 （所有邮寄方式仅限邮政EMS）温馨提示：a.仅需邮寄发票原件即可；b.因为申请量大，邮寄地址填写批量收件地址更快捷，请放心填写。")
#         return []
class QueryReceiptForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

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
        """Once we have all the information, attempt to add it to the
        Google Drive database"""
        
        dispatcher.utter_message("您的筹药申请已经通过，请将发票邮寄到如下地址： 武汉市武昌区邮政速递水果湖揽投部 收件人：医药筹福可维 联系电话 ：027-59425239 （所有邮寄方式仅限邮政EMS）温馨提示：a.仅需邮寄发票原件即可；b.因为申请量大，邮寄地址填写批量收件地址更快捷，请放心填写。")
        return []

class QueryDrugstoreForm(FormAction):
    
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
        dispatcher.utter_message("您的筹药申请已经通过，您的领药地址是：邯郸医药大厦连锁有限公司；药房地址：邯郸市中华南大街1号；药房联系电话：0797-8277239。 本人直接凭身份证原件及正反两面复印件、处方原件领取药品；亲属代领请携带患者身份证原件及正反两面复印件、处方原件、领药委托书、患者手持一周内报纸拍摄的影像材料、代领人身份证原件及正反两面复印件。")
        return []
# class ActionQueryDrugstore(Action):

#     def name(self):
#         return "action_query_drugstore"

#     def run(self, dispatcher, tracker, domain):
#         logger.info("ActionQueryDrugstore run()")
#         dispatcher.utter_message("您的筹药申请已经通过，您的领药地址是：邯郸医药大厦连锁有限公司；药房地址：邯郸市中华南大街1号；药房联系电话：0797-8277239。 本人直接凭身份证原件及正反两面复印件、处方原件领取药品；亲属代领请携带患者身份证原件及正反两面复印件、处方原件、领药委托书、患者手持一周内报纸拍摄的影像材料、代领人身份证原件及正反两面复印件。")
#         return []

# class ActionQueryApplyCity(Action):

#     def name(self):
#         return "action_query_apply_city"

#     def run(self, dispatcher, tracker, domain):
#         logger.info("ActionQueryApplyCity run()")
#         dispatcher.utter_message("本地市有合作药房。")
#         return []

class QueryApplyCityForm(FormAction):

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

# class ActionQueryAuditProgress(Action):

#     def name(self):
#         return "action_query_audit_progress"

#     def run(self, dispatcher, tracker, domain):
#         logger.info("ActionQueryAuditProgress run()")
#         dispatcher.utter_message("江小白福可维第11次审核通过，您的领药药房：邯郸医药大厦连锁有限公司；药房地址：邯郸市中华南大街1号；领药日期：2019-06-18；药房联系电话：0797-8277239")
#         return []

class QueryAuditProgressForm(FormAction):

    def name(self):
        return "query_audit_progress_form"

    @staticmethod
    def required_slots(tracker):
        return ["patient_name", "phone-number", "apply_drug"]

    def slot_mappings(self):
        return {
            "patient_name": [
                self.from_entity(entity="paitent_name"),
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

class AskInvoiceLossForm(FormAction):

    def name(self):
        return "ask_invoice_form"

    @staticmethod
    def required_slots(tracker):
        return ["apply_drug"]
    
    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
                self.from_text()
            ]
        }
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        apply_drug = tracker.get_slot('apply_drug')
        if(apply_drug == '福可维'):
            dispatcher.utter_template('utter_invoice_loss_fkw', tracker)
        elif(apply_drug == '瑞复美'):
            dispatcher.utter_template('utter_invoice_loss_rfm', tracker)
        elif(apply_drug == '脑脉利'):
            dispatcher.utter_template('utter_invoice_loss_nml', tracker)
        elif(apply_drug == '益久'):
            dispatcher.utter_template('utter_invoice_loss_yj', tracker)
        else:
            dispatcher.utter_message('抱歉，无法确认您申请的药品')
        return []

class AskInvoiceReimbursementForm(FormAction):

    def name(self):
        return "ask_invoice_reimbursement_form"

    @staticmethod
    def required_slots(tracker):
        if(tracker.get_slot('apply_drug') == '福可维'):
            return ["apply_drug", "is_imburse"]
        else:
            return ["apply_drug"]
    
    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
                self.from_text()
            ],
            "is_imburse": [
                self.from_intent(intent="affirm",value=True),
                self.from_intent(intent="deny",value=False),
            ]
        }

    # def validate_apply_drug(self, value, dispatcher, tracker, domain):
    #     if tracker.get_slot("apply_drug") == '福可维':
    #         return {"apply_drug": value}
    #     else:
    #         dispatcher.utter_template("utter_question_not_fit", tracker)
    #         return {"apply_drug": None}
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if(tracker.get_slot('apply_drug') != '福可维'):
            dispatcher.utter_message(template="utter_question_not_fit", tracker)
        else:
            if(tracker.get_slo == True):
                dispatcher.utter_message(template="utter_drug_reimbursement_yes_fkw", tracker)
            else:
                dispatcher.utter_message(template="utter_drug_reimbursement_no_fkw", tracker)
                
        return []

# class ActionInvoiceReimbursement(Action):

#     def name(self) -> Text:
#         return "action_invoice_reimbursement"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List["Event"]:
#         apply_drug = tracker.get_slot("apply_drug")
#         if(apply_drug != None):
#             if(apply_drug == "福可维"):
#                 dispatcher.utter_template('utter_aks_drug_reimbursement', tracker)
#             else:
#                 dispatcher.utter_template('utter_question_not_fit', tracker)
#         else:
#             dispatcher.utter_template("utter_ask_apply_drug",tracker)

#         return []

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
            if intent.get("name", "") != "out_of_scope"
        ]

        message_title = (
            "不好意思，没太明白您的意思 🤔 您的意思是..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            logger.debug(intent)
            logger.debug(entities)
            buttons.append(
                {
                    "title": self.get_button_title(intent, entities),
                    "payload": "/{}{}".format(intent, entities_json),
                }
            )

        buttons.append({"title": "都不是", "payload": "/out_of_scope"})

        dispatcher.utter_button_message(message_title, buttons=buttons)

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
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_template("utter_restart_with_button", tracker)

            # return [SlotSet("feedback_value", "negative"), ConversationPaused()]
            return []

        # Fallback caused by Core
        else:
            dispatcher.utter_template("utter_default", tracker)
            return [UserUtteranceReverted()]