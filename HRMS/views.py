from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth import login , logout , authenticate 
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'admin_login.html')

def admin_logout_view(request):
    logout(request)
    return redirect('admin_login')


def admin_dashboard(request):
    return render(request , "hrms/index.html")

def admin_dashboard_old(request):
    return render(request , "hrms/index1.html")


def add_client_Function(request):
    if request.method == 'POST':
        try:
            client_name = request.POST.get('client_name')
            client_short_name = request.POST.get('client_short_name')
            client_code = request.POST.get('client_code')
            client_address = request.POST.get('client_address')
            client_district = request.POST.get('client_district')
            client_state = request.POST.get('client_state')
            client_pincode = request.POST.get('client_pincode')
            client_office_phone = request.POST.get('client_office_phone')
            client_client_email = request.POST.get('client_client_email')
            client_work_contract_no = request.POST.get('client_work_contract_no')
            client_start_date = request.POST.get('client_start_date')
            client_end_date = request.POST.get('client_end_date')
            client_GST_No = request.POST.get('client_GST_No')
            client_Contract_Value = request.POST.get('client_Contract_Value')
            client_Bonus = request.POST.get('client_Bonus')
            client_EPF = request.POST.get('client_EPF')
            client_ESI = request.POST.get('client_ESI')
                
            
            name = request.POST.get("name")
            mobile_number = request.POST.get("mobile_number")
            email = request.POST.get("email")
            designation = request.POST.get("designation")
            
            if Clientmst.objects.filter(cname=client_name).exists():
                return JsonResponse({'success': False, 'message': 'Client with the same name already exists.'})

            client = Clientmst(
                cname=client_name,
                csname=client_short_name,
                ccode=client_code,
                address=client_address,
                district=client_district,
                state=client_state,
                pin=client_pincode,
                oficeph=client_office_phone,
                email=client_client_email,
                contractno=client_work_contract_no,
                startdate=client_start_date,
                enddate=client_end_date,
                gstno=client_GST_No,
                contractvalue=client_Contract_Value,
                bonus=client_Bonus,
                epf=client_EPF,
                esi=client_ESI,
                userid =request.user.username ,
                        
                contactperson=name,
                contactmobileno=mobile_number,
                contactemail=email,
                contactdesg=designation,
                    )
            client.save()
            return JsonResponse({'success': True, 'message': 'Client added successfully.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
    return render(request, "admin/master/add_client.html")

def editt_client_Function(request, client_id):
    client = Clientmst.objects.get(cid=client_id)
    if request.method == 'POST':
        try:
            client_name = request.POST.get('client_name')
            client_short_name = request.POST.get('client_short_name')
            client_code = request.POST.get('client_code')
            client_address = request.POST.get('client_address')
            client_district = request.POST.get('client_district')
            client_state = request.POST.get('client_state')
            client_pincode = request.POST.get('client_pincode')
            client_office_phone = request.POST.get('client_office_phone')
            client_client_email = request.POST.get('client_client_email')
            client_work_contract_no = request.POST.get('client_work_contract_no')
            client_start_date = request.POST.get('client_start_date')
            client_end_date = request.POST.get('client_end_date')
            client_GST_No = request.POST.get('client_GST_No')
            client_Contract_Value = request.POST.get('client_Contract_Value')
            client_Bonus = request.POST.get('client_Bonus')
            client_EPF = request.POST.get('client_EPF')
            client_ESI = request.POST.get('client_ESI')
            name = request.POST.get("name")
            mobile_number = request.POST.get("mobile_number")
            email = request.POST.get("email")
            designation = request.POST.get("designation")
            remark = request.POST.get("remark")

            client.cname = client_name
            client.csname = client_short_name
            client.ccode = client.ccode
            client.address = client_address
            client.district = client_district
            client.state = client_state
            client.pin = client_pincode
            client.oficeph = client_office_phone
            client.email = client_client_email
            client.contractno = client_work_contract_no
            client.startdate = client_start_date
            client.enddate = client_end_date
            client.gstno = client_GST_No
            client.contractvalue = client_Contract_Value
            client.bonus = client_Bonus
            client.epf = client_EPF
            client.esi = client_ESI
            client.contactperson = name
            client.contactmobileno = mobile_number
            client.contactemail = email
            client.contactdesg = designation
            client.save()
        
            response_data = {
                'success': True, 
                'message': 'Client data Updated successfully'
            }
        except Exception as e:
            response_data = {
                'success': False, 
                'message': str(e)
            }
        
        return JsonResponse(response_data)
   
    context = {
            'client': client,
        }
    
    return render(request, "admin/master/update_client.html", context)


def client_lists_Function(request):
    clients = Clientmst.objects.all().order_by("-cid")
    context = {
        "clients": clients,
    }
    return render(request, "admin/master/Clientmaster.html", context)


def delete_client_Function(request , client_id):
    try:
        client = get_object_or_404(Clientmst , cid=client_id)
        client.delete()
        response_data = {
            'success': True,
            'message': 'Client Details deleted successfully.'
        }
    except Exception as e:
        response_data = {
            'success': False,
            'message':  str(e)
        }
    
    return JsonResponse(response_data)

def client_status_Function(request, client_id):
    try:
        client = get_object_or_404(Clientmst, cid=client_id)
        client.toggle_status()

        # Determine the label to display based on the current state
        label = "Activate" if client.activests else "Deactivate"

        return JsonResponse({"success": True, "message": f"Client is now {label}"})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})

@csrf_exempt
def search_clients(request):
    keyword = request.GET.get('keyword', '')

    # Search by both cname and ccode
    clients = Clientmst.objects.filter(
        Q(cname__icontains=keyword) | Q(ccode__icontains=keyword)
    ).values('ccode', 'cname')

    return JsonResponse({'clients': list(clients)})

def fetch_divisions(request):
    client_name = request.GET.get('client_name', '')
    ccode, cname = map(str.strip, client_name.split('-'))
    
    divisions = Divisionmst.objects.filter(cid__cname__icontains=cname).values('did', 'division')
    return JsonResponse({'divisions': list(divisions)})


def add_division_Function(request):
    if request.method == "POST":
        client_name = request.POST['client_name']
        division_name = request.POST['division_name']
        bank_name = request.POST['bank_name']
        ifsc_code = request.POST['ifsc_code']
        virtual_account_number = request.POST['virtual_account_number']

        if Divisionmst.objects.filter(division=division_name).exists():
                return JsonResponse({'success': False, 'message': 'Division with the same name already exists.'})

        ccode, cname = map(str.strip, client_name.split('-'))
        
        client = get_object_or_404(Clientmst, ccode=ccode)
        
        try:
            
            division_object = Divisionmst(
                cid=client,
                division=division_name,
                bankname=bank_name,
                ifsccode=ifsc_code,
                bankaccno=int(virtual_account_number) ,
                userid =request.user.username
            )
            division_object.save()
            return JsonResponse({'success': True, 'message': 'Division added successfully.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
    return render(request, "admin/master/add_division.html")

def update_division_Function(request, division_id):
    if request.method == "POST":
        
        division = get_object_or_404(Divisionmst, did=division_id)
        
        division_name = request.POST['division_name']
        bank_name = request.POST['bank_name']
        ifsc_code = request.POST['ifsc_code']
        virtual_account_number = int(request.POST['virtual_account_number'])

        print(type(virtual_account_number))

        try:
            
            division.cid = division.cid
            division.division = division_name
            division.bankname = bank_name
            division.ifsccode = ifsc_code
            division.bankaccno = int(virtual_account_number)
            division.modifyuser = request.user.username
            division.save()

            response_data = {
                'success': True,
                'message': 'Division updated successfully'
            }
        except Exception as e:
            response_data = {
                'success': False,
                'message': str(e)
            }

        return JsonResponse(response_data)

    division = Divisionmst.objects.get(did=division_id)
    context = {
        'division': division
    }

    return render(request, "admin/master/update_division.html", context)

def delete_division_Function(request, division_id):
    try:
        # Get the division object to delete
        division = get_object_or_404(Divisionmst, did=division_id)

        # Perform the deletion
        division.delete()

        # If deletion is successful
        response_data = {
            'success': True,
            'message': 'Division deleted successfully.'
        }
    except Exception as e:
        # If an error occurs during deletion
        response_data = {
            'success': False,
            'message': 'An error occurred while deleting the division.'
        }
    
    return JsonResponse(response_data)

def division_lists_Function(request):
    divisions = Divisionmst.objects.filter(activests=True)
    context = {
        "divisions" : divisions
    }
    return render(request , "admin/master/division_lists.html" , context)

def division_status_Function(request, division_id):
    try:
        division = get_object_or_404(Divisionmst, did=division_id)
        division.toggle_status()

        label = "Activate" if division.activests else "Deactivate"
        # Toggle the is_active field
        return JsonResponse({"success": True, "message": f"Client is now {label}"})
        
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})
    
