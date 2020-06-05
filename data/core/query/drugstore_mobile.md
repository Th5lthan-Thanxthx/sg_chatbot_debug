<!-- ## 查询药房电话-已删除
* query_drugstore_mobile
  - query_drugstore_mobile_form
  - form{"name": "query_drugstore_mobile_form"}
  - form{"name": null}
  - utter_is_help

* query_drugstore_mobile
  - query_drugstore_mobile_form
  - form{"name": "query_drugstore_mobile_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore_mobile
* affirm
  - query_drugstore_mobile_form
  - form{"name": null}
  - utter_is_help
  
* query_drugstore_mobile
  - query_drugstore_mobile_form
  - form{"name": "query_drugstore_mobile_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore_mobile
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help -->