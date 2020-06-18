## 发票已报销
* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"福可维"}
    - slot{"apply_drug":"福可维"}
    - invoice_refund_form
    - form{"name": "invoice_refund_form"}
    - form{"name": null}
    - utter_is_help

* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"脑脉利"}
    - slot{"apply_drug":"脑脉利"}
    - invoice_refund_form
    - form{"name": "invoice_refund_form"}
    - form{"name": null}
    - utter_is_help

* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"吉至"}
    - slot{"apply_drug":"吉至"}
    - invoice_refund_form
    - form{"name": "invoice_refund_form"}
    - form{"name": null}
    - utter_is_help

* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"益久"}
    - slot{"apply_drug":"益久"}
    - invoice_refund_form
    - form{"name": "invoice_refund_form"}
    - form{"name": null}
    - utter_is_help

* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"百泽安"}
    - slot{"apply_drug":"百泽安"}
    - invoice_refund_form
    - form{"name":"invoice_refund_form"}
    - slot{"apply_drug":"百泽安"}
    - slot{"apply_drug":"百泽安"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_is_help


## 需人工
* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"恩立施"}
    - slot{"apply_drug":"恩立施"}
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name_mobile":"张三 17800000001"}
    - form{"name": null}

* invoice_refund
    - utter_ask_apply_drug
* chitchat
    - respond_chitchat
* provide_drug{"apply_drug":"恩立施"}
    - slot{"apply_drug":"恩立施"}
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name_mobile":"张三 17800000001"}
    - form{"name": null}

* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - prepare_handoff_to_human_form
    - form{"name":"prepare_handoff_to_human_form"}
    - slot{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - slot{"patient_name_mobile":"张三 17800000001"}
    - form{"name": null}

* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - prepare_handoff_to_human_form
    - form{"name":"prepare_handoff_to_human_form"}
    - slot{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - slot{"requested_slot":"patient_name_mobile"}
* invoice_refund{"patient_name":"张三"}
    - slot{"patient_name":"张三"}
    - prepare_handoff_to_human_form
    - slot{"patient_name_mobile":"张三"}
    - form{"name":null}
    - slot{"requested_slot":null}