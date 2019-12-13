# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

class ActionQueryReceiptAddress(Action):

    def name(self):
        return "action_query_receipt_address"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("您的筹药申请已经通过，请将发票邮寄到如下地址： 武汉市武昌区邮政速递水果湖揽投部 收件人：医药筹福可维 联系电话 ：027-59425239 （所有邮寄方式仅限邮政EMS）温馨提示：a.仅需邮寄发票原件即可；b.因为申请量大，邮寄地址填写批量收件地址更快捷，请放心填写。")
        return []

class ActionQueryDrugstore(Action):

    def name(self):
        return "action_query_drugstore"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("您的筹药申请已经通过，您的领药地址是：邯郸医药大厦连锁有限公司；药房地址：邯郸市中华南大街1号；药房联系电话：0797-8277239。 本人直接凭身份证原件及正反两面复印件、处方原件领取药品；亲属代领请携带患者身份证原件及正反两面复印件、处方原件、领药委托书、患者手持一周内报纸拍摄的影像材料、代领人身份证原件及正反两面复印件。")
        return []

class ActionQueryApplyCity(Action):

    def name(self):
        return "action_query_apply_city"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("本地市有合作药房。")
        return []

class ActionQueryAuditProgress(Action):

    def name(self):
        return "action_query_audit_progress"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("江小白福可维第11次审核通过，您的领药药房：邯郸医药大厦连锁有限公司；药房地址：邯郸市中华南大街1号；领药日期：2019-06-18；药房联系电话：0797-8277239")
        return []
