from django.urls import path 
from HRMS import views

app_name = "HRMS"
urlpatterns = [
    path('add-client' , views.add_client_Function , name="add_client"),
    path('client-lists' , views.client_lists_Function , name="client_lists"),
    path('update-client/<int:client_id>/', views.editt_client_Function, name='editt_client_Function'),
    path('delete-client/<int:client_id>/' , views.delete_client_Function , name="delete_client_Function"),

    path('client-status/<int:client_id>/' , views.client_status_Function , name="client_status"),
    path('get-client-details/', views.get_client_details, name='get_client_details'),
    
    path('search_clients/', views.search_clients, name='search_clients'),
    path('add-division' , views.add_division_Function , name="add_division"),
    path('division-lists' , views.division_lists_Function , name="division_lists"),
    path('update-division/<int:division_id>/' , views.update_division_Function , name="update_division"),
    path('delete-division/<int:division_id>/', views.delete_division_Function, name='delete_division'),

    path('division-status/<int:division_id>/', views.division_status_Function, name='division_status'),
    
    path('add/service/charges' , views.add_ServiceCharge_Function , name="add_servicecharge"),
    
    path('client/estimate/billing' , views.client_Billing_Function , name="client_estimatebilling"),
    path('add_estimate/<int:division_id>/', views.add_estimate_billing, name='add_estimate'),
    path('add_clientdivisionestimatebilling/<int:division_id>/', views.add_clientdivisionestimatebilling, name='add_clientdivisionestimatebilling'),

    
    path('inactive/client/lists' , views.inactiveClient_list_Function , name="inactive_client"),
    path('inactive/division/lists' , views.inactiveDivision_list_Function , name="inactive_division"),
    
#     # Employee Module 
#     # ==========================
    path('search_employee/', views.search_employee, name='search_employee'),
    # path('get_divisions/', views.get_divisions, name='get_divisions'),
    path('get_employee_details/', views.get_employee_details, name='get_employee_details'),
    path('add/employee/details' , views.add_Employee_Function , name="add_employee"),
    path('employee_lists/' , views.employee_lists_Function , name="employee_list"),
    path('edit/employee/details' , views.edit_Employee_Function , name="edit_employee"),
    path('update/employee/division' , views.update_employee_division_function , name="update_employee_division"),
    path('Employee/loan/advance/details' , views.Employee_loan_advance_details_Function , name="loan_advance_details"),
    path('Add/Employee/loan/' , views.Add_employee_loan_Function , name="add_loan"),
    path('Employee/salary/update/request' , views.Employee_salary_update_request_Function , name="salary_update_request"),
    path('Employee/salary/update/status/' , views.Employee_salary_update_status_Function , name="salary_update_status"),
    path('Employee/salary/approval/status' , views.Employee_salary_Approval_Function , name="salary_salary_approval"),

    path('update_salary/<int:emp_id>/', views.update_salary, name='update_salary'),

    path('Employee/salary/verification/' , views.salary_Function , name="salary_Function"),

    path('Employee/epf/verification/' , views.epf_Function , name="epf_Function"),

    path('Employee/esi/verification/' , views.esi_Function , name="esi_Function"),
    
    path('approve_salary' , views.approve_salary , name="approve_salary"),


#     # Payment Module 
#     # ==========================
    path('approved_salary_payment/' , views.approved_salary_payment , name="approved_salary_payment"),
    path('approved_epf_deposite/' , views.approved_epf_deposite , name="approved_epf_deposite"),
    path('approved_esi_deposite/' , views.approved_esi_deposite , name="approved_esi_deposite"),


#     # Bill Module 
#     # ==========================
    path('bill_entry/' , views.bill_entry , name="bill_entry"),
    path('add_new_bill/' , views.add_new_bill , name="add_new_bill"),
    path('view_bill/' , views.view_bill , name="view_bill"),
    path('bill_receive/' , views.bill_receive , name="bill_receive"),
    path('add_bill_receive_details/' , views.add_bill_receive_details , name="add_bill_receive_details"),
    path('client_expenditure/' , views.client_expenditure , name="client_expenditure"),
    path('add_expenditure/' , views.add_expenditure , name="add_expenditure"),
    path('view_expenditure_details/' , views.view_expenditure_details , name="view_expenditure_details"),
    path('generate_bill/' , views.generate_bill , name="generate_bill"),
    path('view_generate_bill/' , views.view_generate_bill , name="view_generate_bill"),
    path('generate_new_bill/' , views.generate_new_bill , name="generate_new_bill"),
    path('proforma_bill/' , views.proforma_bill , name="proforma_bill"),
    path('add_proforma_bill_invoice/' , views.add_proforma_bill_invoice , name="add_proforma_bill_invoice"),
    path('view_proforma_bill_invoice/' , views.view_proforma_bill_invoice , name="view_proforma_bill_invoice"),
    
    path('fetch_divisions/' , views.fetch_divisions , name="fetch_divisions"),
    path('searchclienTdivisioN_bills/' , views.searchclienTdivisioN_bills , name="searchclienTdivisioN_bills"),
    path('bill_approval/' , views.bill_approval , name="bill_approval"),
    path('bill_disapproval/' , views.bill_disapproval , name="bill_disapproval"),
    path('gst_bill_prepare/' , views.gst_bill_prepare , name="gst_bill_prepare"),
    path('gst_bill_pending/' , views.gst_bill_pending , name="gst_bill_pending"),


#     # Bill Report Module 
#     # ===========================================================================================
    
    path('bill_submitted/' , views.bill_submitted , name="bill_submitted"),
    path('bill_received/' , views.bill_received , name="bill_received"),
    path('expenditure_report/' , views.expenditure_report , name="expenditure_report"),
    path('bill_outstanding/' , views.bill_outstanding , name="bill_outstanding"),
    path('client_profit_loss_statement/' , views.client_profit_loss_statement , name="client_profit_loss_statement"),
    path('gst_received_reports/' , views.gst_received_reports , name="gst_received_reports"),
    path('tds_reports/' , views.tds_reports , name="tds_reports"),
    path('date_wise_bill_received/' , views.date_wise_bill_received , name="date_wise_bill_received"),
    path('month_wise_bill_register/' , views.month_wise_bill_register , name="month_wise_bill_register"),
    path('payment_not_received/' , views.payment_not_received , name="payment_not_received"),
    path('bill_not_despatched/' , views.bill_not_despatched , name="bill_not_despatched"),
    path('date_wise_bill_submited/' , views.date_wise_bill_submited , name="date_wise_bill_submited"),

#     # Tender Module 
#     # ===========================================================================================
    path('company_essential_documents/' , views.company_essential_documents , name="company_essential_documents"),
    path('add_new_document/' , views.add_new_document , name="add_new_document"),

    path('tenders/' , views.tenders , name="tenders"),
    path('add_new_tender/' , views.add_new_tender , name="add_new_tender"),

    path('tender_prepration/' , views.tender_prepration , name="tender_prepration"),
    
    path('tender_financial_bid/' , views.tender_financial_bid , name="tender_financial_bid"),
    path('add_financial_bid_details/' , views.add_financial_bid_details , name="add_financial_bid_details"),
    path('add_status_details/' , views.add_status_details , name="add_status_details"),
    path('view_tender_financial_bid/' , views.view_tender_financial_bid , name="view_tender_financial_bid"),

    path('tender_status_upload/' , views.tender_status_upload , name="tender_status_upload"),
    path('view_tender_status_upload/' , views.view_tender_status_upload , name="view_tender_status_upload"),

    path('tender_submited/' , views.tender_submited , name="tender_submited"),
    path('tender_not_submited/' , views.tender_not_submited , name="tender_not_submited"),
    path('tender_expired/' , views.tender_expired , name="tender_expired"),

#     # users Module 
#     # ===========================================================================================
    path('add_new_user/' , views.add_new_user , name="add_new_user"),
    path('create_users/' , views.create_users , name="create_users"),
    path('asigned_client/' , views.asigned_client , name="asigned_client"),

    path('menu_access/' , views.menu_access , name="menu_access"),
    path('user_status_review/' , views.user_status_review , name="user_status_review"),
    path('branch_status_review/' , views.branch_status_review , name="branch_status_review"),
    path('monthly_status_review/' , views.monthly_status_review , name="monthly_status_review"),
    
    #Payroll Module :-
    
    path('process/attendance/' , views.Add_attendance_function , name="Add_attendance_function") ,
    path('Save_attendance_function/' , views.Save_attendance_function , name="Save_attendance_function") ,
    path('edit/attendance/' , views.Edit_attendance_function , name="Edit_attendance_function") ,
    path('approve/attendance/' , views.Approve_attendance_function , name="Approve_attendance_function") ,
    path('approve_attendance/' , views.approve_attendance , name="approve_attendance") ,
    path('reject_attendance/' , views.reject_attendance , name="reject_attendance") ,
    path('submit_attendance/' , views.submit_attendance , name="submit_attendance") ,
    path('return_attendance/' , views.return_attendance , name="return_attendance") ,
    
    path('view_attendance/<int:header_id>/', views.view_attendance, name='view_attendance'),
    path('submit_attendance/', views.submit_attendance, name='submit_attendance'),
    path('delete_attendance/', views.delete_attendance, name='delete_attendance'),
    
    
    
    
    path('process/salary/', views.Add_salary_function, name='Add_salary_function'),
    path('edit/salary/', views.edit_salary_function, name='edit_salary_function'),
    path('submit_salary/', views.submit_salary, name='submit_salary'),
    
    path('view_salary/<int:header_id>/', views.view_salary, name='view_salary'),

    path('delete_salary/', views.delete_salary, name='delete_salary'),
    
    path('approve/salaries/' , views.Approve_salary_function , name="Approve_salary_function") ,
    path('approve_salary/', views.approve_salary, name='approve_salary'),
    path('reject_salary/', views.reject_salary, name='reject_salary'),
    path('return_salary/', views.return_salary, name='return_salary'),

    
# Reports Module :-

    path('client_reports/' , views.client_reports , name="client_reports") ,
    path('employees_reports/' , views.employees_reports , name="employees_reports") ,


]