def add_ServiceCharge_Function(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        employee_epf = request.POST.get('employee_epf')
        employer_epf = request.POST.get('employer_epf')
        max_epf_wages = request.POST.get('max_epf_wages')
        employee_esi = request.POST.get('employee_esi')
        employer_esi = request.POST.get('employer_esi')
        max_esi_wages = request.POST.get('max_esi_wages')
        print(client_name)
        
        
        try:
            client_mst = Clientmst.objects.get(cname=client_name)
            print(client_mst)
            
            client_charge = Clientcharges.objects.get(cid = client_mst)
            print(client_charge)
            
            # Update the existing record with the new values
            client_charge.empepf = employee_epf
            client_charge.emprepf = employer_epf
            client_charge.epfwages = max_epf_wages
            client_charge.empesi = employee_esi
            client_charge.empresi = employer_esi
            client_charge.esiwages = max_esi_wages
            client_charge.save()

            return JsonResponse(
                {
                    'success': True, 
                    'message': 'Data updated successfully!'
                }
            )

        except Clientcharges.DoesNotExist:
            client = Clientcharges.objects.get(cid__cname=client_name)
            new_client_charge = Clientcharges(
                cid=client,
                empepf=employee_epf,
                emprepf=employer_epf,
                epfwages=max_epf_wages,
                empesi=employee_esi,
                empresi=employer_esi,
                esiwages=max_esi_wages
            )
            new_client_charge.save()

            return JsonResponse({'message': 'Data saved successfully!'})

        except Exception as e:
            # Handle other exceptions and return an error message
            return JsonResponse({'message': f'Error: {e}'}, status=500)
        
    return render(request , "admin/master/add_clientservicecharges.html")

def get_client_details(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        try:
            client_charge = Clientcharges.objects.get(cid__cname=client_name)
            data = {
                    'employee_epf': client_charge.empepf,
                    'employer_epf': client_charge.emprepf,
                    'max_epf_wages': client_charge.epfwages,
                    'employee_esi': client_charge.empesi,
                    'employer_esi': client_charge.empresi,
                    'max_esi_wages': client_charge.esiwages
                }
            return JsonResponse(data)
        except Clientcharges.DoesNotExist:
                # Data does not exist, return default values
                data = {
                    'employee_epf': 12,
                    'employer_epf': 13,
                    'max_epf_wages': 15000,
                    'employee_esi': 0.75,
                    'employer_esi': 3.25,
                    'max_esi_wages': 21000
                }
        return JsonResponse(data)
        

def inactiveClient_list_Function(request):
    inactive_clients = Clientmst.objects.filter(activests=False)
    context = {
        "inactive_clients": inactive_clients,
    }
    return render(request, "admin/master/inactiveClient.html", context)

def inactiveDivision_list_Function(request):
    inactiveDivisions = Divisionmst.objects.filter(activests = False)
    context={
        "inactiveDivisions" : inactiveDivisions
    }   
    return render(request , "admin/master/inactiveDivision.html" , context)


def client_Billing_Function(request):
    divisions = Divisionmst.objects.all()
    context = {
        "divisions" : divisions
    }
    return render(request , "admin/master/Clientestimatebilling.html" , context)


def add_estimate_billing(request, division_id):
    div = get_object_or_404(Divisionmst, did=division_id)

    if request.method == 'POST':
        category = request.POST.get('category')
        strength = request.POST.get('strength')
        empwages = request.POST.get('Employee_wages')
        perempwages = request.POST.get('Total_wages')
        epfwages = request.POST.get('EPF_wages')
        esiwages = request.POST.get('ESI_wages')
        epf = request.POST.get('EPF')
        esi = request.POST.get('ESI')
        epfsts = request.POST.get('epfRadio')
        esists = request.POST.get('esiRadio')
        
        objectInstance = Clientdivisionestimatebillingdtl.objects.create(
            cid=div.cid,
            did=div,
            category=category,
            strength=strength,
            empwages=empwages,
            perempwages=perempwages,
            epfwages=epfwages,
            esiwages=esiwages,
            epf=epf,
            esi=esi,
            epfsts=epfsts,
            esists=esists,
            cuserid=request.user.username,
        )
        return redirect('HRMS:add_estimate', division_id=division_id)
        
        
    estimate_billing_dtls = Clientdivisionestimatebillingdtl.objects.filter(did=division_id, cid=div.cid)

    context = {
        'div': div,
        'estimate_billing_dtls': estimate_billing_dtls,
    }

    return render(request, "admin/master/add_estimatebilling.html", context)


def add_clientdivisionestimatebilling(request , division_id):
    div = get_object_or_404(Divisionmst, did=division_id)
    if request.method == 'POST':
        strength = request.POST.get('strength')
        billingwages = request.POST.get('billingwages')
        billingepf = request.POST.get('billingepf')
        billingesi = request.POST.get('billingesi')
        seviceon = request.POST.get('seviceon')
        sevicecharge = request.POST.get('sevicecharge')
        totalsevicecharge = request.POST.get('totalsevicecharge')
        bonus = request.POST.get('bonus')
        leave = request.POST.get('leave')
        nfholidays = request.POST.get('nfholidays')
        gst = request.POST.get('gst')
        
        
        material = request.POST.get('material')
        fule = request.POST.get('fule')
        machinary = request.POST.get('machinary')
        others = request.POST.get('others')
        totalgst = request.POST.get('totalgst')
        totalestimate = request.POST.get('totalestimate')
        selected_checkboxes = request.POST.getlist('gston')
        gston = ','.join(selected_checkboxes)
        
        data = Clientdivisionestimatebilling.objects.create(
            cid=div.cid,
            did=div,
            strength = strength ,
            billingwages = billingwages ,
            billingepf = billingepf ,
            billingesi = billingesi ,
            seviceon = seviceon ,
            sevicecharge = sevicecharge ,
            totalsevicecharge = totalsevicecharge ,
            bonus = bonus ,
            leave = leave ,
            nfholidays = nfholidays ,
            gst = gst ,
            material = material ,
            fule = fule ,
            machinary = machinary ,
            totalgst = totalgst ,
            others = others ,
            totalestimate = totalestimate ,
            gston = gston ,
            cuserid = request.user.username
        )
        return redirect('HRMS:add_estimate', division_id=division_id)
    


# # Employee Module 
# # ===========================================================================================
# from .models import Employee , Division_Table
# @csrf_exempt
# def get_divisions(request):
#     client_name = request.GET.get('client_name', '')
#     divisions = Division_Table.objects.filter(client__client_name=client_name).values_list('division_name', flat=True)
#     return JsonResponse({'divisions': list(divisions)})


def add_Employee_Function(request):
    if request.method == 'POST':
        
        empname = request.POST.get('empname')
        empfhname = request.POST.get('empfhname')
        empdob = request.POST.get('empdob')  # Assuming this is a date in the format YYYY-MM-DD
        qualification = request.POST.get('qualification')
        mobileno = request.POST.get('mobileno')
        emergencyno = request.POST.get('emergencyno')
        bloodgroup = request.POST.get('bloodgroup')
        gender = request.POST.get('gender')
        joinningdate = request.POST.get('joinningdate')  # Assuming this is a date in the format YYYY-MM-DD
        department = request.POST.get('department')
        desgination = request.POST.get('desgination')
        preaddress = request.POST.get('preaddress')
        precity = request.POST.get('precity')
        predist = request.POST.get('predist')
        prestate = request.POST.get('prestate')
        prepin = request.POST.get('prepin')
        peraddress = request.POST.get('peraddress')
        percity = request.POST.get('percity')
        perdist = request.POST.get('perdist')
        perstate = request.POST.get('perstate')
        perpin = request.POST.get('perpin')
        unno = request.POST.get('unno')
        aadharno = request.POST.get('aadharno')
        bankname = request.POST.get('bankname')
        accountno = request.POST.get('accountno')
        ifsccode = request.POST.get('ifsccode')
        basic = request.POST.get('basic')
        hra = request.POST.get('hra')
        others = request.POST.get('others')
        conv = request.POST.get('conv')
        maxepf = request.POST.get('maxepf')
        maxesi = request.POST.get('maxesi')
        lta = request.POST.get('lta')
        medical = request.POST.get('medical')
        resallow = request.POST.get('resallow')
        epfno = request.POST.get('epfno')
        esino = request.POST.get('esino')
        wagestype = request.POST.get('wagestype')
        billtype = request.POST.get('billtype')
        bonus = request.POST.get('bonus')
        leave = request.POST.get('leave')
        epf = request.POST.get('epf')
        esi = request.POST.get('esi')
        


        division_id = request.POST.get('division_id')
        print(division_id)
        
        did = get_object_or_404(Divisionmst , did = division_id)
        
        try:
            
        # Create and save a new EmployeeMst instance
            employee = Employeemst(
                empname=empname,
                empfhname=empfhname,
                empdob=empdob,
                qualification=qualification,
                mobileno=mobileno,
                emergencyno=emergencyno,
                bloodgroup=bloodgroup,
                gender=gender,
                joinningdate=joinningdate,
                department=department,
                desgination=desgination,
                preaddress=preaddress,
                precity=precity,
                predist=predist,
                prestate=prestate,
                prepin=prepin,
                peraddress=peraddress,
                percity=percity,
                perdist=perdist,
                perstate=perstate,
                perpin=perpin,
                unno=unno,
                aadharno=aadharno,
                bankname=bankname,
                accountno=accountno,
                ifsccode=ifsccode,
                basic=basic,
                hra=hra,
                others=others,
                conv=conv,
                maxepf=maxepf,
                maxesi=maxesi,
                lta=lta,
                medical=medical,
                resallow=resallow,
                epfno=epfno,
                esino=esino,
                wagestype=wagestype,
                billtype=billtype,
                bonus=bonus,
                leave=leave,
                epf=epf,
                esi=esi,
                cid=did.cid,
                did=did ,
                userid = request.user.username
            )
            employee.save()
            response_data = {
                    'success': True, 
                    'message': 'Employee data saved successfully'
                }
        except Exception as e:
                response_data = {
                    'success': False, 
                    'message': str(e)
                }
    
        return JsonResponse(response_data)

    return render(request, "admin/employee/add_employee.html")
    
def employee_lists_Function(request):
    employees = Employeemst.objects.all()
    context = {
        "employees" : employees
    }
    return render(request , "admin/employee/employee_lists.html" , context)


def edit_Employee_Function(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        try:
            # Search for the employee by EmpCode or EmpName
            employee = Employeemst.objects.get(Q(empcode__icontains=search_query) | Q(empname__icontains=search_query))
            
            # Fetch the associated Division for this employee
            division = employee.did  # Assuming 'did' is the ForeignKey field on the Employee model

            return render(request, "admin/employee/edit_employee.html", {"employee": employee, "division": division})
        except Employeemst.DoesNotExist:
            # Employee not found, you can handle this case as needed
            return render(request, "admin/employee/edit_employee.html", {'error_message': 'Employee not found'})
        
    return render(request, "admin/employee/edit_employee.html")

def update_employee_division_function(request):
    full_client_name = "LKXXX-XXXX"
    
    if request.method == 'POST':
        full_client_name = request.POST.get('client_name')
        selected_division_id = request.POST.get('division')

        if selected_division_id:
            selected_division = Divisionmst.objects.get(did=selected_division_id)
            selected_employee_ids = request.POST.getlist('selected_employees')

            for employee_id in selected_employee_ids:
                employee = Employeemst.objects.get(empid=employee_id)
                employee.did = selected_division
                employee.save()

    # Split the full client name into code and name
    parts = map(str.strip, full_client_name.split('-'))
    
    # Provide default values for ccode and cname if needed
    ccode = next(parts, "")
    cname = next(parts, "")

    divisions = Divisionmst.objects.filter(cid__cname=cname)
    
    employees = Employeemst.objects.filter(did__cid__cname=cname)
    
    context = {'divisions': divisions, 'employees': employees, 'client_name': cname}
    return render(request, "admin/employee/update_employee_division.html", context)

@csrf_exempt
def search_employee(request):
    keyword = request.GET.get('keyword', '')
    employeeCode = Employeemst.objects.filter(empcode__icontains=keyword).values_list('empcode' , flat=True)
    return JsonResponse({'clients': list(employeeCode)})

def get_employee_details(request):
    if request.method == 'POST':
        empcode = request.POST.get('employee_code')

        try:
            # Retrieve the employee based on the employee code
            employee = Employeemst.objects.get(empcode=empcode)

            # Get the client, division, and designation details
            client = employee.did.cid.cname
            division = employee.did.division
            desgination = employee.desgination
            department = employee.department

            # Return the details as JSON
            data = {
                'client': client,
                'division': division,
                'desgination': desgination,
                'department': department,
            }
            return JsonResponse(data)

        except Employeemst.DoesNotExist:
            # Handle the case where no matching employee is found
            return JsonResponse({'error': 'Employee not found'}, status=400)

    # Handle other HTTP methods or cases
    return JsonResponse({}, status=405)


def Employee_loan_advance_details_Function(request):
    loans = Emploanhdr.objects.all().order_by("-lid")
    context = {
        "loans" : loans
    }
    return render(request , "admin/employee/loanAdvance_details.html" , context)

def Add_employee_loan_Function(request):
    if request.method == 'POST':
        # Get data from the POST request
        empcode = request.POST.get('employee_code')  
        loanamount = request.POST.get('loanamount')
        noinst = request.POST.get('noinst')
        instamount = request.POST.get('instamount')
        
        selected_month = int(request.POST.get("selected_month"))
        selected_year = int(request.POST.get("selected_year"))
        year_month = f"{selected_year}-{selected_month:01}"  
        
        try:
            # Try to retrieve the employee based on empcode
            employee = Employeemst.objects.get(empcode=empcode)
            
            # Create a new Emploanhdr instance and save it to the database
            with transaction.atomic():
                loan = Emploanhdr(
                    empid=employee,
                    empcode=empcode,
                    loanamount=loanamount,
                    noinst=noinst,
                    instamount=instamount,
                    startyearmonth=year_month,
                    cuserid = request.user.username
                    
                )
                loan.save()
            
            response_data = {
                'success': True, 
                'message': 'Loan data saved successfully'
            }
        except Employeemst.DoesNotExist:
            response_data = {
                'success': False, 
                'message': 'Employee with the specified empcode does not exist'
            }
        except Exception as e:
            response_data = {
                'success': False, 
                'message': str(e)
            }
    
        return JsonResponse(response_data)
    
    return render(request, "admin/employee/add_loan.html")

def Employee_salary_update_request_Function(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        division_id = request.POST.get('division_id')

        
        ccode, cname = map(str.strip, client_name.split('-'))
        
        client = get_object_or_404(Clientmst, ccode=ccode)
        division = get_object_or_404(Divisionmst, did=division_id)
        
        
        # Query employees based on client and division
        employees = Employeemst.objects.filter(
            cid=client,
            did=division
        )

        return render(request, 'admin/employee/salary_updation.html', {'employees': employees})

    return render(request, "admin/employee/salary_updation.html")

def update_salary(request, emp_id):
    if request.method == 'POST':
        try:
            # Get the employee by ID
            employee = get_object_or_404(Employeemst, pk=emp_id)

            # Get the new basic salary from POST data
            increment = float(request.POST.get('incrementAmount'))
            cwagestype = employee.wagestype
            cbasic = employee.basic
            
            totalgross = cbasic + increment

            # Update the wage type based on the checkbox
            wage_type_checked = request.POST.get('wageType')
            if wage_type_checked:
                uwagestype = '1'
            else:
                uwagestype = '2'
            # Create a new record in Employeesalaryupdate
            Employeesalaryupdate.objects.create(
                empid=employee,
                cwagestype=cwagestype,
                cbasic=cbasic,
                uwagestype=uwagestype,
                ubasic = cbasic + increment,
                increment=increment,
                totalgross=totalgross ,
                cuserid = request.user.username
                
            )

            return JsonResponse({'success': True, 'message': 'Salary updated successfully'})
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid salary value'}, status=400)

    # If it's not a POST request or other exceptions occur, render the template
    employee = get_object_or_404(Employeemst, pk=emp_id)
    return render(request, "admin/employee/update_salary.html", {'employee': employee})

def Employee_salary_update_status_Function(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        division_id = request.POST.get('division_id')

        ccode, cname = map(str.strip, client_name.split('-'))
        
        client = get_object_or_404(Clientmst, ccode=ccode)
        division = get_object_or_404(Divisionmst, did=division_id)
        
      

        employees = Employeesalaryupdate.objects.filter(
            empid__cid=client,
            empid__did=division
        )

        context = {
            "employees" : employees
        }
        return render(request , "admin/employee/salary_update_status.html" , context)
    return render(request , "admin/employee/salary_update_status.html")

def Employee_salary_Approval_Function(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        division_id = request.POST.get('division_id')
        
        ccode, cname = map(str.strip, client_name.split('-'))
        
        client = get_object_or_404(Clientmst, ccode=ccode)
        division = get_object_or_404(Divisionmst, did=division_id)

        employees = Employeesalaryupdate.objects.filter(
            empid__cid=client,
            empid__did=division,
            status=0
        )

        context = {
            "employees" : employees
        }
        return render(request , "admin/employee/salary_approval.html" , context)
    return render(request , "admin/employee/salary_approval.html" )

def approve_salary(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        try:
            update_salary = Employeesalaryupdate.objects.get(pk=record_id)
            update_salary.status = 2
            update_salary.auserid = request.user.username 
            update_salary.adate = timezone.now()
            update_salary.save()
            
            
            employee = update_salary.empid
            employee.basic = update_salary.totalgross
            employee.save()
            
            return JsonResponse({'success': True})
        except Employeesalaryupdate.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})



# # Payroll Module :-
# # ===========================================================================================

from django.db.models import Q
from django.db import transaction

def Add_attendance_function(request):
    if request.method == "POST":
        # Extract client and division data
        
        selected_month = int(request.POST.get("selected_month"))
        selected_year = int(request.POST.get("selected_year"))
        year_month = f"{selected_year}-{selected_month:01}"
        
        
        division_id = request.POST.get('division_id')

        
        division = get_object_or_404(Divisionmst, did=division_id)
        client_id = division.cid.cid
       
        monthdays = {
            1: 31,
            2: 28 if not selected_year % 4 and (selected_year % 100 or not selected_year % 400) else 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }.get(selected_month, 0)

        
        employees = Employeemst.objects.filter(
            Q(cid=client_id) &
            Q(did=division_id) &
            Q(activests=1) &
            ~Q(empattendancedtl__yearmonth=year_month)
        ).distinct()
        
        if not employees:
            messages.error(request, "No employees found for attendance. Attendance data already exists." )
            
            return render(request, "admin/payroll/add_emp_attendance.html")
        
        # Create the attendance header
        header = Empattendancehdr.objects.create(
            cid=Clientmst.objects.get(cid=client_id),
            did=Divisionmst.objects.get(did=division_id),
            atnyearmonth=year_month,
            totalemp=len(employees) ,
            monthdays = monthdays , 
            totalapprovattn = len(employees) * monthdays ,
            
            guserid = request.user.username,
            muserid = request.user.username,
            submituserid = request.user.username,
            auserid = request.user.username,
            
        )
        
        for employee in employees:
            Empattendancedtl.objects.create(
                aid=header,
                empid=Employeemst.objects.get(empid=employee.empid),
                yearmonth=f"{selected_year}-{selected_month:01}",
                totaldays=monthdays,
                present=monthdays,
                woff=0,
                hday=0,
                cl=0,
                el=0,
                ml=0,
                lpdays=0,
                tsalarydays=monthdays,
            )
        unique_year_months = Empattendancehdr.objects.values('atnyearmonth').distinct()
        years = {ym['atnyearmonth'][:4] for ym in unique_year_months}
        sorted_years = sorted(years, reverse=True)
        context = {
        "years": sorted_years,
        "employees": employees,
        }
        
        messages.success(request, "Attendance data has been successfully saved.")
        return render(request, "admin/payroll/add_emp_attendance.html", context)
    
    unique_year_months = Empattendancehdr.objects.values('atnyearmonth').distinct()
    years = {ym['atnyearmonth'][:4] for ym in unique_year_months}
    sorted_years = sorted(years, reverse=True)

    context = {
        "years": sorted_years,
    }

    return render(request, "admin/payroll/add_emp_attendance.html", context)


def Save_attendance_function(request):
    pass

def Edit_attendance_function(request):
    
    if request.method == "POST":

        division_id = request.POST.get('division_id')

        
        division = get_object_or_404(Divisionmst, did=division_id)
        client_id = division.cid.cid
       
        
        # Retrieve Empattendancehdr records based on client_id and division_id
        attendance_records = Empattendancehdr.objects.filter(cid=client_id, did=division_id).order_by("-aid")
        
        # Pass the attendance_records, client_name, and division_name as context data
        context = {
            'attendance_records': attendance_records,
            'client_name': division.cid.cname,
            'division_name': division.division,
        }
        
        return render(request, "admin/payroll/edit_emp_attendance.html", context)

    return render(request, "admin/payroll/edit_emp_attendance.html")

def view_attendance(request, header_id):
    # Retrieve the Empattendancehdr record based on the header_id
    header_record = Empattendancehdr.objects.get(pk=header_id)

    # Retrieve Empattendancedtl records for the selected header
    attendance_details = Empattendancedtl.objects.filter(aid=header_record)

    context = {
        'header_record': header_record,
        'attendance_details': attendance_details,
    }

    return render(request, 'admin/payroll/view_attendance.html', context)

def Approve_attendance_function(request):
    selected_month = request.GET.get('selected_month', '')
    selected_year = request.GET.get('selected_year', '')

    
    approved_count = 2
    
    if request.method == 'POST':
        division_id = request.POST.get('division_id')
        division = get_object_or_404(Divisionmst, did=division_id)
        
        
        attendance_records = Empattendancehdr.objects.filter(
            did = division.did ,
            cid = division.cid.cid ,
            submitsts=1
        )
        
        unique_year_months = Empattendancehdr.objects.values('atnyearmonth').distinct()

        years = {ym['atnyearmonth'][:4] for ym in unique_year_months}
        sorted_years = sorted(years, reverse=True)

        context = {
            'attendance_records': attendance_records,
            'approved_count': approved_count,
            "years" : sorted_years , 
        }
        
        
        
        return render(request, "admin/payroll/approve_emp_attendance.html", context)
        
      
    if selected_month and selected_year:
        yearmonth_filter = f"{selected_year}-{selected_month:01}"
        attendance_records = Empattendancehdr.objects.filter(atnyearmonth=yearmonth_filter, submitsts=1)
        
        pending_count =Empattendancehdr.objects.filter(atnyearmonth=yearmonth_filter, approvstatus=0).count()
        approved_count =Empattendancehdr.objects.filter(atnyearmonth=yearmonth_filter, approvstatus=1).count()
        total_clients = Empattendancehdr.objects.values('cid').count()
        
        unique_year_months = Empattendancehdr.objects.values('atnyearmonth').distinct()

        years = {ym['atnyearmonth'][:4] for ym in unique_year_months}
        sorted_years = sorted(years, reverse=True)
    
        
        context = {
            'attendance_records': attendance_records,
            'approved_count': approved_count,
            'pending_count': pending_count,
            'total_clients': total_clients,
            "years" : sorted_years , 
        }
        
        
        
        return render(request, "admin/payroll/approve_emp_attendance.html", context)
    
    unique_year_months = Empattendancehdr.objects.values('atnyearmonth').distinct()

    years = {ym['atnyearmonth'][:4] for ym in unique_year_months}
    sorted_years = sorted(years, reverse=True)
    
    context = { 
        "years" : sorted_years , 
    }
    return render(request, "admin/payroll/approve_emp_attendance.html" , context)

def view_attendance_employee(request):
    return render(request , "admin/payroll/view_emp_attendance.html")

def submit_attendance(request):
    # Check if it's a POST request
    if request.method == "POST":
        record_id = request.POST.get('record_id')
        try:
            header = Empattendancehdr.objects.get(pk=record_id)
            header.submitsts = 1  # Set submitsts to 1 (or your desired value)
            header.save()
            return JsonResponse({'success': True, 'message': 'Attendance submitted successfully'})
        except Empattendancehdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Header not found'})
    
    # If it's not a POST request, return an error response
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})

def approve_attendance(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        try:
            attendance_record = Empattendancehdr.objects.get(pk=record_id)
            attendance_record.approvstatus = 1
            attendance_record.save()
            return JsonResponse({'success': True})
        except Empattendancehdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})

def reject_attendance(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        try:
            attendance_record = Empattendancehdr.objects.get(pk=record_id)
            attendance_record.approvstatus = 0
            attendance_record.save()
            return JsonResponse({'success': True})
        except Empattendancehdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})

def return_attendance(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        try:
            attendance_record = Empattendancehdr.objects.get(pk=record_id)
            attendance_record.submitsts = 0
            attendance_record.approvstatus = 0
            attendance_record.save()
            return JsonResponse({'success': True})
        except Empattendancehdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})

