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
    - form{"name": "invoice_refund_form"}
    - form{"name": null}
    - utter_is_help


## 需人工
* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"恩立施"}
    - slot{"apply_drug":"恩立施"}
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}

* invoice_refund
    - utter_ask_apply_drug
* chitchat
    - respond_chitchat
* provide_drug{"apply_drug":"恩立施"}
    - slot{"apply_drug":"恩立施"}
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}

* invoice_refund
    - utter_ask_apply_drug
* provide_drug{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}

* invoice_refund
    - utter_ask_apply_drug
* chitchat
    - respond_chitchat
* provide_drug{"apply_drug":"瑞复美"}
    - slot{"apply_drug":"瑞复美"}
    - utter_prepare_handoff_to_human
    - prepare_handoff_to_human_form
    - form{"name": "prepare_handoff_to_human_form"}
    - slot{"patient_name":"张三"}
    - slot{"phone-number":"17800000001"}
    - form{"name": null}


<!-- ## 发票已报销 + ofs + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* out_of_scope
  - utter_default
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help


## 发票已报销 + faq + faq + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + chitchat + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + chitchat + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help -->