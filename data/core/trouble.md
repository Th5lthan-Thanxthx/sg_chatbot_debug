## 发票丢失
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + ofs + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* out_of_scope
  - utter_default
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help


## 发票丢失 + faq + faq + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + chitchat + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + chitchat + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + ofs + ofs + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* out_of_scope
  - utter_default
  - utter_ask_continue_trouble_invoice_loss
* out_of_scope
  - utter_default
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + chitchat + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help


## 发票丢失 + faq + chitchat + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + chitchat + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + faq + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + faq + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + affirm + faq + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + affirm + faq + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + affirm + chitchat + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + affirm + chitchat + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + affirm + chitchat + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + affirm + chitchat + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + affirm + faq + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + chitchat + affirm + faq + deny
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + faq + afirm + faq + faq + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + faq + faq + faq + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票丢失 + faq + affirm + faq + affirm + faq + afirm + faq + affirm
* trouble_invoice_loss
  - trouble_invoice_loss_form
  - form{"name": "trouble_invoice_loss_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_loss
* affirm
  - utter_ok
  - trouble_invoice_loss_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help




## 发票已报销
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + ofs + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* out_of_scope
  - utter_default
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help


## 发票已报销 + faq + faq + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + chitchat + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + chitchat + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + ofs + ofs + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* out_of_scope
  - utter_default
  - utter_ask_continue_trouble_invoice_reimbursement
* out_of_scope
  - utter_default
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + chitchat + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help


## 发票已报销 + faq + chitchat + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + chitchat + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + faq + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + faq + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + faq + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + faq + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + chitchat + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + chitchat + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + chitchat + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + chitchat + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + faq + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + chitchat + affirm + faq + deny
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* chitchat
  - respond_chitchat
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* deny
  - utter_thumbsup
  - action_deactivate_form
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + faq + afirm + faq + faq + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + faq + faq + faq + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help

## 发票已报销 + faq + affirm + faq + affirm + faq + afirm + faq + affirm
* trouble_invoice_reimbursement
  - trouble_invoice_reimbursement_form
  - form{"name": "trouble_invoice_reimbursement_form"}
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
* faq
  - respond_faq
  - utter_ask_continue_trouble_invoice_reimbursement
* affirm
  - utter_ok
  - trouble_invoice_reimbursement_form
  - slot{"apply_drug": "福可维"}
  - form{"name": null}
  - utter_is_help