def delete_attendance(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        print(record_id)
        try:
            attendance_record = get_object_or_404(Empattendancehdr, pk=record_id)
            attendance_record.delete()
            return JsonResponse({'success': True})
        except Empattendancehdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})



def Add_salary_function(request):
    if request.method == "POST":
        
        selected_month = int(request.POST.get("selected_month"))
        selected_year = int(request.POST.get("selected_year"))
        year_month = f"{selected_year}-{selected_month:01}"
        
        division_id = request.POST.get('division_id')

        division = get_object_or_404(Divisionmst, did=division_id)
        client_id = division.cid.cid
       
        monthdays = {
            1: 31,
            2: 28 if not selected_year % 4 and (selected_year % 100 or not selected_year % 400) else 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }.get(selected_month, 0)

        existing_salary_hdr = Empsalaryhdr.objects.filter(
            cid = division.cid ,
            did=division,
            attnyearmonth=year_month,
        ).first()
        
        attendance_header = Empattendancehdr.objects.filter(
            cid=client_id ,
            did=division_id,
            atnyearmonth=year_month,
            approvstatus=1
        ).first()
        
        
        if existing_salary_hdr:
            messages.error(request , f"Salary Already Processed")
            
        
        elif not attendance_header:
            messages.error(request , f"Attendance for the selected year-month and division is not approved.") 
        
        
        else:
            with transaction.atomic():
                salary_header = Empsalaryhdr.objects.create(
                    cid = division.cid ,
                    did=division,
                    aid=attendance_header,
                    attnyearmonth=year_month,
                    totalemp = attendance_header.totalemp,
                    guserid=request.user.username,
                    
                )
                total_salary = 0
                
                for emp_detail in Empattendancedtl.objects.filter(aid=attendance_header):
                    
                    
                    calculatedattndays=emp_detail.present
                    calcumatedwagestype= int(emp_detail.empid.wagestype)
                    
                    print(calcumatedwagestype)
                    
                    if emp_detail.empid.wagestype == 1:
                        calculateddailywages = emp_detail.empid.basic
                    else:
                        calculateddailywages = emp_detail.empid.basic / emp_detail.present

                    calculatedbasic = emp_detail.empid.basic
                    
                    calculatedepf = calculatedbasic * .12
                    calculatedesi = calculatedbasic * .0075
                    
                    calculatedemprepf = calculatedbasic * .13
                    calculatedempresi = calculatedbasic * .0325
                    
                    claculatedgross = calculatedattndays * calculateddailywages
                    
                    calculatedatnwages = calculateddailywages * calculatedattndays
                    
                    
                    Empsalarydtl.objects.create(
                        sid=salary_header,
                        empid=emp_detail.empid,
                        
                        yearmonth=year_month,                
                        attndays=calculatedattndays,
                        wagestype=calcumatedwagestype,  
                        
                        basic=calculatedbasic,
                        dailywages = calculateddailywages ,
                        atnwages = calculatedatnwages ,
                        
                        bonus = 0,
                        insentive = 0 ,
                        ot = 0,
                        arrear = 0,
                        
                        epf = calculatedepf ,
                        esi = calculatedesi ,
                        emprepf = calculatedemprepf ,
                        empresi = calculatedempresi ,
                        
                        ptax = 0 ,
                        advance = 0 ,
                        uniform = 0 ,
                        others = 0,
                        loans = 0 ,
                        sewacharge = 32 ,
                        
                        gross = claculatedgross ,
                        netpay = claculatedgross -  (calculatedepf + calculatedesi + 32 ), 
                        
                        
                        processuserid=request.user.username,
                        processstatus = 1 ,
                    )
                    
                    total_salary += claculatedgross
                    
                salary_header.totalsalary = total_salary
                salary_header.save()    
                
                messages.error(request , f"Salary processing completed successfully.")

    return render(request, "admin/payroll/salary/add_emp_salary.html")


