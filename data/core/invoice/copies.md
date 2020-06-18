## 发票复印件/替代品可以吗
* invoice_copies
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"恩立施"}
    - slot{"apply_drug":"恩立施"}
    - invoice_copies_form
    - form{"name": "invoice_copies_form"}
    - form{"name": null}
    - utter_is_help

* invoice_copies
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"脑脉利"}
    - slot{"apply_drug":"脑脉利"}
    - invoice_copies_form
    - form{"name": "invoice_copies_form"}
    - form{"name": null}
  - utter_is_help

* invoice_copies
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"百泽安"}
    - slot{"apply_drug":"百泽安"}
    - invoice_copies_form
    - form{"name":"invoice_copies_form"}
    - slot{"apply_drug":"百泽安"}
    - slot{"apply_drug":"百泽安"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_is_help

* invoice_copies
    - utter_ask_apply_drug
* chitchat
    - respond_chitchat
* provide_drug{"apply_drug":"百泽安"}
    - slot{"apply_drug":"百泽安"}
    - invoice_copies_form
    - form{"name":"invoice_copies_form"}
    - slot{"apply_drug":"百泽安"}
    - slot{"apply_drug":"百泽安"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_is_help

* invoice_copies
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - invoice_copies_form
    - form{"name":"invoice_copies_form"}
    - slot{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_is_help

* invoice_copies
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"吉至"}
    - slot{"apply_drug":"吉至"}
    - invoice_copies_form
    - form{"name": "invoice_copies_form"}
    - form{"name": null}
    - utter_is_help

* invoice_copies
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"益久"}
    - slot{"apply_drug":"益久"}
    - invoice_copies_form
    - form{"name": "invoice_copies_form"}
    - form{"name": null}
    - utter_is_help

* invoice_copies
    - utter_ask_apply_drug
* chitchat
    - respond_chitchat
* provide_drug{"apply_drug":"益久"}
    - slot{"apply_drug":"益久"}
    - invoice_copies_form
    - form{"name": "invoice_copies_form"}
    - form{"name": null}
    - utter_is_help


## 需人工
* invoice_copies
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"福可维"}
    - slot{"apply_drug":"福可维"}
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"apply_drug": "福可维"}
    - slot{"patient_name_mobile":"张三 17800000001"}
    - form{"name": null}