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
        logger.info(tracker.events)
        dispatcher.utter_message(template="utter_greet")
        return [UserUtteranceReverted()]




class QueryReceiveDateForm(FormAction):
    """查询：领药日期"""
    
    def name(self):
        return "query_receive_date_form"

    @staticmethod
    def required_slots(tracker):
        slot = tracker.get_slot('apply_drug')
        if(slot == '百泽安'):
            return ["apply_drug","foundation","patient_idsn", ]
        else:
            return ["apply_drug", 'patient_idsn']

    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ],
            'foundation': [
                self.from_entity(entity="foundation"),
                self.from_text(),
            ],
            "patient_idsn": [
                self.from_entity(entity="patient_idsn"),
                self.from_text(),
            ]
        }

    def validate_patient_idsn(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker ,domain:Dict[Text, Any]):
        return {'patient_idsn': value}
        # dispatcher.utter_message(“证件号格式不正确”)
        # return {"patient_idsn": None}

    def validate_foundation(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker ,domain:Dict[Text, Any]):
        return {'foundation': value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        apply_drug = tracker.get_slot('apply_drug')
        patient_idsn = tracker.get_slot('patient_idsn')
        if(apply_drug=='百泽安'):
            apply_drug = apply_drug + tracker.get_slot('foundation')

        yyc_query = queryApi.yycQuery()
        post_data = {'idsn':tracker.get_slot('patient_idsn'), 'papProjectName':tracker.get_slot('apply_drug')}
        res = yyc_query.query_patientreceivetime(post_data)
        print("res:")
        print(res)

        if res.get('success') and res.get('code') == 20000 and res.get('data'):
            dispatcher.utter_message("已查到您的筹药信息，您的领药日期是：" + res.get('data') )
        else:
            dispatcher.utter_message("未查到您的筹药信息，如有其他需要请与人工联系" )

        return []

        #dispatcher.utter_message(apply_drug+' '+patient_idsn+' '+"您好，您的领药日期是：XXXX-XX-XX。")
        #return []


class QueryCityDrugstoreForm(FormAction):
    """查询：城市药房列表"""
    
    def name(self):
        return "query_city_drugstore_form"

    @staticmethod
    def required_slots(tracker):
        return ['apply_drug','apply_city']
    
    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ],
            "apply_city": [
                self.from_entity(entity="apply_city"),
                self.from_text(),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_default_with_human")
        return []


class ActionQueryServiceTel(Action):

    def name(self):
        return 'action_query_service_tel'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_query_service_tel")
        return [UserUtteranceReverted()]


class QueryEmailAddrForm(FormAction):
    """查询：邮寄地址"""

    def name(self):
        return "query_email_addr_form"

    @staticmethod
    def required_slots(tracker):
        
        return [
            "apply_drug",
        ]

    def slot_mappings(self):

        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ],
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
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        yyc_query = queryApi.yycQuery()
        post_data = {'papProjectName':tracker.get_slot('apply_drug')}
        res = yyc_query.query_emailaddr(post_data)
        print("res:")
        print(res)

        if res.get('success') and res.get('code') == 20000 and res.get('data'):
            dispatcher.utter_message("您的筹药信息已找到，发票邮寄地址是：" + res.get('data') )
        else:
            dispatcher.utter_message("您的筹药信息未找到，无需邮寄发票")

        # dispatcher.utter_message('name:{}, mobile:{}, apply_drug:{}'.format(tracker.get_slot('patient_name'), tracker.get_slot('phone-number'), tracker.get_slot('apply_drug')))
        return []
        
        