def edit_salary_function(request):
    if request.method == "POST":
        
        division_id = request.POST.get('division_id')

        division = get_object_or_404(Divisionmst, did=division_id)
        client_id = division.cid.cid
        
        salary_records = Empsalaryhdr.objects.filter(cid=client_id, did=division_id).order_by("-aid")
        
        context = {
            "salary_records" : salary_records
        } 
        return render(request ,"admin/payroll/salary/edit_emp_salary.html" , context)
    return render(request ,"admin/payroll/salary/edit_emp_salary.html" )

def view_salary(request, header_id):
    
    header_record = Empsalaryhdr.objects.get(pk=header_id)

    salary_details = Empsalarydtl.objects.filter(sid=header_record)

    context = {
        'header_record': header_record,
        'salary_details': salary_details,
    }

    return render(request, 'admin/payroll/salary/view_salary.html', context)

def submit_salary(request):
    # Check if it's a POST request
    if request.method == "POST":
        record_id = request.POST.get('record_id')
        try:
            header = Empsalaryhdr.objects.get(pk=record_id)
            header.submitsts=1 
            header.submitdate=timezone.now()
            header.submituserid=request.user.username
            header.save()
            
            return JsonResponse({'success': True, 'message': 'Salary submitted successfully'})
        except Empsalaryhdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Header not found'})
    
    # If it's not a POST request, return an error response
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})

