## query receipt address
* greet
  - utter_greet
* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
  - form{"name": null}

* greet
  - utter_greet
* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receipt
* affirm
  - query_receipt_form
  - form{"name": null}

* greet
  - utter_greet
* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receipt
* deny
  - action_deactivate_form
  - form{"name": null}

## query drugstore
* greet
  - utter_greet
* query_drugstore
  - query_drugstore_form
  - form{"name": "query_drugstore_form"}
  - form{"name": null}

* greet
  - utter_greet
* query_drugstore
  - query_drugstore_form
  - form{"name": "query_drugstore_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore
* affirm
  - query_drugstore_form
  - form{"name": null}
  
* greet
  - utter_greet
* query_drugstore
  - query_drugstore_form
  - form{"name": "query_drugstore_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore
* deny
  - action_deactivate_form
  - form{"name": null}


## query apply city
* greet
  - utter_greet
* query_apply_city
  - query_apply_city_form
  - form{"name": "query_apply_city_form"}
  - form{"name": null}

* greet
  - utter_greet
* query_apply_city
  - query_apply_city_form
  - form{"name": "query_apply_city_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_apply_city
* affirm
  - query_apply_city_form
  - form{"name": null}

* greet
  - utter_greet
* query_apply_city
  - query_apply_city_form
  - form{"name": "query_apply_city_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_apply_city
* deny
  - action_deactivate_form
  - form{"name": null}

## query audit progress
* greet
  - utter_greet
* query_audit_progress
  - query_audit_progress_form
  - form{"name": "query_audit_progress_form"}
  - form{"name": null}

* greet
  - utter_greet
* query_audit_progress
  - query_audit_progress_form
  - form{"name": "query_audit_progress_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_audit_progress
* affirm
  - query_audit_progress_form
  - form{"name": null}
  
* greet
  - utter_greet
* query_audit_progress
  - query_audit_progress_form
  - form{"name": "query_audit_progress_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_audit_progress
* deny
  - action_deactivate_form
  - form{"name": null}

