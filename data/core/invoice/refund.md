## 发票已报销
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + ofs + affirm
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
  - utter_is_help

## 发票已报销 + ofs + ofs + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* out_of_scope
  - utter_default
  - utter_ask_continue_invoice_refund
* out_of_scope
  - utter_default
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
  - utter_is_help


## 发票已报销 + faq + chitchat + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
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

## 发票已报销 + faq + chitchat + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + faq + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + faq + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + faq + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + faq + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + chitchat + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + chitchat + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + chitchat + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + chitchat + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + faq + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + faq + deny
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + faq + afirm + faq + faq + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + faq + faq + faq + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + faq + affirm + faq + afirm + faq + affirm
* invoice_refund
  - invoice_refund_form
  - form{"name": "invoice_refund_form"}
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
* faq
  - respond_faq
  - utter_ask_continue_invoice_refund
* affirm
  - utter_ok
  - invoice_refund_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help