def delete_salary(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        print(record_id)
        try:
            salary_record = get_object_or_404(Empsalaryhdr, pk=record_id)
            
            # Retrieve and delete related records in Empsalarydtl
            related_records = salary_record.empsalarydtl_set.all()
            related_records.delete()

            # Delete the Empsalaryhdr record
            salary_record.delete()

            return JsonResponse({'success': True})
        except Empsalaryhdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})


def Approve_salary_function(request):
    selected_month = request.GET.get('selected_month', '')
    selected_year = request.GET.get('selected_year', '')

    
    approved_count = 2
    
    if request.method == 'POST':
        division_id = request.POST.get('division_id')
        division = get_object_or_404(Divisionmst, did=division_id)
        
        
        attendance_records = Empsalaryhdr.objects.filter(
            did = division.did ,
            cid = division.cid.cid ,
            submitsts=1
        )
        
        unique_year_months = Empsalaryhdr.objects.values('attnyearmonth').distinct()

        years = {ym['attnyearmonth'][:4] for ym in unique_year_months}
        sorted_years = sorted(years, reverse=True)

        context = {
            'attendance_records': attendance_records,
            'approved_count': approved_count,
            "years" : sorted_years , 
        }
        
        
        
        return render(request, "admin/payroll/salary/approve_emp_salary.html", context)
        
      
    if selected_month and selected_year:
        yearmonth_filter = f"{selected_year}-{selected_month:01}"
        
        attendance_records = Empsalaryhdr.objects.filter(attnyearmonth=yearmonth_filter, submitsts=1)
        
        pending_count =Empsalaryhdr.objects.filter(attnyearmonth=yearmonth_filter, approvstatus=0).count()
        approved_count =Empsalaryhdr.objects.filter(attnyearmonth=yearmonth_filter, approvstatus=1).count()
        total_clients = Empsalaryhdr.objects.values('cid').count()
        
        unique_year_months = Empsalaryhdr.objects.values('attnyearmonth').distinct()

        years = {ym['attnyearmonth'][:4] for ym in unique_year_months}
        sorted_years = sorted(years, reverse=True)
    
        
        context = {
            'attendance_records': attendance_records,
            'approved_count': approved_count,
            'pending_count': pending_count,
            'total_clients': total_clients,
            "years" : sorted_years , 
        }
        
        
        
        return render(request, "admin/payroll/salary/approve_emp_salary.html", context)
    
    unique_year_months = Empsalaryhdr.objects.values('attnyearmonth').distinct()

    years = {ym['attnyearmonth'][:4] for ym in unique_year_months}
    sorted_years = sorted(years, reverse=True)
    
    context = { 
        "years" : sorted_years , 
    }
    return render(request, "admin/payroll/salary/approve_emp_salary.html", context)