class QueryDrugstoreAddressForm(FormAction):
    """查询：药房地址"""

    def name(self):
        return "query_drugstore_address_form"

    @staticmethod
    def required_slots(tracker):
        return ["apply_city","drugstore_name",]

    def slot_mappings(self):
        return {
            "apply_city": [
                self.from_entity(entity="apply_city"),
                self.from_text(),
            ],
            "drugstore_name": [
                # self.from_entity(entity="drugstore_name"),
                self.from_text(),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        yyc_query = queryApi.yycQuery()
        post_data = {'name':tracker.get_slot('drugstore_name')}
        res = yyc_query.query_drugstoreAddress(post_data)
        print("res:")
        print(res)

        if res.get('success') and res.get('code') == 20000 and res.get('data'):
            dispatcher.utter_message("药房{}地址是：{}".format(tracker.get_slot('drugstore_name'), res.get('data')) )
        else:
            dispatcher.utter_message("药房信息未找到，请与人工联系" )

        # dispatcher.utter_message("您的筹药申请已经通过，您的领药地址是：{dr_name}；药房地址：邯郸市中华南大街1号；药房联系电话：{dr_mobile}。 本人直接凭身份证原件及正反两面复印件、处方原件领取药品；亲属代领请携带患者身份证原件及正反两面复印件、处方原件、领药委托书、患者手持一周内报纸拍摄的影像材料、代领人身份证原件及正反两面复印件。".format(**res))
        return []


# class QueryDrugstoreMobileForm(FormAction):
#     """查询：领药药房电话"""

#     def name(self):
#         return "query_drugstore_mobile_form"

#     @staticmethod
#     def required_slots(tracker):
#         return [
#             "drugstore_name",
#         ]

#     def slot_mappings(self):
#         return {
#             "drugstore_name": [
#                 # self.from_entity(entity="patient_name"),
#                 self.from_text(),
#             ],
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         yyc_query = queryApi.yycQuery()
#         post_data = {'name':tracker.get_slot('drugstore_name')}
#         res = yyc_query.query_drugstorephone(post_data)

#         print("res:")
#         print(res)

#         if res.get('success') and res.get('code') == 20000 and res.get('data'):
#             dispatcher.utter_message("您要查询的药房的电话是：" + res.get('data') )
#         else:
#             dispatcher.utter_message("未找到您要查询的药房电话，请与人工联系" )

#         # drugstore_name = tracker.get_slot('drugstore_name')
#         # dispatcher.utter_message("您药房{}的电话是XXXXXX。".format(drugstore_name))
#         return []


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

        yyc_query = queryApi.yycQuery()
        post_data = {'name':tracker.get_slot('patient_name'), 'mobile':tracker.get_slot('phone-number'), 'papProjectName':tracker.get_slot('apply_drug')}
        res = yyc_query.query_patientprocess(post_data)
        print("res:")
        print(res)

        if res.get('success') and res.get('code') == 20000 and res.get('data'):
            dispatcher.utter_message("您的筹药进度已经查到，当前状态是：" + res.get('data') )
        else:
            dispatcher.utter_message("您的筹药进度未查到，请与人工联系" )

        # dispatcher.utter_message("江小白福可维第11次审核通过，您的领药药房：邯郸医药大厦连锁有限公司；药房地址：邯郸市中华南大街1号；领药日期：2019-06-18；药房联系电话：0797-8277239")
        return []




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


class InvoiceRefundForm(FormAction):
    """发票：发票报销"""
    
    def name(self):
        return "invoice_refund_form"

    @staticmethod
    def required_slots(tracker):
        slot = tracker.get_slot('apply_drug')
        if( slot == '福可维'):
            return ["apply_drug", "is_refund"]
        else:
            return ["apply_drug"]
    
    def slot_mappings(self):
        return {
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ],
            "is_refund": [
                self.from_intent(intent="affirm",value=True),
                self.from_intent(intent="deny",value=False),
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
        # slot = tracker.get_slot('apply_drug')
        # if( slot == '福可维'):
        #     if(tracker.get_slot("is_refund") == True):
        #         dispatcher.utter_message(template="utter_is_refund_fkw_yes")
        #     else:
        #         dispatcher.utter_message(template="utter_is_refund_fkw_no")
        # else:
        #     dispatcher.utter_message(template="utter_question_not_fit")
        dispatcher.utter_message("待对接接口")

        return []


class InvoiceNameErrorForm(FormAction):
    """发票：发票姓名错误"""
    
    def name(self):
        return "invoice_name_error_form"

    @staticmethod
    def required_slots(tracker):
        return ['apply_drug']
    
    def slot_mappings(self):
        return {
            'apply_drug':[
                self.from_entity(entity="apply_drug")
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("待对接接口")
        return []


class InvoiceIncompleteForm(FormAction):
    """发票：发票不全"""
    
    def name(self):
        return "invoice_incomplete_form"

    @staticmethod
    def required_slots(tracker):
        return ['apply_drug']
    
    def slot_mappings(self):
        return {
            'apply_drug':[
                self.from_entity(entity="apply_drug")
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("待对接接口")
        return []


class InvoiceCopiesForm(FormAction):
    """发票：发票复印件/替代品可以吗"""
    
    def name(self):
        return "invoice_copies_form"

    @staticmethod
    def required_slots(tracker):
        return ['apply_drug']
    
    def slot_mappings(self):
        return {
            'apply_drug':[
                self.from_entity(entity="apply_drug")
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("待对接接口")
        return []


class InvoiceSendBackForm(FormAction):
    """发票：发票回寄"""
    
    def name(self):
        return "invoice_send_back_form"

    @staticmethod
    def required_slots(tracker):
        return ['apply_drug']
    
    def slot_mappings(self):
        return {
            'apply_drug':[
                self.from_entity(entity="apply_drug")
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("待对接接口")
        return []




class HandoffToHumanForm(FormAction):
    """转人工：转人工服务前收集用户信息"""
    
    def name(self):
        return "handoff_to_human_form"

    @staticmethod
    def required_slots(tracker):
        return ['patient_name', 'patient_idsn', 'apply_drug']
    
    def slot_mappings(self):
        return {
            "patient_name": [
                self.from_entity(entity="patient_name"),
                self.from_text(),
            ],
            "patient_idsn": [
                self.from_entity(entity="patient_idsn"),
                self.from_text(),
            ],
            "apply_drug": [
                self.from_entity(entity="apply_drug"),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker : Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("待对接接口")
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

