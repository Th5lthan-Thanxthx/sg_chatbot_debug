## 查询领药日期
* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help
  
* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
  - slot{"apply_drug": "瑞复美"}
  - form{"name": null}
  - utter_is_help

* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
  - slot{"apply_drug": "脑脉利"}
  - form{"name": null}
  - utter_is_help

* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
  - slot{"apply_drug": "百泽安"}
  - form{"name": null}
  - utter_is_help

* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
  - slot{"apply_drug": "恩立施"}
  - form{"name": null}
  - utter_is_help

* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
  - slot{"apply_drug": "吉至"}
  - form{"name": null}
  - utter_is_help

* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
  - slot{"apply_drug": "益久"}
  - form{"name": null}
  - utter_is_help


* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_city_drugstore
* affirm
  - query_city_drugstore_form
  - form{"name": null}
  - utter_is_help
  
* query_city_drugstore
  - query_city_drugstore_form
  - form{"name": "query_city_drugstore_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_city_drugstore
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help