def approve_salary(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        try:
            salary_record = Empsalaryhdr.objects.get(pk=record_id)
            salary_record.approvstatus = 1
            salary_record.approvuserid = request.user.username
            salary_record.approvdate = timezone.now()
            salary_record.save()
            return JsonResponse({'success': True})
        except Empsalaryhdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})


def reject_salary(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        try:
            salary_record = Empsalaryhdr.objects.get(pk=record_id)
            salary_record.approvstatus = 0
            salary_record.approvuserid = None
            salary_record.approvdate = None
            
            salary_record.save()
            return JsonResponse({'success': True})
        except Empsalaryhdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})


def return_salary(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        try:
            salary_record = Empsalaryhdr.objects.get(pk=record_id)
            salary_record.submitsts = 0
            salary_record.approvstatus = 0
            
            salary_record.save()
            return JsonResponse({'success': True})
        except Empsalaryhdr.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Record not found'})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})



# # Verify Module 
# # ===========================================================================================
from .models import Empepfhdr , Empesihdr , Empsalaryhdr
def salary_Function(request):
    selected_month = request.GET.get('selected_month')
    selected_year = request.GET.get('selected_year')
    
    if selected_month and selected_year:
        yearmonth_filter = f"{selected_year}-{selected_month:01}"
        print(yearmonth_filter)  # Format: 'YYYY-MM'
        epfs = Empsalaryhdr.objects.filter(yearmonth=yearmonth_filter)
    else:
        epfs = Empsalaryhdr.objects.all()
        
    # Count the number of successfully payments (submitpaysts=1) and not payments (submitpaysts=0)
    successfully_payment = epfs.filter(submitpaysts=1).count()
    not_payment = epfs.filter(submitpaysts=0).count()
    
    context = {
        "epfs": epfs,
        "selected_month": selected_month,
        "selected_year": selected_year,
        "successfully_payment": successfully_payment,
        "not_payment": not_payment,
    }
    return render(request , "admin/verify/salary.html")

from .models import Empepfhdr , Empesihdr , Empsalaryhdr
def epf_Function(request):
    
    selected_month = request.GET.get('selected_month')
    selected_year = request.GET.get('selected_year')
    
    if selected_month and selected_year:
        yearmonth_filter = f"{selected_year}-{selected_month:01}"
        print(yearmonth_filter)  # Format: 'YYYY-MM'
        epfs = Empepfhdr.objects.filter(yearmonth=yearmonth_filter)
    else:
        epfs = Empepfhdr.objects.all()
        
    # Count the number of successfully payments (submitpaysts=1) and not payments (submitpaysts=0)
    successfully_payment = epfs.filter(submitpaysts=1).count()
    not_payment = epfs.filter(submitpaysts=0).count()
    
    context = {
        "epfs": epfs,
        "selected_month": selected_month,
        "selected_year": selected_year,
        "successfully_payment": successfully_payment,
        "not_payment": not_payment,
    }
    return render(request , "admin/verify/epf.html" , context)



def esi_Function(request):
    selected_month = request.GET.get('selected_month')
    selected_year = request.GET.get('selected_year')
    
    if selected_month and selected_year:
        yearmonth_filter = f"{selected_year}-{selected_month:01}"
        print(yearmonth_filter)  # Format: 'YYYY-MM'
        esis = Empesihdr.objects.filter(yearmonth=yearmonth_filter)
    else:
        esis = Empesihdr.objects.all()
        
    # Count the number of successfully payments (submitpaysts=1) and not payments (submitpaysts=0)
    successfully_payment = esis.filter(submitpaysts=1).count()
    not_payment = esis.filter(submitpaysts=0).count()
    
    context = {
        "esis": esis,
        "selected_month": selected_month,
        "selected_year": selected_year,
        "successfully_payment": successfully_payment,
        "not_payment": not_payment,
    }
    return render(request , "admin/verify/esi.html" , context)

# # Payment Module 
# # ===========================================================================================

def approved_salary_payment(request):
    return render(request , "admin/payment/approved_salary_payment.html")

def approved_esi_deposite(request):
    return render(request , "admin/payment/approved_esi_deposite.html")

def approved_epf_deposite(request):
    return render(request , "admin/payment/approved_epf_deposite.html")


# # Bill Module 
# # ===========================================================================================

from .models import Billhdr , Billdtl , Clientbillreceive
def bill_entry(request):
    bill = Billdtl.objects.all()
    context={
        "bill" : bill
    }
    return render(request , "admin/bill/view_bill.html" , context)

def add_new_bill(request):
    return render(request , "admin/bill/add_new_bill.html")

def view_bill(request):
    return render(request , "admin/bill/view_bill.html")


def bill_receive(request):
    bill_receives = Clientbillreceive.objects.select_related('bid__cid', 'did').all()
    context={
        "bill_receives" : bill_receives
    }
    return render(request , "admin/bill/view_bill_receive_details.html" , context)

def add_bill_receive_details(request):
    return render(request , "admin/bill/add_bill_receive_details.html")

from .models import Clientexpenditure
def client_expenditure(request):
    client_expenditures = Clientexpenditure.objects.all()
    context = {
        "client_expenditures" : client_expenditures
    }
    return render(request , "admin/bill/view_expenditure_details.html" , context)

def add_expenditure(request):
    return render(request , "admin/bill/add_expenditure.html")

def view_expenditure_details(request):
    return render(request , "admin/bill/view_expenditure_details.html")


def generate_bill(request):
    return render(request , "admin/bill/generate_new_bill.html")

def view_generate_bill(request):
    return render(request , "admin/bill/view_generate_bill.html")

def generate_new_bill(request):
    return render(request , "admin/bill/generate_new_bill.html")

def proforma_bill(request):
    return render(request , "admin/bill/add_proforma_bill_invoice.html")

def add_proforma_bill_invoice(request):
    return render(request , "admin/bill/add_proforma_bill_invoice.html")




def view_proforma_bill_invoice(request):
    x = "fnbfgnfgngfn"
    return render(request , "admin/bill/view_proforma_bill_invoice.html" , {"x" : x})



def bill_approval(request):
    if request.method == 'GET':
        
        client_name = request.GET.get('client_name')
        division_name = request.GET.get('division_name')
        
        selected_month = request.GET.get('selected_month')
        selected_year = request.GET.get('selected_year')
        
        bill_no = request.GET.get('bill_no')

        if selected_month is not None and selected_year is not None:
            # Construct the yearmonth string in the format "YYYY-MM"
            year_month_str = f"{selected_year}-{selected_month:01}"
            
            yEARbills = Billhdr.objects.filter(
                yearmonth=year_month_str,
                approve=1
            )
            if not yEARbills:
                messages.info(request, 'No results found.')
            return render(request, "admin/bill/bill_approval.html", {'yEARbills': yEARbills})

        
            
        bills = Billhdr.objects.filter(
            cid__cname=client_name,
            did__division=division_name,
            approve=1
        )
        
        if bill_no is not None:
            billsNo = Billhdr.objects.filter(billno__icontains=bill_no, approve=1)
            if not billsNo:
                messages.info(request, 'No results found.')
            return render(request, "admin/bill/bill_approval.html", {'billsNo': billsNo})
            
        
        if not bills:
            messages.info(request, 'No results found.')
        
        context = {
            'bills': bills ,
            
        }
        return render(request , "admin/bill/bill_approval.html" , context)
    return render(request , "admin/bill/bill_approval.html")


from django.http import JsonResponse
from .models import Billhdr

def searchclienTdivisioN_bills(request):
    client_name = request.POST.get('client_name')
    division_name = request.POST.get('division_name')
    
   
    

    # Filter bills based on the search criteria and where approve is 1
    bills = Billhdr.objects.filter(
        cid__cname=client_name,
        did__division=division_name,
        approve=1
    )

    # Serialize the filtered data to JSON
    bill_data = []
    for bill in bills:
        bill_data.append({
            'client_name': bill.cid.cname,
            'division_name': bill.did.division,
            'year_month': bill.yearmonth,
            'bill_date': bill.billdate.strftime('%Y-%m-%d'),
            'bill_no': bill.billno,
            'total_bill': bill.totalbill,
            'gst': bill.gst
        })
        
    queryset = Billhdr.objects.filter(
    cid__ccode=client_name,
    did__division=division_name,
    approve=1
    )
    print(queryset.query)

    return JsonResponse({'bills': bill_data})


def bill_disapproval(request):
    if request.method == 'GET':
        
        client_name = request.GET.get('client_name')
        division_name = request.GET.get('division_name')
        
        selected_month = request.GET.get('selected_month')
        selected_year = request.GET.get('selected_year')
        
        bill_no = request.GET.get('bill_no')

        if selected_month is not None and selected_year is not None:
            # Construct the yearmonth string in the format "YYYY-MM"
            year_month_str = f"{selected_year}-{selected_month:01}"
            
            yEARbills = Billhdr.objects.filter(
                yearmonth=year_month_str,
                approve=0
            )
            if not yEARbills:
                messages.info(request, 'No results found.')
            return render(request, "admin/bill/bill_disapproval.html", {'yEARbills': yEARbills})

        
            
        bills = Billhdr.objects.filter(
            cid__cname=client_name,
            did__division=division_name,
            approve=0
        )
        
        if bill_no is not None:
            billsNo = Billhdr.objects.filter(billno__icontains=bill_no, approve=0)
            if not billsNo:
                messages.info(request, 'No results found.')
            return render(request, "admin/bill/bill_disapproval.html", {'billsNo': billsNo})
            
        
        if not bills:
            messages.info(request, 'No results found.')
        
        context = {
            'bills': bills ,
            
        }
    return render(request , "admin/bill/bill_disapproval.html" , context)


from datetime import datetime
from django.shortcuts import render
from .models import Billhdr

def gst_bill_prepare(request):
    if request.method == 'GET':
        from_date_str = request.GET.get('from_date')
        to_date_str = request.GET.get('to_date')

        # Check if both from_date and to_date are provided and not None
        if from_date_str is not None and to_date_str is not None:
            try:
                from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
                to_date = datetime.strptime(to_date_str, '%Y-%m-%d')

                # Additional validation: Check if from_date is not greater than to_date
                if from_date > to_date:
                    return render(request, "admin/bill/gst_bill_prepare.html", {'error_message': "From date cannot be greater than to date"})

            except ValueError:
                return render(request, "admin/bill/gst_bill_prepare.html", {'error_message': "Invalid date format"})

            bills = Billhdr.objects.filter(billdate__range=(from_date, to_date), approve=True)

            # Check if there are no results and provide feedback
            if not bills:
                return render(request, "admin/bill/gst_bill_prepare.html", {'error_message': "No bills found for the specified date range"})

            return render(request, "admin/bill/gst_bill_prepare.html", {'bills': bills})
        
        else:
            # Handle the case when either from_date or to_date is None
            return render(request, "admin/bill/gst_bill_prepare.html", {'error_message': "Please provide both from_date and to_date"})

    return render(request, "admin/bill/gst_bill_prepare.html")

def gst_bill_pending(request):
    return render(request , "admin/bill/gst_bill_pending.html")


# # Bill Report Module 
# # ===========================================================================================

def bill_submitted(request):
    
    bill_data = Billdtl.objects.all()
    context = {'bill_data': bill_data}
    return render(request , "admin/bill_report/bill_submitted.html" , context)

def bill_received(request):
    bill_data = Clientbillreceive.objects.all()
    context = {'bill_data': bill_data}
    return render(request , "admin/bill_report/bill_received.html", context)

from django.db.models import Count
def expenditure_report(request):
    expenditure_reports = Clientexpenditure.objects.all()
    data = [
        {
            
            "CLIENT_NAME": report.cid.cname,
            "DIVISION": report.did.division,
            "MONTH": datetime.strptime(report.yearmonth, '%Y-%m').strftime('%B'),  
            "YEAR": datetime.strptime(report.yearmonth, '%Y-%m').strftime('%Y'), 
            "MATERIAL": report.materialexpr,
            "FUEL": report.fuleexpr,
            "OPERATIONAL": report.adminexpr,
            "OTHERS": report.otherexpr,
            "TOUR_TRAVEL": report.travelexpr,
        }
        for report in expenditure_reports
    ]
    
    distinct_months = set(datetime.strptime(report.yearmonth, '%Y-%m').strftime('%B') for report in expenditure_reports)
    distinct_years = set(datetime.strptime(report.yearmonth, '%Y-%m').strftime('%Y') for report in expenditure_reports)

    context = {
        "expenditure_reports": data,  
        "distinct_years": distinct_years,
        "distinct_months": distinct_months,
    }
    return render(request , "admin/bill_report/expenditure_report.html" , context)



def bill_outstanding(request):
    
    bill_outstandings = Clientbillreceive.objects.all()
    
    context = {
        "bill_outstandings": bill_outstandings, 
    }
    return render(request , "admin/bill_report/bill_outstanding.html" , context)

def client_profit_loss_statement(request):
    return render(request , "admin/bill_report/client_profit_loss_statement.html")

def gst_received_reports(request):
    gst_received = Clientbillreceive.objects.all()
    
    context = {
        "gst_received": gst_received, 
    }
    return render(request , "admin/bill_report/gst_received_reports.html" , context)

def tds_reports(request):
    tds_reports = Clientbillreceive.objects.all()
    
    context = {
        "tds_reports": tds_reports, 
    }
    return render(request , "admin/bill_report/tds_reports.html" , context)

def date_wise_bill_received(request):
    daywise_bills = Clientbillreceive.objects.all()
    
    context = {
        "daywise_bills": daywise_bills, 
    }
    return render(request , "admin/bill_report/date_wise_bill_received.html" , context)

from .models import Clientbillmst
def month_wise_bill_register(request):
    mothwise_bills = Clientbillmst.objects.all()
    context = {
        "mothwise_bills": mothwise_bills, 
    }
    return render(request , "admin/bill_report/month_wise_bill_register.html" , context)

def payment_not_received(request):
    bill_outstandings = Clientbillreceive.objects.filter(recvamount=0)
    
    context = {
        "bill_outstandings": bill_outstandings, 
    }
    return render(request , "admin/bill_report/payment_not_received.html" , context)

def bill_not_despatched(request):
    return render(request , "admin/bill_report/bill_not_despatched.html")

def date_wise_bill_submited(request):
    return render(request , "admin/bill_report/date_wise_bill_submited.html")

# # Tender Module 
# # ===========================================================================================

from .models import Tenders , Tenderdocument , Companydocuments

def company_essential_documents(request):
    documents = Companydocuments.objects.all().order_by('-docid')
    context = {
        "documents" : documents
    }
    return render(request , "admin/tender/company_essential_documents.html" , context)

from django.core.files.storage import default_storage
def add_new_document(request):
    if request.method == 'POST':
        document_name = request.POST.get('document_name')
        registration_date = request.POST.get('registration_date')
        expired_date = request.POST.get('expired_date')

        unsign_file = request.FILES.get('unsign_file')
        sign_file = request.FILES.get('sign_file')

        # Save files to the server
        unsign_file_path = default_storage.save('uploads/' + unsign_file.name, unsign_file)
        sign_file_path = default_storage.save('uploads/' + sign_file.name, sign_file)

        # Create a new Companydocuments instance
        document = Companydocuments(
            docname=document_name,
            docregdt=registration_date,
            docexpirdt=expired_date,
            unsignpath=unsign_file_path,
            signpath=sign_file_path,
            status=1,  # Set the appropriate status value
            cuserid=request.user.username,  # Assuming you have a user system
        )

        document.save()

        response_data = {'success': True, 'message': 'Document added successfully!'}
        return JsonResponse(response_data)
    return render(request , "admin/tender/add_new_document.html")


def tenders(request):
    tenders = Tenders.objects.all()
    context = {
        "tenders" : tenders
    }
    return render(request , "admin/tender/tenders.html" , context)


def add_new_tender(request):
    if request.method == 'POST':
        tender_name = request.POST.get('tender_name')
        tender_type = request.POST.get('tender_type')
        publish_date = request.POST.get('publish_date')
        expiry_date = request.POST.get('expiry_date')
        category = request.POST.get('category')
        strength = request.POST.get('Strength')
        contract_value = request.POST.get('ContractValue')
        contract_period = request.POST.get('ContractPeriod')
        website_name = request.POST.get('WebSite')
        pre_bid_meet = request.POST.get('PreBidMeet')
        submission_last_date = request.POST.get('SubLastDt')
        mode_submission = request.POST.get('ModeSub')
        technical_bid_open = request.POST.get('TechBidOpen')
        financial_bid_open = request.POST.get('FinBibOpen')
        paper_cost = request.POST.get('PaperCost')
        emd = request.POST.get('EMD')
        
        prepare_user_id = request.POST.get('PUserId')
        monitor_user_id = request.POST.get('MUserId')
        
        adv_doc = request.FILES.get('adv_doc')
        adv_doc_path = default_storage.save('uploads/' + adv_doc.name, adv_doc)
        
        # Save the tender data
        tender = Tenders(
            tendername=tender_name,
            tendertype=tender_type,
            publishdate=publish_date,
            expiredate=expiry_date,
            category=category,
            strength=strength,
            contractvalue=contract_value,
            contractperiod=contract_period,
            websitename=website_name,
            pribidmeet=pre_bid_meet,
            lsubmisiondate=submission_last_date,
            modesubmision=mode_submission,
            techinecalbidopen=technical_bid_open,
            financialbidopen=financial_bid_open,
            papercost=paper_cost,
            emd=emd,
            prepareuserid=prepare_user_id,
            moniteruserid=monitor_user_id,
            cuserid=request.user.username,
            advdocpath=adv_doc_path
        )

        tender.save()

        response_data = {'success': True, 'message': 'Tender added successfully!'}
        return JsonResponse(response_data)
    users = User.objects.all()
    
    context = {
        "users" : users
    }
    return render(request , "admin/tender/add_new_tender.html" , context)


def tender_prepration(request):
    tenders = Tenders.objects.all().order_by('-tid')
    context = {
        "tenders" : tenders
    }
    return render(request , "admin/tender/tender_prepration.html", context)

def tender_financial_bid(request):
    tenders = Tenders.objects.all().order_by('-tid')
    context = {
        "tenders" : tenders
    }
    return render(request , "admin/tender/tender_financial_bid.html" , context)

def add_financial_bid_details(request):
    if request.method == "POST":
        tender_id = request.POST.get('tender_id')
        finbidtype = request.POST.get('finbidtype')
        finbidremark = request.POST.get('finbidremark')
        
        docpath = request.FILES.get('docpath')
        
        tender = get_object_or_404(Tenders , pk = tender_id)
        docpath_file_path = default_storage.save('uploads/' + docpath.name, docpath)
        Tenderfinbiddoc.objects.create(
            tid = tender ,
            finbidtype = finbidtype ,
            finbidremark = finbidremark ,
            docpath = docpath_file_path ,
            cuserid = request.user.username
        )
        response_data = {'success': True, 'message': 'Financial Bid Details added successfully!'}
        return JsonResponse(response_data)
    

def view_tender_financial_bid(request):
    return render(request , "admin/tender/view_tender_financial_bid.html")

def tender_status_upload(request):
    tenders = Tenders.objects.all().order_by('-tid')
    context = {
        "tenders" : tenders
    }
    return render(request , "admin/tender/tender_status_upload.html",context )

def view_tender_status_upload(request):
    return render(request , "admin/tender/view_tender_status_upload.html")

def add_status_details(request):
    if request.method == "POST":
        tender_id = request.POST.get('tender_id')
        statustype = request.POST.get('statustype')
        statusremark = request.POST.get('statusremark')
        
        docpath = request.FILES.get('docpath')
        
        tender = get_object_or_404(Tenders , pk = tender_id)
        docpath_file_path = default_storage.save('uploads/' + docpath.name, docpath)
        Tenderstatusdoc.objects.create(
            tid = tender ,
            statustype = statustype ,
            statusremark = statusremark ,
            docpath = docpath_file_path ,
            cuserid = request.user.username
        )
        response_data = {'success': True, 'message': 'Financial Bid Details added successfully!'}
        return JsonResponse(response_data)


from django.shortcuts import render
from django.db.models import Q
from .models import Tenders

from django.shortcuts import render
from django.db.models import Q
from .models import Tenders
from datetime import datetime

def tender_submited(request):
    if request.method == 'GET':
        selected_start_date = request.GET.get('selected_start_date')
        selected_end_date = request.GET.get('selected_end_date')

        # Check if both start and end dates are selected
        if selected_start_date and selected_end_date:
            try:
                start_date = datetime.strptime(selected_start_date, "%Y-%m-%d")
                end_date = datetime.strptime(selected_end_date, "%Y-%m-%d")
                
                # Assuming submitdt is a DateTimeField, filter based on the date range
                tenders = Tenders.objects.filter(
                    Q(submitdt__gte=start_date) &
                    Q(submitdt__lte=end_date),
                    submitsts=1
                )

                return render(request, "admin/tender/tender_submited.html", {'tenders': tenders})
            except ValueError:
                # Handle the case where the date string is not in the expected format
                # You can add a message or log the error for debugging
                pass

    return render(request, "admin/tender/tender_submited.html")





def tender_not_submited(request):
    if request.method == 'GET':
        selected_start_date = request.GET.get('selected_start_date')
        selected_end_date = request.GET.get('selected_end_date')

        # Check if both start and end dates are selected
        if selected_start_date and selected_end_date:
            try:
                start_date = datetime.strptime(selected_start_date, "%Y-%m-%d")
                end_date = datetime.strptime(selected_end_date, "%Y-%m-%d")
                
                # Assuming submitdt is a DateTimeField, filter based on the date range
                tenders = Tenders.objects.filter(
                    Q(expiredate__gte=start_date) &
                    Q(expiredate__lte=end_date),
                    submitsts=0
                )

                return render(request, "admin/tender/tender_not_submited.html", {'tenders': tenders})
            except ValueError:
                # Handle the case where the date string is not in the expected format
                # You can add a message or log the error for debugging
                pass
    return render(request , "admin/tender/tender_not_submited.html")

def tender_expired(request):
    if request.method == 'GET':
        selected_start_date = request.GET.get('selected_start_date')
        selected_end_date = request.GET.get('selected_end_date')

        # Check if both start and end dates are selected
        if selected_start_date and selected_end_date:
            try:
                start_date = datetime.strptime(selected_start_date, "%Y-%m-%d")
                end_date = datetime.strptime(selected_end_date, "%Y-%m-%d")
                
                # Assuming submitdt is a DateTimeField, filter based on the date range
                tenders = Tenders.objects.filter(
                    Q(expiredate__gte=start_date) &
                    Q(expiredate__lte=end_date)
                )

                return render(request, "admin/tender/tender_not_submited.html", {'tenders': tenders})
            except ValueError:
                # Handle the case where the date string is not in the expected format
                # You can add a message or log the error for debugging
                pass
    return render(request , "admin/tender/tender_expired.html"  )


# # users Module 
# # ===========================================================================================

def create_users(request):
    return render(request , "admin/users/create_users.html")
def add_new_user(request):
    return render(request , "admin/users/add_new_user.html")
def asigned_client(request):
    return render(request , "admin/users/asigned_client.html")


def menu_access(request):
    return render(request , "admin/users/menu_access.html")

def user_status_review(request):
    return render(request , "admin/users/user_status_review.html")

def branch_status_review(request):
    return render(request , "admin/users/branch_status_review.html")

def monthly_status_review(request):
    return render(request , "admin/users/monthly_status_review.html")






# Reports Module :-

def client_reports(request):
    return render(request , "admin/reports/clientListreports.html")

def employees_reports(request):
    return render(request , "admin/reports/employeeListReports.html")


