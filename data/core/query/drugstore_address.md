## 查询药房
* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help
  
* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
  - slot{"apply_drug": "瑞复美"}
  - form{"name": null}
  - utter_is_help

* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
  - slot{"apply_drug": "脑脉利"}
  - form{"name": null}
  - utter_is_help

* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
  - slot{"apply_drug": "百泽安"}
  - form{"name": null}
  - utter_is_help

* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
  - slot{"apply_drug": "恩立施"}
  - form{"name": null}
  - utter_is_help

* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
  - slot{"apply_drug": "吉至"}
  - form{"name": null}
  - utter_is_help

* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
  - slot{"apply_drug": "益久"}
  - form{"name": null}
  - utter_is_help

* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore_address
* affirm
  - query_drugstore_address_form
  - form{"name": null}
  - utter_is_help
  
* query_drugstore_address
  - query_drugstore_address_form
  - form{"name": "query_drugstore_address_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_drugstore_address
* deny
  - action_deactivate_form
  - form{"name": null}