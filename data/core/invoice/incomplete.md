## 发票金额错误
* invoice_incomplete
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"恩立施"}
    - slot{"apply_drug":"恩立施"}
    - invoice_incomplete_form
    - form{"name": "invoice_incomplete_form"}
    - form{"name": null}
    - utter_is_help

* invoice_incomplete
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"脑脉利"}
    - slot{"apply_drug":"脑脉利"}
    - invoice_incomplete_form
    - form{"name": "invoice_incomplete_form"}
    - form{"name": null}
    - utter_is_help

* invoice_incomplete
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"吉至"}
    - slot{"apply_drug":"吉至"}
    - invoice_incomplete_form
    - form{"name": "invoice_incomplete_form"}
    - form{"name": null}
    - utter_is_help

* invoice_incomplete
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"益久"}
    - slot{"apply_drug":"益久"}
    - invoice_incomplete_form
    - form{"name": "invoice_incomplete_form"}
    - form{"name": null}
    - utter_is_help

* invoice_incomplete
    - utter_ask_apply_drug
* chitchat
    - respond_chitchat
* provide_drug{"apply_drug":"益久"}
    - slot{"apply_drug":"益久"}
    - invoice_incomplete_form
    - form{"name": "invoice_incomplete_form"}
    - form{"name": null}
    - utter_is_help


## 需人工
* greet
    - action_greet
* invoice_incomplete
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"福可维"}
    - slot{"apply_drug":"福可维"}
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}

* greet
    - action_greet
* invoice_incomplete
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}

* greet
    - action_greet
* invoice_incomplete
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"百泽安"}
    - slot{"apply_drug":"百泽安"}
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"apply_drug":"百泽安"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}

* invoice_loss
  - invoice_loss_form
  - form{"name": "invoice_loss_form"}
  - slot{"apply_drug":"百泽安"}
  - form{"name": null}
* invoice_incomplete
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"apply_drug":"百泽安"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}