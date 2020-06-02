## 咨询发票类问题
* query_invoice
  - utter_query_invoice

## 查询发票快递地址
* invoice_address_query
  - query_receipt_form
  - form{"name": "query_receipt_form"}
  - form{"name": null}

## 查询发票邮寄地址
* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
  - form{"name": null}

* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receipt
* affirm
  - query_receipt_form
  - form{"name": null}

* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receipt
* deny
  - action_deactivate_form
  - form{"name": null}

## 查询药房地址
* query_drugstore
  - query_drugstore_form
  - form{"name": "query_drugstore_form"}
  - form{"name": null}

* query_drugstore
  - query_drugstore_form
  - form{"name": "query_drugstore_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore
* affirm
  - query_drugstore_form
  - form{"name": null}
  
* query_drugstore
  - query_drugstore_form
  - form{"name": "query_drugstore_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore
* deny
  - action_deactivate_form
  - form{"name": null}

## 查询药房地址
* query_drugstore_mobile
  - query_drugstore_mobile_form
  - form{"name": "query_drugstore_mobile_form"}
  - form{"name": null}
  - utter_is_help

* query_drugstore
  - query_drugstore_mobile_form
  - form{"name": "query_drugstore_mobile_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore
* affirm
  - query_drugstore_mobile_form
  - form{"name": null}
  - utter_is_help
  
* query_drugstore
  - query_drugstore_mobile_form
  - form{"name": "query_drugstore_mobile_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore_mobile
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help


## 查询申请城市
* query_apply_city
  - query_apply_city_form
  - form{"name": "query_apply_city_form"}
  - form{"name": null}

* query_apply_city
  - query_apply_city_form
  - form{"name": "query_apply_city_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_apply_city
* affirm
  - query_apply_city_form
  - form{"name": null}

* query_apply_city
  - query_apply_city_form
  - form{"name": "query_apply_city_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_apply_city
* deny
  - action_deactivate_form
  - form{"name": null}

## 查询审核进度
* query_audit_progress
  - query_audit_progress_form
  - form{"name": "query_audit_progress_form"}
  - form{"name": null}

* query_audit_progress
  - query_audit_progress_form
  - form{"name": "query_audit_progress_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_audit_progress
* affirm
  - query_audit_progress_form
  - form{"name": null}

* query_audit_progress
  - query_audit_progress_form
  - form{"name": "query_audit_progress_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_audit_progress
* deny
  - action_deactivate_form
  - form{"name": null}

## 查询领药日期
* query_receive_date
  - query_receive_date_form
  - form{"name": "query_receive_date_form"}
  - form{"name": null}
  - utter_is_help

* query_receive_date
  - query_receive_date_form
  - form{"name": "query_receive_date_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receive_date
* affirm
  - query_receive_date_form
  - form{"name": null}
  - utter_is_help
  
* query_receive_date
  - query_receive_date_form
  - form{"name": "query_receive_date_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receive_date
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

