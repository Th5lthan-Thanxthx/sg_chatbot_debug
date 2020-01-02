## ask invoice loss
* greet
  - utter_greet
* ask_invoice_loss
  - ask_invoice_form
  - form{"name": "ask_invoice_form"}
  - form{"name": null}

<!-- * greet
  - utter_greet
* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receipt
* affirm
  - query_receipt_form
  - form{"name": null} -->

<!-- * greet
  - utter_greet
* query_receipt_address
  - query_receipt_form
  - form{"name": "query_receipt_form"}
* out_of_scope
  - utter_out_of_scope
  - utter_ask_continue_query_receipt
* deny
  - action_deactivate_form
  - form{"name": null} -->

## ask invoice reimbursement
* greet
  - utter_greet
* ask_invoice_reimbursement
  - ask_invoice_reimbursement_form
  - form{"name": "ask_invoice_reimbursement_form"}
  - form{"name": null}



<!-- * greet
  - utter_greet
* ask_invoice_reimbursement
  - action_invoice_reimbursement
* provide_drug{"apply_drug":"福可维"}
  - utter_aks_drug_reimbursement
* deny
  - utter_drug_reimbursement_no_fkw
* how_to_certificate_no_reimbursement
  - utter_invoice_no_reimbursement_certificate
   -->
<!-- * greet
  - utter_greet
* ask_invoice_reimbursement
  - action_invoice_reimbursement
* provide_drug{"apply_drug":"瑞复美"}
  - utter_question_not_fit -->


<!-- * greet
  - utter_greet
* ask_invoice_reimbursement
  - action_invoice_reimbursement
* provide_drug{"apply_drug":"瑞复美"}
  - utter_question_not_fit -->

<!-- * greet
  - utter_greet
* ask_invoice_reimbursement
  - action_invoice_reimbursement
* affirm
  - utter_drug_reimbursement_yes_fkw 
  
* greet
  - utter_greet
* ask_invoice_reimbursement
  - action_invoice_reimbursement
* deny
  - utter_drug_reimbursement_no_fkw
* how_to_certificate_no_reimbursement
  - utter_invoice_no_reimbursement_certificate -->



