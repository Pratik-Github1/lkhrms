from django.db import models
import random


class Clientmst(models.Model):
    cid = models.BigAutoField(db_column='CId', primary_key=True) 
    cname = models.CharField(db_column='CName', max_length=100, blank=True, null=True)  
    ccode = models.CharField(db_column='CCode', max_length=10, blank=True, null=True)  
    
    district = models.CharField(db_column='District', max_length=50, blank=True, null=True)  
    
    csname = models.CharField(db_column='CSName', max_length=50, blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  
    pin = models.CharField(db_column='Pin', max_length=10, blank=True, null=True)  
    oficeph = models.CharField(db_column='OficePh', max_length=15, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  
    contractno = models.CharField(db_column='ContractNo', max_length=20, blank=True, null=True)  
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  
    gstno = models.CharField(db_column='GSTNo', max_length=30, blank=True, null=True)  
    contractvalue = models.FloatField(db_column='ContractValue', blank=True, null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=5, blank=True, null=True)  
    epf = models.CharField(db_column='EPF', max_length=5, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=5, blank=True, null=True)  
    
    contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  
    contactmobileno = models.CharField(db_column='ContactMobileNo', max_length=15, blank=True, null=True)  
    contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True)  
    contactdesg = models.CharField(db_column='ContactDesg', max_length=50, blank=True, null=True)  
    
    userid = models.CharField(db_column='Userid', max_length=30, blank=True, null=True) 
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=30, blank=True, null=True) 
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    
    activests = models.BooleanField(db_column='ActiveSts', blank=True, null=True , default=True)
    udt = models.DateTimeField(auto_now=True, db_column='UDt', blank=True, null=True)  

    def save(self, *args, **kwargs):
        # If the record is being created (not updated) and ccode is not set, generate a new ccode
        if not self.ccode and not self.pk:
            super().save(*args, **kwargs)  # Save the instance to get a valid cid
            self.ccode = f"LK{self.cid:03d}"
            super().save(*args, **kwargs)  # Save again to update ccode
        else:
            super().save(*args, **kwargs)
        
    class Meta:
        db_table = 'clientmst'

class Divisionmst(models.Model):
    did = models.BigAutoField(db_column='DId', primary_key=True) 
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE , db_column='CId', blank=True, null=True) 
    
    division = models.CharField(db_column='Division', max_length=100, blank=True, null=True)
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCode', max_length=20, blank=True, null=True)  
    bankaccno = models.BigIntegerField(db_column='BankAccNO', blank=True, null=True)  
      
    userid = models.CharField(db_column='Userid', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    
     
    activests = models.BooleanField(db_column='ActiveSts', blank=True, null=True , default=True)
    
    udt = models.DateTimeField(auto_now=True, db_column='UDt', blank=True, null=True)    
    
    
    def toggle_status(self):
        self.activests = not self.activests
        self.save()

    class Meta:
        
        db_table = 'divisionmst'

class Clientdivisionestimatebilling(models.Model):
    eid = models.AutoField(primary_key=True, db_column='Eid')
    
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE, db_column='Cid', blank=True, null=True)
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True)
    
    
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)  
    billingwages = models.FloatField(db_column='BillingWages', blank=True, null=True)  
    billingepf = models.FloatField(db_column='BillingEPF', blank=True, null=True)  
    billingesi = models.FloatField(db_column='BillingESI', blank=True, null=True)  
    seviceon = models.IntegerField(db_column='SeviceOn', blank=True, null=True)  
    sevicecharge = models.FloatField(db_column='SeviceCharge', blank=True, null=True)  
    totalsevicecharge = models.FloatField(db_column='TotalSeviceCharge', blank=True, null=True)  
    bonus = models.FloatField(db_column='Bonus', blank=True, null=True)  
    leave = models.FloatField(db_column='Leave', blank=True, null=True)  
    nfholidays = models.FloatField(db_column='NFHolidays', blank=True, null=True)  
    gst = models.FloatField(db_column='GST', blank=True, null=True)  
    
    material = models.FloatField(db_column='Material', blank=True, null=True)  
    fule = models.FloatField(db_column='Fule', blank=True, null=True)  
    machinary = models.FloatField(db_column='Machinary', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    totalgst = models.FloatField(db_column='TotalGST', blank=True, null=True)  
    totalestimate = models.FloatField(db_column='TotalEstimate', blank=True, null=True)  
    gston = models.CharField(db_column='GSTON', max_length=50, blank=True, null=True)  
    
    
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)
 
    muserid = models.CharField(db_column='MUserId', max_length=50, blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=50, blank=True, null=True)  

    class Meta:
        
        db_table = 'clientdivisionestimatebilling'

class Clientdivisionestimatebillingdtl(models.Model):
    edid = models.AutoField(db_column='EDId' , primary_key=True) 
    
    eid = models.ForeignKey(Clientdivisionestimatebilling , on_delete=models.CASCADE, db_column='Eid', blank=True, null=True , default=None) 
    
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE, db_column='Cid', blank=True, null=True)
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True)
    
    category = models.CharField(db_column='Category', max_length=30, blank=True, null=True)  
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)  
    perempwages = models.FloatField(db_column='PerEmpWages', blank=True, null=True)  
    empwages = models.FloatField(db_column='EmpWages', blank=True, null=True)  
    epfwages = models.FloatField(db_column='EPFWages', blank=True, null=True)  
    esiwages = models.FloatField(db_column='ESIWages', blank=True, null=True)  
    epf = models.FloatField(db_column='EPF', blank=True, null=True)  
    esi = models.FloatField(db_column='ESI', blank=True, null=True)  
    epfsts = models.IntegerField(db_column='EpfSts', blank=True, null=True)  
    esists = models.IntegerField(db_column='EsiSts', blank=True, null=True)  
    
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'clientdivisionestimatebillingdtl'

class Employeemst(models.Model):
    empid = models.BigAutoField(db_column='EmpId', primary_key=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=10, blank=True, null=True)  
    empname = models.CharField(db_column='EmpName', max_length=100, blank=True, null=True)  
    empfhname = models.CharField(db_column='EmpFHName', max_length=100, blank=True, null=True)  
    empdob = models.DateTimeField(db_column='EmpDob', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  
    mobileno = models.CharField(db_column='MobileNo', max_length=30, blank=True, null=True)  
    emergencyno = models.CharField(db_column='EmergencyNo', max_length=15, blank=True, null=True)  
    bloodgroup = models.CharField(db_column='BloodGroup', max_length=5, blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=15, blank=True, null=True)  
    joinningdate = models.DateTimeField(db_column='JoinningDate', blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  
    desgination = models.CharField(db_column='Desgination', max_length=100, blank=True, null=True)  
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE, db_column='CId', blank=True, null=True) 
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True) 
    preaddress = models.CharField(db_column='PreAddress', max_length=150, blank=True, null=True)  
    precity = models.CharField(db_column='PreCity', max_length=50, blank=True, null=True)  
    predist = models.CharField(db_column='PreDist', max_length=50, blank=True, null=True)  
    prestate = models.CharField(db_column='PreState', max_length=50, blank=True, null=True)  
    prepin = models.CharField(db_column='PrePin', max_length=10, blank=True, null=True)  
    peraddress = models.CharField(db_column='PerAddress', max_length=150, blank=True, null=True)  
    percity = models.CharField(db_column='PerCity', max_length=50, blank=True, null=True)  
    perdist = models.CharField(db_column='PerDist', max_length=50, blank=True, null=True)  
    perstate = models.CharField(db_column='PerState', max_length=50, blank=True, null=True)  
    perpin = models.CharField(db_column='PerPin', max_length=10, blank=True, null=True)  
    unno = models.CharField(db_column='UNNo', max_length=50, blank=True, null=True)  
    aadharno = models.CharField(db_column='AadharNo', max_length=20, blank=True, null=True)  
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    accountno = models.CharField(db_column='AccountNo', max_length=50, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCode', max_length=25, blank=True, null=True)  
    
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    conv = models.FloatField(db_column='Conv', blank=True, null=True)  
    maxepf = models.FloatField(db_column='MaxEPF', blank=True, null=True , default=15000)  
    maxesi = models.FloatField(db_column='MaxESI', blank=True, null=True , default=21000)  
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  
    medical = models.FloatField(db_column='Medical', blank=True, null=True)  
    resallow = models.FloatField(db_column='ResAllow', blank=True, null=True)  
    epfno = models.CharField(db_column='EPFNo', max_length=50, blank=True, null=True)  
    esino = models.CharField(db_column='ESINo', max_length=50, blank=True, null=True)  
    wagestype = models.IntegerField(db_column='WagesType', blank=True, null=True)  
    billtype = models.IntegerField(db_column='Billtype', null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=2, blank=True, null=True)  
    leave = models.CharField(max_length=2, blank=True, null=True)
    epf = models.CharField(db_column='EPF', max_length=2, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=2, blank=True, null=True)  
    
    
    userid = models.CharField(db_column='UserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    
    activests = models.BooleanField(default=True , blank=True, null=True)
    
    def toggle_status(self):
        self.activests = not self.activests
        self.save()

    def generate_empcode(self):
        # Get the first character of empname
        first_char = self.empname[0].upper()

        # Find the latest employee with the same first character
        latest_employee = Employeemst.objects.filter(empcode__startswith=first_char).order_by('-empcode').first()

        if latest_employee:
            # Extract the numeric part of the empcode and increment it
            numeric_part = int(latest_employee.empcode[1:]) + 1
        else:
            # If no existing employees with the same first character, start with 1
            numeric_part = 1

        # Format the empcode with leading zeros
        self.empcode = f'{first_char}{numeric_part:04d}'

    def save(self, *args, **kwargs):
        if not self.empcode:
            self.generate_empcode()
        super().save(*args, **kwargs)
    class Meta:
        
        db_table = 'employeemst'

class Emploanhdr(models.Model):
    lid = models.AutoField(db_column='LId', primary_key=True) 
    empcode = models.CharField(db_column='EmpCode', max_length=20, blank=True, null=True) 
    
    empid = models.ForeignKey(Employeemst , on_delete=models.CASCADE , db_column='EmpId', blank=True, null=True)
    
    loanamount = models.FloatField(db_column='LoanAmount', blank=True, null=True) 
    noinst = models.IntegerField(db_column='NoInst', blank=True, null=True) 
    instamount = models.FloatField(db_column='InstAmount', blank=True, null=True) 
    startyearmonth = models.CharField(db_column='StartYearMonth', max_length=20, blank=True, null=True) 
    
    paidinst = models.IntegerField(db_column='PaidInst', blank=True, null=True) 
    appfilepath = models.CharField(db_column='AppFilePath', max_length=100, blank=True, null=True)
    
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True) 
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True) 

    cdt = models.DateTimeField(db_column='CDt', auto_now_add=True, blank=True, null=True)  # auto_now_add=True for creation date
    mdate = models.DateTimeField(db_column='Mdate', auto_now=True, blank=True, null=True)  # auto_now=True for modification date

    status = models.IntegerField(db_column='Status', blank=True, null=True , default=0) 

    class Meta:
        
        db_table = 'EmpLoanHdr'

class Emploandtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lid = models.ForeignKey(Emploanhdr , on_delete=models.CASCADE , db_column='LId', blank=True, null=True)
    empid = models.ForeignKey(Employeemst , on_delete=models.CASCADE , db_column='EmpId', blank=True, null=True)
    yearmonth = models.CharField(db_column='YearMonth', max_length=20, blank=True, null=True) 
    instno = models.IntegerField(db_column='InstNo', blank=True, null=True) 
    instamount = models.FloatField(db_column='InstAmount', blank=True, null=True) 
    status = models.IntegerField(db_column='Status', blank=True, null=True) 
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True) 

    class Meta:
        
        db_table = 'EmpLoanDtl'
        
class Employeesalaryupdate(models.Model):
    slno = models.AutoField(db_column='Slno', primary_key=True) 
    empid = models.ForeignKey(Employeemst , on_delete=models.CASCADE , db_column='EmpId', blank=True, null=True)
    
    cwagestype = models.IntegerField(db_column='CWagesType', blank=True, null=True) 
    cbasic = models.FloatField(db_column='CBasic', blank=True, null=True) 
    
    uwagestype = models.IntegerField(db_column='UWagesType', blank=True, null=True) 
    ubasic = models.FloatField(db_column='UBasic', blank=True, null=True) 
    increment = models.FloatField(db_column='Increment', blank=True, null=True) 
    totalgross = models.FloatField(db_column='TotalGross', blank=True, null=True) 
    
    status = models.IntegerField(db_column='Status', blank=True, null=True , default=0) 
    
    cuserid = models.CharField(db_column='CUserId', max_length=15, blank=True, null=True) 
    cdate = models.DateTimeField(db_column='CDate', auto_now_add=True, blank=True, null=True) 
    auserid = models.CharField(db_column='AUserId', max_length=15, blank=True, null=True) 
    adate = models.DateTimeField(db_column='ADate', blank=True, null=True) 

    class Meta:
        db_table = 'EmployeeSalaryUpdate'

class Empattendancehdr(models.Model):
    aid = models.AutoField(db_column='AId', primary_key=True) 
    
    atnno = models.CharField(db_column='AtnNo', max_length=20, blank=True, null=True) 
    
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE, db_column='CId', blank=True, null=True) 
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True) 
    
    
    atnyearmonth = models.CharField(db_column='AtnYearMonth', max_length=10, blank=True, null=True) 
    
    monthdays = models.IntegerField(db_column='MonthDays', blank=True, null=True) 
    
    totalapprovattn = models.FloatField(db_column='TotalApprovAttn', blank=True, null=True) 
    
    totalemp = models.IntegerField(db_column='TotalEmp', blank=True, null=True) 
    
    gdate = models.DateTimeField(db_column='GDate', auto_now_add=True, blank=True, null=True) 
    guserid = models.CharField(db_column='GUserId', max_length=20, blank=True, null=True) 
    mdate = models.DateTimeField(db_column='MDate', auto_now=True , blank=True, null=True) 
    muserid = models.CharField(db_column='MUserid', max_length=20, blank=True, null=True) 
    
    submitsts = models.IntegerField(db_column='SubmitSts', blank=True, null=True , default=0) 
    
    submituserid = models.CharField(db_column='SubmitUserId', max_length=20, blank=True, null=True) 
    
    submitdt = models.DateTimeField(db_column='SubmitDt', auto_now_add=True, blank=True, null=True) 
    auserid = models.CharField(db_column='AUserId', max_length=20, blank=True, null=True) 
    
    approvstatus = models.IntegerField(db_column='ApprovStatus', blank=True, null=True , default=0) 
    
    approvdate = models.DateTimeField(db_column='ApprovDate', blank=True, null=True) 
    salarystatus = models.IntegerField(db_column='SalaryStatus', blank=True, null=True) 
    salarydate = models.DateTimeField(db_column='SalaryDate', blank=True, null=True) 
    billstatus = models.IntegerField(db_column='BillStatus', blank=True, null=True) 
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True) 
    ruserid = models.CharField(db_column='RUserId', max_length=20, blank=True, null=True) 
    rdate = models.DateTimeField(db_column='RDate', blank=True, null=True) 

    def save(self, *args, **kwargs):
        if not self.atnno:
            # Generate an 8-digit unique positive integer
            while True:
                new_atnno = str(random.randint(10000000, 99999999))
                if not Empattendancehdr.objects.filter(atnno=new_atnno).exists():
                    self.atnno = new_atnno
                    break

        super().save(*args, **kwargs)
        
    class Meta:
        
        db_table = 'EmpAttendanceHdr'
      
class Empattendancedtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    
    aid = models.ForeignKey(Empattendancehdr , on_delete=models.CASCADE,  db_column='AId', blank=True, null=True)  
    empid = models.ForeignKey(Employeemst , on_delete=models.CASCADE,  db_column='EmpId', blank=True, null=True)  
    
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    totaldays = models.FloatField(db_column='TotalDays', blank=True, null=True)  
    present = models.FloatField(db_column='Present', blank=True, null=True)  
    woff = models.FloatField(db_column='Woff', blank=True, null=True)  
    hday = models.FloatField(db_column='HDay', blank=True, null=True)  
    cl = models.FloatField(db_column='CL', blank=True, null=True)  
    el = models.FloatField(db_column='EL', blank=True, null=True)  
    ml = models.FloatField(db_column='ML', blank=True, null=True)  
    lpdays = models.FloatField(db_column='LPDays', blank=True, null=True)  
    
    tsalarydays = models.FloatField(db_column='TSalaryDays', blank=True, null=True)  

    class Meta:
        
        db_table = 'EmpAttendanceDtl'

class Empsalaryhdr(models.Model):
    sid = models.BigAutoField(db_column='SId', primary_key=True) 
    
    salaryno = models.CharField(db_column='SalaryNo', max_length=50, blank=True, null=True)  
    
    
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE, db_column='CId', blank=True, null=True) 
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True)
    aid = models.ForeignKey(Empattendancehdr , db_column='AId',  on_delete=models.CASCADE, blank=True, null=True)
    
    
    attnyearmonth = models.CharField(db_column='AttnYearMonth', max_length=50, blank=True, null=True)  
    
    totalsalary = models.FloatField(db_column='TotalSalary', blank=True, null=True)  
    totalemp = models.IntegerField(db_column='TotalEmp', blank=True, null=True)  
    
    totalholdemp = models.IntegerField(db_column='TotalHoldEmp', blank=True, null=True)   #Null
    
    
    gdate = models.DateTimeField(db_column='GDate', auto_now_add=True,  blank=True, null=True)  
    guserid = models.CharField(db_column='GUserId', max_length=20, blank=True, null=True)  
    
    submitsts = models.IntegerField(db_column='SubmitSts', blank=True, null=True)  
    submitdate = models.DateTimeField(db_column='SubmitDate', auto_now_add=True, blank=True, null=True)  
    submituserid = models.CharField(db_column='SubmitUserid', max_length=20, blank=True, null=True)  
    
    approvstatus = models.IntegerField(db_column='ApprovStatus', blank=True, null=True)  
    approvuserid = models.CharField(db_column='ApprovUserid', max_length=20, blank=True, null=True)  
    approvdate = models.DateTimeField(db_column='ApprovDate', blank=True, null=True)  
    
    paysts = models.IntegerField(db_column='PaySts', blank=True, null=True)  
    paydate = models.DateTimeField(db_column='PayDate', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserId', max_length=20, blank=True, null=True)  
    
    submitpaysts = models.IntegerField(db_column='SubmitPaySts', blank=True, null=True)  
    submitpayuserid = models.CharField(db_column='SubmitPayUserId', max_length=20, blank=True, null=True)  
    submitpaydate = models.DateTimeField(db_column='SubmitPayDate', blank=True, null=True)  

    def save(self, *args, **kwargs):
        if not self.salaryno:
            
            while True:
                new_salaryno = str(random.randint(1000000000, 9999999999))
                if not Empsalaryhdr.objects.filter(salaryno=new_salaryno).exists():
                    self.salaryno = new_salaryno
                    break

        super().save(*args, **kwargs)
    
    class Meta:
        
        db_table = 'empsalaryhdr'

class Empsalarydtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True) 
    
    sid = models.ForeignKey(Empsalaryhdr , db_column='SId',  on_delete=models.CASCADE, blank=True, null=True) 
    
    empid = models.ForeignKey(Employeemst , on_delete=models.CASCADE,  db_column='EmpId', blank=True, null=True) 
    
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    
    attndays = models.FloatField(db_column='AttnDays', blank=True, null=True)  
    
    wagestype = models.IntegerField(db_column='WagesType' ,  blank=True, null=True)  
    basic = models.DecimalField(db_column='Basic', max_digits=18, decimal_places=2, blank=True, null=True)  
    dailywages = models.DecimalField(db_column='DailyWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    atnwages = models.DecimalField(db_column='AtnWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    bonus = models.DecimalField(db_column='Bonus', max_digits=18, decimal_places=2, blank=True, null=True)  
    insentive = models.DecimalField(db_column='Insentive', max_digits=18, decimal_places=2, blank=True, null=True)  
    ot = models.DecimalField(db_column='OT', max_digits=18, decimal_places=2, blank=True, null=True)  
    arrear = models.DecimalField(db_column='Arrear', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    epf = models.DecimalField(db_column='EPF', max_digits=18, decimal_places=2, blank=True, null=True)  
    esi = models.DecimalField(db_column='ESI', max_digits=18, decimal_places=2, blank=True, null=True)  
    emprepf = models.DecimalField(db_column='EmprEPF', max_digits=18, decimal_places=2, blank=True, null=True)  
    empresi = models.DecimalField(db_column='EmprESI', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    ptax = models.DecimalField(db_column='PTax', max_digits=18, decimal_places=2, blank=True, null=True)  
    advance = models.DecimalField(db_column='Advance', max_digits=18, decimal_places=2, blank=True, null=True)  
    uniform = models.DecimalField(db_column='Uniform', max_digits=18, decimal_places=2, blank=True, null=True)  
    others = models.DecimalField(db_column='Others', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    loans = models.DecimalField(db_column='Loans', max_digits=18, decimal_places=2, blank=True, null=True)  
    sewacharge = models.DecimalField(db_column='SewaCharge', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    gross = models.DecimalField(db_column='Gross', max_digits=18, decimal_places=2, blank=True, null=True)  
    netpay = models.DecimalField(db_column='NetPay', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    
    muserid = models.CharField(db_column='MUserid', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    
    processstatus = models.IntegerField(db_column='ProcessStatus', blank=True, null=True)  
    processdt = models.DateTimeField(db_column='ProcessDt', auto_now_add=True , blank=True, null=True)  
    processuserid = models.CharField(db_column='ProcessUserId', max_length=20, blank=True, null=True)  
    
    releasests = models.IntegerField(db_column='ReleaseSts', blank=True, null=True)  
    releasedt = models.DateTimeField(db_column='ReleaseDt', blank=True, null=True)  
    releaseuserid = models.CharField(db_column='ReleaseUserid', max_length=20, blank=True, null=True)  
    
    paystatus = models.IntegerField(db_column='PayStatus', blank=True, null=True)  
    paydt = models.DateTimeField(db_column='PayDt', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserid', max_length=20, blank=True, null=True)  

    class Meta:
        
        db_table = 'empsalarydtl'


class Empepfhdr(models.Model):
    epfid = models.IntegerField(db_column='EpfId', blank=True, null=True)  
    
    epfno = models.CharField(db_column='EpfNo', max_length=50, blank=True, null=True)  
    
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='DId', blank=True, null=True)  
    aid = models.IntegerField(db_column='AId', blank=True, null=True)  
    sid = models.IntegerField(db_column='SId', blank=True, null=True)
    
    
    yearmonth = models.CharField(db_column='YearMonth', max_length=50, blank=True, null=True)  
    totalepf = models.FloatField(db_column='TotalEPF', blank=True, null=True)  
    totalattn = models.FloatField(db_column='TotalAttn', blank=True, null=True)  
    totalemp = models.IntegerField(db_column='TotalEmp', blank=True, null=True)  
    
    gdate = models.DateTimeField(db_column='GDate', blank=True, null=True)  
    guserid = models.CharField(db_column='GUserId', max_length=20, blank=True, null=True)  
    
    submitsts = models.IntegerField(db_column='SubmitSts', blank=True, null=True)  
    submituserid = models.CharField(db_column='SubmitUserid', max_length=20, blank=True, null=True)  
    submitdate = models.DateTimeField(db_column='SubmitDate', blank=True, null=True)  
    
    approvstatus = models.IntegerField(db_column='ApprovStatus', blank=True, null=True)  
    approvuserid = models.CharField(db_column='ApprovUserid', max_length=20, blank=True, null=True)  
    approvdate = models.DateTimeField(db_column='ApprovDate', blank=True, null=True)  
    
    batchno = models.CharField(db_column='BatchNo', max_length=10, blank=True, null=True)  
    
    submitpaysts = models.IntegerField(db_column='SubmitPaySts', blank=True, null=True)  
    submitpayuserid = models.CharField(db_column='SubmitPayUserId', max_length=20, blank=True, null=True)  
    submitpaydate = models.DateTimeField(db_column='SubmitPayDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'empepfhdr'



class Empepfdtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    
    epfid = models.IntegerField(db_column='EpfId', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    sattndays = models.FloatField(db_column='SAttnDays', blank=True, null=True)  
    dailywages = models.DecimalField(db_column='DailyWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    atnwages = models.DecimalField(db_column='AtnWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    salaryepfemp = models.DecimalField(db_column='SalaryEPFEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    salaryepfempr = models.DecimalField(db_column='SalaryEPFEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    salaryepf = models.DecimalField(db_column='SalaryEPF', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfwages = models.DecimalField(db_column='EPFWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfempper = models.FloatField(db_column='EpfEmpPer', blank=True, null=True)  
    epfemprper = models.FloatField(db_column='EpfEmprPer', blank=True, null=True)  
    epfper = models.FloatField(db_column='EpfPer', blank=True, null=True)  
    eattndays = models.FloatField(db_column='EAttnDays', blank=True, null=True)  
    epfemp = models.DecimalField(db_column='EPFEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfempr = models.DecimalField(db_column='EPFEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfdeposit = models.DecimalField(db_column='EPFDeposit', max_digits=18, decimal_places=2, blank=True, null=True)  
    
    status = models.IntegerField(db_column='Status', blank=True, null=True)  
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  
    
    muserid = models.CharField(db_column='MUserid', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    
    processstatus = models.IntegerField(db_column='ProcessStatus', blank=True, null=True)  
    processuserid = models.CharField(db_column='ProcessUserId', max_length=20, blank=True, null=True)  
    processdt = models.DateTimeField(db_column='ProcessDt', blank=True, null=True)  
    
    releasests = models.IntegerField(db_column='ReleaseSts', blank=True, null=True)  
    releaseuserid = models.CharField(db_column='ReleaseUserId', max_length=20, blank=True, null=True)  
    releasedt = models.DateTimeField(db_column='ReleaseDt', blank=True, null=True)  
    
    paystatus = models.IntegerField(db_column='PayStatus', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserId', max_length=20, blank=True, null=True)  
    paydt = models.DateTimeField(db_column='PayDt', blank=True, null=True)  

    class Meta:
        
        db_table = 'empepfdtl'


class Billhdr(models.Model):
    bid = models.AutoField(db_column='Bid' , primary_key=True)
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE , db_column='CId', blank=True, null=True)
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True)
    
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    
    billreffno = models.CharField(db_column='BillReffNo', max_length=20, blank=True, null=True)
    billno = models.CharField(db_column='BillNo', max_length=50, blank=True, null=True)   
    orderno = models.CharField(db_column='OrderNo', max_length=50, blank=True, null=True)  
    
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True) 

    address1 = models.CharField(db_column='Address1', max_length=500, blank=True, null=True)  
    address2 = models.CharField(db_column='Address2', max_length=500, blank=True, null=True)  
    
    gross = models.FloatField(db_column='Gross', blank=True, null=True)  
    epfsts = models.IntegerField(db_column='EpfSts', blank=True, null=True)  
    epfper = models.FloatField(db_column='EpfPer', blank=True, null=True)  
    epf = models.FloatField(db_column='Epf', blank=True, null=True)  
    esists = models.IntegerField(db_column='EsiSts', blank=True, null=True)  
    esiper = models.FloatField(db_column='EsiPer', blank=True, null=True)  
    esi = models.FloatField(db_column='ESI', blank=True, null=True)  
    srvsts = models.IntegerField(db_column='SrvSts', blank=True, null=True)  
    srvon = models.IntegerField(db_column='SrvOn', blank=True, null=True)  
    srvvalue = models.FloatField(db_column='SrvValue', blank=True, null=True)  
    srvcharge = models.FloatField(db_column='SrvCharge', blank=True, null=True)  
    bonussts = models.IntegerField(db_column='BonusSts', blank=True, null=True)  
    bonus = models.FloatField(db_column='Bonus', blank=True, null=True)  
    leavests = models.IntegerField(db_column='LeaveSts', blank=True, null=True)  
    leave = models.FloatField(db_column='Leave', blank=True, null=True)  
    nfholidayssts = models.IntegerField(db_column='NFHolidaysSts', blank=True, null=True)  
    nfholidays = models.FloatField(db_column='NFHolidays', blank=True, null=True)  
    materialsts = models.IntegerField(db_column='MaterialSts', blank=True, null=True)  
    material = models.FloatField(db_column='Material', blank=True, null=True)  
    fulests = models.IntegerField(db_column='FuleSts', blank=True, null=True)  
    fule = models.FloatField(db_column='Fule', blank=True, null=True)  
    machinarysts = models.IntegerField(db_column='MachinarySts', blank=True, null=True)  
    machinary = models.FloatField(db_column='Machinary', blank=True, null=True)  
    otherssts = models.IntegerField(db_column='OthersSts', blank=True, null=True)  
    othersname = models.CharField(db_column='OthersName', max_length=50, blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    gststs = models.IntegerField(db_column='GstSts', blank=True, null=True)  
    gstper = models.FloatField(db_column='GstPer', blank=True, null=True)  
    gston = models.CharField(db_column='GSTOn', max_length=50, blank=True, null=True)  
    gstgross = models.FloatField(db_column='GSTGross', blank=True, null=True)  
    gst = models.FloatField(db_column='GST', blank=True, null=True)  
    totalbill = models.FloatField(db_column='TotalBill', blank=True, null=True)  
    bankaccid = models.IntegerField(db_column='BankAccId', blank=True, null=True)  
    submit = models.IntegerField(db_column='Submit', blank=True, null=True)  
    submitdate = models.DateTimeField(db_column='SubmitDate', blank=True, null=True)  
    submituserid = models.CharField(db_column='SubmitUserId', max_length=20, blank=True, null=True)  
    approve = models.IntegerField(db_column='Approve', blank=True, null=True)  
    appdate = models.DateTimeField(db_column='AppDate', blank=True, null=True)  
    appuserid = models.CharField(db_column='AppUserId', max_length=20, blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    city = models.CharField(db_column='City', max_length=200, blank=True, null=True)  
    contactperson = models.CharField(db_column='ContactPerson', max_length=100, blank=True, null=True)  
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  
    fax = models.CharField(db_column='Fax', max_length=30, blank=True, null=True)  
    email = models.CharField(db_column='EMail', max_length=100, blank=True, null=True)  
    pan = models.CharField(db_column='PAN', max_length=20, blank=True, null=True)  
    gstin = models.CharField(db_column='GSTIN', max_length=30, blank=True, null=True)  
    provcontactperson = models.CharField(db_column='ProvContactPerson', max_length=100, blank=True, null=True)  
    provphone = models.CharField(db_column='ProvPhone', max_length=30, blank=True, null=True)  
    attndate = models.CharField(db_column='AttnDate', max_length=50, blank=True, null=True)  

    class Meta:
        db_table = 'billhdr'

class Billdtl(models.Model):
    bdid = models.AutoField(db_column='BDid' , primary_key=True)
    bid = models.ForeignKey(Billhdr, on_delete=models.CASCADE, db_column='Bid', blank=True, null=True, related_name='bill_details')
    
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)  
    str = models.IntegerField(db_column='Str', blank=True, null=True)  
    wages = models.FloatField(db_column='Wages', blank=True, null=True)  
    wtype = models.IntegerField(db_column='WType', blank=True, null=True)  
    qnty = models.FloatField(db_column='Qnty', blank=True, null=True)  
    total = models.FloatField(db_column='Total', blank=True, null=True)  
    sts = models.IntegerField(db_column='Sts', blank=True, null=True)  
    
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=50, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        db_table = 'billdtl'


class Clientcontactdetails(models.Model):
    cpid = models.BigAutoField(db_column='CpId', primary_key=True)  
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE, db_column='Cid', blank=True, null=True)
    cguid = models.CharField(db_column='CGuid', max_length=50, blank=True, null=True)  
    contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  
    contactmobileno = models.CharField(db_column='ContactMobileNo', max_length=50, blank=True, null=True)  
    contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True)  
    contactdesg = models.CharField(db_column='ContactDesg', max_length=50, blank=True, null=True)  
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    remark = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        
        db_table = 'clientcontactdetails'




class Companydocuments(models.Model):
    docid = models.AutoField(db_column='DocId', primary_key=True) 
    
    docname = models.CharField(db_column='DocName', max_length=500, blank=True, null=True) 
    docregdt = models.CharField(db_column='DocRegDt', max_length=50, blank=True, null=True) 
    docexpirdt = models.CharField(db_column='DocExpirDt', max_length=50, blank=True, null=True) 
    
    unsignpath = models.CharField(db_column='UnSignPath', max_length=500, blank=True, null=True) 
    signpath = models.CharField(db_column='SignPath', max_length=500, blank=True, null=True) 
    
    status = models.IntegerField(db_column='Status', blank=True, null=True) 
    
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True) 
    cdate = models.DateTimeField(db_column='CDate', auto_now_add=True , blank=True, null=True) 
    
    muserid = models.CharField(db_column='MUserid', max_length=20,  db_collation='utf8mb4_general_ci', blank=True, null=True) 
    mdate = models.DateTimeField(db_column='MDate', blank=True, auto_now=True , null=True) 

    class Meta:
        
        db_table = 'CompanyDocuments'





class Tenders(models.Model):
    tid = models.AutoField(db_column='Tid', primary_key=True)
    
    tendername = models.CharField(db_column='TenderName', blank=True, null=True , max_length=200)  
    tendertype = models.IntegerField(db_column='TenderType', blank=True, null=True)  
    publishdate = models.DateTimeField(db_column='PublishDate', blank=True, null=True)  
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)  
    contractvalue = models.FloatField(db_column='ContractValue', blank=True, null=True)  
    contractperiod = models.CharField(db_column='ContractPeriod', max_length=50, blank=True, null=True)  
    websitename = models.CharField(db_column='WebSiteName', max_length=100, blank=True, null=True)  
    dateadm = models.DateTimeField(db_column='DateAdm', blank=True, null=True)  
    
    pribidmeet = models.DateTimeField(db_column='PriBidMeet', blank=True, null=True)  
    
    lsubmisiondate = models.DateTimeField(db_column='LSubmisionDate', blank=True, null=True)  
    modesubmision = models.CharField(db_column='ModeSubmision', max_length=50, blank=True, null=True)  
    techinecalbidopen = models.DateTimeField(db_column='TechinecalBidOpen', blank=True, null=True)  
    financialbidopen = models.DateTimeField(db_column='FinancialBidOpen', blank=True, null=True)  
    papercost = models.FloatField(db_column='PaperCost', blank=True, null=True)  
    
    emd = models.CharField(db_column='EMD', max_length=50, blank=True, null=True)  
    
    prepareuserid = models.CharField(db_column='PrepareUserId', max_length=20, blank=True, null=True)  
    moniteruserid = models.CharField(db_column='MoniterUserId', max_length=20, blank=True, null=True)  
    
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True) 
    
    submitsts = models.IntegerField(db_column='SubmitSts', blank=True, null=True) 
    
    submituserid = models.CharField(db_column='SubmitUserId', max_length=50, blank=True, null=True)  
    submitdt = models.DateTimeField(db_column='SubmitDt', blank=True, null=True) 
    
    advdocpath = models.CharField(db_column='AdvDocPath', max_length=200, blank=True, null=True)  
    status = models.IntegerField(db_column='Status', blank=True, null=True)  
    

    class Meta:
        
        db_table = 'tenders'


class Tenderstatusdoc(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    tid = models.ForeignKey(Tenders, on_delete=models.CASCADE , db_column='Tid', blank=True, null=True) 
    
    statustype = models.IntegerField(db_column='StatusType', blank=True, null=True)  
    statusremark = models.CharField(db_column='StatusRemark', blank=True, null=True , max_length=20)  
    docpath = models.CharField(db_column='DocPath', max_length=500, blank=True, null=True)  
    
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)

    class Meta:
        db_table = 'tenderstatusdoc'


class Tenderfinbiddoc(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    tid = models.ForeignKey(Tenders, on_delete=models.CASCADE , db_column='Tid', blank=True, null=True) 
    
    finbidtype = models.IntegerField(db_column='FinBidType', blank=True, null=True)  
    finbidremark = models.CharField(db_column='FinBidRemark', blank=True, null=True , max_length=20)  
    docpath = models.CharField(db_column='DocPath', max_length=500, blank=True, null=True)  
    
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)

    class Meta:
        db_table = 'tenderfinbiddoc'
    

class Tenderdocument(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    
    tid = models.ForeignKey(Tenders, on_delete=models.CASCADE , db_column='Tid', blank=True, null=True) 
    docid = models.ForeignKey(Companydocuments, on_delete=models.CASCADE , db_column='DocId', blank=True, null=True) 
    
     
    
    tenderdocname = models.CharField(db_column='TenderDocName', max_length=500, blank=True, null=True)  
    docpath = models.CharField(db_column='DocPath', max_length=500, blank=True, null=True)  
    sno = models.IntegerField(db_column='SNo', blank=True, null=True)  
    noofpage = models.IntegerField(db_column='NoOfPage', blank=True, null=True)  
    spage = models.IntegerField(db_column='SPage', blank=True, null=True)  
    epage = models.IntegerField(db_column='EPage', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)

    class Meta:
        
        db_table = 'tenderdocument'



















class Autotradehdr(models.Model):
    trdid = models.IntegerField(db_column='TrdId', blank=True, null=True)  
    tradecode = models.CharField(db_column='TradeCode', max_length=30, blank=True, null=True)  
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  
    addendtime = models.DateTimeField(db_column='AddEndTime', blank=True, null=True)  
    closetime = models.DateTimeField(db_column='CloseTime', blank=True, null=True)  
    addsts = models.IntegerField(db_column='AddSts', blank=True, null=True)  
    totalbuy = models.FloatField(db_column='TotalBuy', blank=True, null=True)  
    totalsell = models.FloatField(db_column='TotalSell', blank=True, null=True)  
    winsts = models.IntegerField(db_column='WinSts', blank=True, null=True)  
    trdstatus = models.IntegerField(db_column='TrdStatus', blank=True, null=True)  
    dt = models.DateTimeField(db_column='Dt', blank=True, null=True)  
    udt = models.DateTimeField(auto_now=True, db_column='UDt', blank=True, null=True)    

    class Meta:
        db_table = 'autotradehdr'

class Autotradermbrdtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    trdid = models.IntegerField(db_column='TrdId', blank=True, null=True)  
    mbrid = models.CharField(db_column='MbrId', max_length=20, blank=True, null=True  )  
    tradetype = models.IntegerField(db_column='TradeType', blank=True, null=True)  
    tradeamt = models.FloatField(db_column='TradeAmt', blank=True, null=True)  
    leverage = models.IntegerField(db_column='Leverage', blank=True, null=True)  
    dt = models.DateTimeField(db_column='Dt', blank=True, null=True)  

    class Meta:
        db_table = 'autotradermbrdtl'

class Autotradewallet(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    mbrid = models.CharField(db_column='MbrId', max_length=15, blank=True, null=True  )  
    tid = models.IntegerField(db_column='Tid', blank=True, null=True)  
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  
    ttype = models.CharField(db_column='Ttype', max_length=5, blank=True, null=True)  
    dt = models.DateTimeField(db_column='Dt', blank=True, null=True)  

    class Meta:
        
        db_table = 'autotradewallet'

class Branch(models.Model):
    bid = models.IntegerField(db_column='Bid', blank=True, null=True)  
    branch = models.CharField(db_column='Branch', max_length=50, blank=True, null=True)  

    class Meta:
        
        db_table = 'branch'

class Clientbillmst(models.Model):
    bid = models.IntegerField(db_column='BId', blank=True, null=True)  
    did = models.IntegerField(db_column='Did', blank=True, null=True)  
    monthyear = models.CharField(db_column='MonthYear', max_length=15, blank=True, null=True)  
    billno = models.CharField(db_column='BillNo', max_length=50, blank=True, null=True)  
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)  
    billamount = models.FloatField(db_column='BillAmount', blank=True, null=True)  
    wages = models.FloatField(db_column='Wages', blank=True, null=True)  
    efp = models.FloatField(db_column='EFP', blank=True, null=True)  
    esi = models.FloatField(db_column='ESI', blank=True, null=True)  
    srvcharge = models.FloatField(db_column='SrvCharge', blank=True, null=True)  
    bonus = models.FloatField(db_column='Bonus', blank=True, null=True)  
    nfholidays = models.FloatField(db_column='NFHolidays', blank=True, null=True)  
    material = models.FloatField(db_column='Material', blank=True, null=True)  
    fule = models.FloatField(db_column='Fule', blank=True, null=True)  
    machinary = models.FloatField(db_column='Machinary', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    total = models.FloatField(db_column='Total', blank=True, null=True)  
    gst = models.FloatField(db_column='GST', blank=True, null=True)  
    filepath = models.CharField(db_column='FilePath', max_length=500, blank=True, null=True)  
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=50, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=50, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    leave = models.FloatField(db_column='Leave', blank=True, null=True)  
    gstgross = models.FloatField(db_column='GSTGross', blank=True, null=True)  
    bhid = models.IntegerField(db_column='BHId', blank=True, null=True)  
    approve = models.IntegerField(db_column='Approve', blank=True, null=True)  
    appdate = models.DateTimeField(db_column='AppDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'clientbillmst'

class Clientbillreceive(models.Model):
    brid = models.AutoField(db_column='BRId', primary_key=True) 
    
    bid = models.ForeignKey(Clientbillmst, on_delete=models.CASCADE, db_column='Bid', blank=True, null=True)
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True)  
    recptno = models.CharField(db_column='RecptNo', max_length=25, blank=True, null=True)  
    recvamount = models.FloatField(db_column='RecvAmount', blank=True, null=True)  
    tds = models.FloatField(db_column='TDS', blank=True, null=True)  
    gst = models.FloatField(db_column='GST', blank=True, null=True)  
    penalty = models.FloatField(db_column='Penalty', blank=True, null=True)  
    other = models.FloatField(db_column='Other', blank=True, null=True)  
    total = models.FloatField(db_column='Total', blank=True, null=True)  
    receivedt = models.DateTimeField(db_column='ReceiveDt', blank=True, null=True)  
    bank = models.CharField(db_column='Bank', max_length=50, blank=True, null=True)  
    chequeno = models.CharField(db_column='ChequeNo', max_length=50, blank=True, null=True)  
    materialexpr = models.FloatField(db_column='MaterialExpr', blank=True, null=True)  
    fuleexpr = models.FloatField(db_column='FuleExpr', blank=True, null=True)  
    adminexpr = models.FloatField(db_column='AdminExpr', blank=True, null=True)  
    otherexpr = models.FloatField(db_column='OtherExpr', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    gsttds = models.FloatField(db_column='GSTTds', blank=True, null=True)  
    billtype = models.IntegerField(db_column='BillType', blank=True, null=True)  

    class Meta:
        
        db_table = 'clientbillreceive'


class Clientcharges(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    empepf = models.FloatField(db_column='EmpEPF', blank=True, null=True)  
    emprepf = models.FloatField(db_column='EmprEPF', blank=True, null=True)  
    epfwages = models.FloatField(db_column='EPFWages', blank=True, null=True)  
    empesi = models.FloatField(db_column='EmpESI', blank=True, null=True)  
    empresi = models.FloatField(db_column='EmprESI', blank=True, null=True)  
    esiwages = models.FloatField(db_column='ESIWages', blank=True, null=True)  
    gst = models.FloatField(db_column='GST', blank=True, null=True)  
    servicecharge = models.FloatField(db_column='ServiceCharge', blank=True, null=True)  
    tds = models.FloatField(db_column='TDS', blank=True, null=True)  

    class Meta:
        
        db_table = 'clientcharges'



class Clientexpenditure(models.Model):
    exid = models.AutoField(db_column='ExId', primary_key=True) 
    cid = models.ForeignKey(Clientmst, on_delete=models.CASCADE , db_column='CId', blank=True, null=True) 
    did = models.ForeignKey(Divisionmst, on_delete=models.CASCADE, db_column='Did', blank=True, null=True)
    
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    materialexpr = models.FloatField(db_column='MaterialExpr', blank=True, null=True)  
    fuleexpr = models.FloatField(db_column='FuleExpr', blank=True, null=True)  
    adminexpr = models.FloatField(db_column='AdminExpr', blank=True, null=True)  
    otherexpr = models.FloatField(db_column='OtherExpr', blank=True, null=True)  
    travelexpr = models.FloatField(db_column='TravelExpr', blank=True, null=True)  
    expdate = models.DateTimeField(db_column='ExpDate', blank=True, null=True)  
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'clientexpenditure'



class Clientmst1(models.Model):
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    ccode = models.CharField(db_column='CCode', max_length=10, blank=True, null=True)  
    cname = models.CharField(db_column='CName', max_length=100, blank=True, null=True)  
    csname = models.CharField(db_column='CSName', max_length=50, blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  
    district = models.CharField(db_column='District', max_length=50, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  
    pin = models.CharField(db_column='Pin', max_length=10, blank=True, null=True)  
    oficeph = models.CharField(db_column='OficePh', max_length=15, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  
    contractno = models.CharField(db_column='ContractNo', max_length=20, blank=True, null=True)  
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  
    gstno = models.CharField(db_column='GSTNo', max_length=30, blank=True, null=True)  
    contractvalue = models.FloatField(db_column='ContractValue', blank=True, null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=5, blank=True, null=True)  
    epf = models.CharField(db_column='EPF', max_length=5, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=5, blank=True, null=True)  
    contactperson = models.CharField(db_column='ContactPerson', max_length=50, blank=True, null=True)  
    contactmobileno = models.CharField(db_column='ContactMobileNo', max_length=15, blank=True, null=True)  
    contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True)  
    contactdesg = models.CharField(db_column='ContactDesg', max_length=50, blank=True, null=True)  
    userid = models.CharField(db_column='Userid', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'clientmst_1'


class Companybank(models.Model):
    accid = models.IntegerField(db_column='AccId', blank=True, null=True)  
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    accno = models.CharField(db_column='AccNo', max_length=50, blank=True, null=True)  
    ifsc = models.CharField(db_column='IFSC', max_length=50, blank=True, null=True)  

    class Meta:
        
        db_table = 'companybank'





class DelEmployeemst20230127(models.Model):
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=10, blank=True, null=True)  
    empname = models.CharField(db_column='EmpName', max_length=100, blank=True, null=True)  
    empfhname = models.CharField(db_column='EmpFHName', max_length=100, blank=True, null=True)  
    empdob = models.DateTimeField(db_column='EmpDob', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  
    mobileno = models.CharField(db_column='MobileNo', max_length=30, blank=True, null=True)  
    emergencyno = models.CharField(db_column='EmergencyNo', max_length=15, blank=True, null=True)  
    bloodgroup = models.CharField(db_column='BloodGroup', max_length=5, blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=15, blank=True, null=True)  
    joinningdate = models.DateTimeField(db_column='JoinningDate', blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  
    desgination = models.CharField(db_column='Desgination', max_length=100, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='Did', blank=True, null=True)  
    preaddress = models.CharField(db_column='PreAddress', max_length=150, blank=True, null=True)  
    precity = models.CharField(db_column='PreCity', max_length=50, blank=True, null=True)  
    predist = models.CharField(db_column='PreDist', max_length=50, blank=True, null=True)  
    prestate = models.CharField(db_column='PreState', max_length=50, blank=True, null=True)  
    prepin = models.CharField(db_column='PrePin', max_length=10, blank=True, null=True)  
    peraddress = models.CharField(db_column='PerAddress', max_length=150, blank=True, null=True)  
    percity = models.CharField(db_column='PerCity', max_length=50, blank=True, null=True)  
    perdist = models.CharField(db_column='PerDist', max_length=50, blank=True, null=True)  
    perstate = models.CharField(db_column='PerState', max_length=50, blank=True, null=True)  
    perpin = models.CharField(db_column='PerPin', max_length=10, blank=True, null=True)  
    unno = models.CharField(db_column='UNNo', max_length=50, blank=True, null=True)  
    aadharno = models.CharField(db_column='AadharNo', max_length=20, blank=True, null=True)  
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    accountno = models.CharField(db_column='AccountNo', max_length=50, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCode', max_length=25, blank=True, null=True)  
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    conv = models.FloatField(db_column='Conv', blank=True, null=True)  
    maxepf = models.FloatField(db_column='MaxEPF', blank=True, null=True)  
    maxesi = models.FloatField(db_column='MaxESI', blank=True, null=True)  
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  
    medical = models.FloatField(db_column='Medical', blank=True, null=True)  
    resallow = models.FloatField(db_column='ResAllow', blank=True, null=True)  
    epfno = models.CharField(db_column='EPFNo', max_length=50, blank=True, null=True)  
    esino = models.CharField(db_column='ESINo', max_length=50, blank=True, null=True)  
    wagestype = models.CharField(db_column='WagesType', max_length=2, blank=True, null=True)  
    billtype = models.CharField(db_column='Billtype', max_length=2, blank=True, null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=2, blank=True, null=True)  
    leave = models.CharField(max_length=2, blank=True, null=True)
    epf = models.CharField(db_column='EPF', max_length=2, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=2, blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    activests = models.IntegerField(db_column='ActiveSts', blank=True, null=True)  

    class Meta:
        
        db_table = 'del_employeemst_20230127'





class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class Emp9(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.DateTimeField(db_column='Date of birth', blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.CharField(db_column='Emergency No', max_length=255, blank=True, null=True)   
    blood_group = models.CharField(db_column='Blood Group', max_length=255, blank=True, null=True)   
    date_of_joinning = models.DateTimeField(db_column='Date of Joinning', blank=True, null=True)   
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.FloatField(db_column='UN No#', blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp9'


class Emp1(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='EMPLYEE CODE', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='EMPLYEE NAME', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='FATHER/HUSBAND NAME', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='CLIENT CODE', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='CLIENT NAME', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='DIVISION', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='DESIGNATION', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='DEPARTMENT', max_length=255, blank=True, null=True)  
    date_of_birth = models.CharField(db_column='DATE OF BIRTH', max_length=255, blank=True, null=True)   
    qualification = models.CharField(db_column='QUALIFICATION', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='MOBILE NO#', max_length=255, blank=True, null=True)
    emergency_no = models.DateTimeField(db_column='EMERGENCY NO', blank=True, null=True)   
    blood_group = models.FloatField(db_column='BLOOD GROUP', blank=True, null=True)   
    date_of_joinning = models.CharField(db_column='DATE OF JOINNING', max_length=255, blank=True, null=True)   
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='PRESENT ADDRESS', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='DISTIRCT', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='STATE', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='PIN CODE', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='AADHAR NO#', max_length=255, blank=True, null=True)
    uan_no = models.FloatField(db_column='UAN# NO', blank=True, null=True)   
    epf_no_field = models.CharField(db_column='EPF NO#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI NO#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/C NUMBER', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC CODE', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='BANK NAME', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='WAGES TYPE', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='BASIC WAGES', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  
    status1 = models.CharField(db_column='STATUS1', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_1'


class Emp10Delete(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyeecode = models.CharField(db_column='EmplyeeCode', max_length=255, blank=True, null=True)  
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.CharField(db_column='Date of birth', max_length=255, blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.CharField(db_column='Emergency No', max_length=255, blank=True, null=True)   
    blood_group = models.CharField(db_column='Blood Group', max_length=255, blank=True, null=True)   
    date_of_joinning = models.CharField(db_column='Date of Joinning', max_length=255, blank=True, null=True)   
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.CharField(db_column='UN No#', max_length=255, blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_10_delete'


class Emp2(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.CharField(db_column='Date of birth', max_length=255, blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.DateTimeField(db_column='Emergency No', blank=True, null=True)   
    blood_group = models.FloatField(db_column='Blood Group', blank=True, null=True)   
    date_of_joinning = models.CharField(db_column='Date of Joinning', max_length=255, blank=True, null=True)   
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.FloatField(db_column='UN No#', blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_2'


class Emp3(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.CharField(db_column='Date of birth', max_length=255, blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.CharField(db_column='Emergency No', max_length=255, blank=True, null=True)   
    blood_group = models.CharField(db_column='Blood Group', max_length=255, blank=True, null=True)   
    date_of_joinning = models.CharField(db_column='Date of Joinning', max_length=255, blank=True, null=True)   
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.CharField(db_column='UN No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  
    f33 = models.CharField(db_column='F33', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_3'


class Emp4(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.DateTimeField(db_column='Date of birth', blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.CharField(db_column='Emergency No', max_length=255, blank=True, null=True)   
    blood_group = models.CharField(db_column='Blood Group', max_length=255, blank=True, null=True)   
    date_of_joinning = models.DateTimeField(db_column='Date of Joinning', blank=True, null=True)   
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.FloatField(db_column='UN No#', blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  
    f34 = models.CharField(db_column='F34', max_length=255, blank=True, null=True)  
    f35 = models.CharField(db_column='F35', max_length=255, blank=True, null=True)  
    f36 = models.CharField(db_column='F36', max_length=255, blank=True, null=True)  
    f37 = models.CharField(db_column='F37', max_length=255, blank=True, null=True)  
    f38 = models.CharField(db_column='F38', max_length=255, blank=True, null=True)  
    f39 = models.CharField(db_column='F39', max_length=255, blank=True, null=True)  
    f40 = models.CharField(db_column='F40', max_length=255, blank=True, null=True)  
    f41 = models.CharField(db_column='F41', max_length=255, blank=True, null=True)  
    f42 = models.CharField(db_column='F42', max_length=255, blank=True, null=True)  
    f43 = models.CharField(db_column='F43', max_length=255, blank=True, null=True)  
    f44 = models.CharField(db_column='F44', max_length=255, blank=True, null=True)  
    f45 = models.CharField(db_column='F45', max_length=255, blank=True, null=True)  
    f46 = models.CharField(db_column='F46', max_length=255, blank=True, null=True)  
    f47 = models.CharField(db_column='F47', max_length=255, blank=True, null=True)  
    f48 = models.CharField(db_column='F48', max_length=255, blank=True, null=True)  
    f49 = models.CharField(db_column='F49', max_length=255, blank=True, null=True)  
    f50 = models.CharField(db_column='F50', max_length=255, blank=True, null=True)  
    f51 = models.CharField(db_column='F51', max_length=255, blank=True, null=True)  
    f52 = models.CharField(db_column='F52', max_length=255, blank=True, null=True)  
    f53 = models.CharField(db_column='F53', max_length=255, blank=True, null=True)  
    f54 = models.CharField(db_column='F54', max_length=255, blank=True, null=True)  
    f55 = models.CharField(db_column='F55', max_length=255, blank=True, null=True)  
    f56 = models.CharField(db_column='F56', max_length=255, blank=True, null=True)  
    f57 = models.CharField(db_column='F57', max_length=255, blank=True, null=True)  
    f58 = models.CharField(db_column='F58', max_length=255, blank=True, null=True)  
    f59 = models.CharField(db_column='F59', max_length=255, blank=True, null=True)  
    f60 = models.CharField(db_column='F60', max_length=255, blank=True, null=True)  
    f61 = models.CharField(db_column='F61', max_length=255, blank=True, null=True)  
    f62 = models.CharField(db_column='F62', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_4'


class Emp5(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.CharField(db_column='Date of birth', max_length=255, blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.DateTimeField(db_column='Emergency No', blank=True, null=True)   
    blood_group = models.FloatField(db_column='Blood Group', blank=True, null=True)   
    doj = models.CharField(db_column='DOJ', max_length=255, blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.CharField(db_column='UN No#', max_length=255, blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  
    jhggf = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'emp_5'


class Emp6(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.DateTimeField(db_column='Date of birth', blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.CharField(db_column='Emergency No', max_length=255, blank=True, null=True)   
    blood_group = models.CharField(db_column='Blood Group', max_length=255, blank=True, null=True)   
    date_of_joinning = models.DateTimeField(db_column='Date of Joinning', blank=True, null=True)   
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.CharField(db_column='UN No#', max_length=255, blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_6'


class Emp7(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.DateTimeField(db_column='Date of birth', blank=True, null=True)   
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mobile_no_field = models.CharField(db_column='Mobile No#', max_length=255, blank=True, null=True)
    emergency_no = models.CharField(db_column='Emergency No', max_length=255, blank=True, null=True)   
    blood_group = models.CharField(db_column='Blood Group', max_length=255, blank=True, null=True)   
    date_of_joinning = models.DateTimeField(db_column='Date of Joinning', blank=True, null=True)   
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.CharField(db_column='UN No#', max_length=255, blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.CharField(db_column='ESI No#', max_length=255, blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_7'


class Emp8Add(models.Model):
    sl_no_field = models.FloatField(db_column='Sl# No#', blank=True, null=True)
    emplyee_code = models.CharField(db_column='Emplyee Code', max_length=255, blank=True, null=True)   
    emplyee_name = models.CharField(db_column='Emplyee Name', max_length=255, blank=True, null=True)   
    father_husband_name = models.CharField(db_column='Father/Husband Name', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    client_name = models.CharField(db_column='Client Name', max_length=255, blank=True, null=True)   
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    date_of_birth = models.DateTimeField(db_column='Date of birth', blank=True, null=True)   
    qualification = models.DateTimeField(db_column='Qualification', blank=True, null=True)  
    mobile_no_field = models.FloatField(db_column='Mobile No#', blank=True, null=True)
    emergency_no = models.CharField(db_column='Emergency No', max_length=255, blank=True, null=True)   
    blood_group = models.DateTimeField(db_column='Blood Group', blank=True, null=True)   
    doj = models.DateTimeField(db_column='DOJ', blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  
    present_address = models.CharField(db_column='Present Address', max_length=255, blank=True, null=True)   
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  
    distirct = models.CharField(db_column='Distirct', max_length=255, blank=True, null=True)  
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  
    pin_code = models.CharField(db_column='Pin Code', max_length=255, blank=True, null=True)   
    aadhar_no_field = models.CharField(db_column='Aadhar No#', max_length=255, blank=True, null=True)
    un_no_field = models.CharField(db_column='UN No#', max_length=255, blank=True, null=True)
    epf_no_field = models.CharField(db_column='EPF No#', max_length=255, blank=True, null=True)
    esi_no_field = models.FloatField(db_column='ESI No#', blank=True, null=True)
    a_c_number = models.CharField(db_column='A/c Number', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    wages_type = models.CharField(db_column='Wages Type', max_length=255, blank=True, null=True)   
    basic_wages = models.CharField(db_column='Basic Wages', max_length=255, blank=True, null=True)   
    epf = models.CharField(db_column='EPF', max_length=255, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=255, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_8add'


class EmpNew(models.Model):
    slno = models.FloatField(db_column='SLNO', blank=True, null=True)  
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  
    fname = models.CharField(db_column='FNAME', max_length=255, blank=True, null=True)  
    clientcode = models.CharField(db_column='ClientCode', max_length=255, blank=True, null=True)  
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  
    doj = models.DateTimeField(db_column='DOJ', blank=True, null=True)  
    paddress = models.CharField(db_column='PAddress', max_length=255, blank=True, null=True)  
    aadharno = models.FloatField(db_column='AadharNo', blank=True, null=True)  
    unno = models.FloatField(db_column='UNNo', blank=True, null=True)  
    esic = models.CharField(db_column='ESIC', max_length=255, blank=True, null=True)  
    bankname = models.CharField(db_column='BANKNAME', max_length=255, blank=True, null=True)  
    accountno = models.CharField(db_column='ACCOUNTNO', max_length=255, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCODE', max_length=255, blank=True, null=True)  
    basicwages = models.FloatField(db_column='BasicWages', blank=True, null=True)  
    cid = models.IntegerField(db_column='CID', blank=True, null=True)  
    did = models.IntegerField(db_column='DId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=20, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_new'


class EmpNew1(models.Model):
    slno = models.FloatField(db_column='SLNO', blank=True, null=True)  
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  
    fname = models.CharField(db_column='FNAME', max_length=255, blank=True, null=True)  
    clientcode = models.CharField(db_column='ClientCode', max_length=255, blank=True, null=True)  
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  
    doj = models.DateTimeField(db_column='DOJ', blank=True, null=True)  
    paddress = models.CharField(db_column='Paddress', max_length=255, blank=True, null=True)  
    aadharno = models.CharField(db_column='AadharNo', max_length=255, blank=True, null=True)  
    unno = models.FloatField(db_column='UNNo', blank=True, null=True)  
    esic = models.FloatField(db_column='ESIC', blank=True, null=True)  
    bankname = models.CharField(db_column='BANKNAME', max_length=255, blank=True, null=True)  
    accountno = models.DateTimeField(db_column='ACCOUNTNO', blank=True, null=True)  
    ifsccode = models.DateTimeField(db_column='IFSCCODE', blank=True, null=True)  
    basicwages = models.FloatField(db_column='BasicWages', blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='DId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=10, blank=True, null=True)  

    class Meta:
        
        db_table = 'emp_new1'


class Emparrearsalarydtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    asid = models.IntegerField(db_column='ASId', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    wagestype = models.CharField(db_column='WagesType', max_length=2, blank=True, null=True)  
    basic = models.DecimalField(db_column='Basic', max_digits=18, decimal_places=2, blank=True, null=True)  
    dailywages = models.DecimalField(db_column='DailyWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    arrear = models.DecimalField(db_column='Arrear', max_digits=18, decimal_places=2, blank=True, null=True)  
    cdt = models.DateTimeField(db_column='CDt', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=50, blank=True, null=True)  
    muserid = models.CharField(db_column='MUserid', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    processstatus = models.IntegerField(db_column='ProcessStatus', blank=True, null=True)  
    processdt = models.DateTimeField(db_column='ProcessDt', blank=True, null=True)  
    processuserid = models.CharField(db_column='ProcessUserId', max_length=50, blank=True, null=True)  
    releasests = models.IntegerField(db_column='ReleaseSts', blank=True, null=True)  
    releasedt = models.DateTimeField(db_column='ReleaseDt', blank=True, null=True)  
    releaseuserid = models.CharField(db_column='ReleaseUserid', max_length=50, blank=True, null=True)  
    paystatus = models.IntegerField(db_column='PayStatus', blank=True, null=True)  
    paydt = models.DateTimeField(db_column='PayDt', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserid', max_length=50, blank=True, null=True)  

    class Meta:
        
        db_table = 'emparrearsalarydtl'


class Emparrearsalaryhdr(models.Model):
    asid = models.IntegerField(db_column='ASId', blank=True, null=True)  
    asalaryno = models.CharField(db_column='ASalaryNo', max_length=50, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='DId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=50, blank=True, null=True)  
    totalarrearsalary = models.FloatField(db_column='TotalArrearSalary', blank=True, null=True)  
    totalemp = models.IntegerField(db_column='TotalEmp', blank=True, null=True)  
    gdate = models.DateTimeField(db_column='GDate', blank=True, null=True)  
    guserid = models.CharField(db_column='GUserId', max_length=20, blank=True, null=True)  
    submitsts = models.IntegerField(db_column='SubmitSts', blank=True, null=True)  
    submitdate = models.DateTimeField(db_column='SubmitDate', blank=True, null=True)  
    submituserid = models.CharField(db_column='SubmitUserid', max_length=50, blank=True, null=True)  
    approvstatus = models.IntegerField(db_column='ApprovStatus', blank=True, null=True)  
    approvuserid = models.CharField(db_column='ApprovUserid', max_length=20, blank=True, null=True)  
    approvdate = models.DateTimeField(db_column='ApprovDate', blank=True, null=True)  
    paysts = models.IntegerField(db_column='PaySts', blank=True, null=True)  
    paydate = models.DateTimeField(db_column='PayDate', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserId', max_length=50, blank=True, null=True)  

    class Meta:
        
        db_table = 'emparrearsalaryhdr'



class Empepfarreardtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    aepfid = models.IntegerField(db_column='AEpfId', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    dailywages = models.DecimalField(db_column='DailyWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfwages = models.DecimalField(db_column='EPFWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfempper = models.FloatField(db_column='EpfEmpPer', blank=True, null=True)  
    epfemprper = models.FloatField(db_column='EpfEmprPer', blank=True, null=True)  
    epfper = models.FloatField(db_column='EpfPer', blank=True, null=True)  
    eattndays = models.FloatField(db_column='EAttnDays', blank=True, null=True)  
    epfemp = models.DecimalField(db_column='EPFEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfempr = models.DecimalField(db_column='EPFEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    epfdeposit = models.DecimalField(db_column='EPFDeposit', max_digits=18, decimal_places=2, blank=True, null=True)  
    status = models.IntegerField(db_column='Status', blank=True, null=True)  
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdt = models.DateTimeField(db_column='CDt', blank=True, null=True)  
    muserid = models.CharField(db_column='MUserid', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    processstatus = models.IntegerField(db_column='ProcessStatus', blank=True, null=True)  
    processuserid = models.CharField(db_column='ProcessUserId', max_length=20, blank=True, null=True)  
    processdt = models.DateTimeField(db_column='ProcessDt', blank=True, null=True)  
    releasests = models.IntegerField(db_column='ReleaseSts', blank=True, null=True)  
    releaseuserid = models.CharField(db_column='ReleaseUserId', max_length=20, blank=True, null=True)  
    releasedt = models.DateTimeField(db_column='ReleaseDt', blank=True, null=True)  
    paystatus = models.IntegerField(db_column='PayStatus', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserId', max_length=20, blank=True, null=True)  
    paydt = models.DateTimeField(db_column='PayDt', blank=True, null=True)  

    class Meta:
        
        db_table = 'empepfarreardtl'


class Empepfarrearhdr(models.Model):
    aepfid = models.IntegerField(db_column='AEpfId', blank=True, null=True)  
    aepfno = models.CharField(db_column='AEpfNo', max_length=50, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='DId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=50, blank=True, null=True)  
    totalepf = models.FloatField(db_column='TotalEPF', blank=True, null=True)  
    totalattn = models.FloatField(db_column='TotalAttn', blank=True, null=True)  
    totalemp = models.IntegerField(db_column='TotalEmp', blank=True, null=True)  
    gdate = models.DateTimeField(db_column='GDate', blank=True, null=True)  
    guserid = models.CharField(db_column='GUserId', max_length=20, blank=True, null=True)  
    submitsts = models.IntegerField(db_column='SubmitSts', blank=True, null=True)  
    submituserid = models.CharField(db_column='SubmitUserid', max_length=20, blank=True, null=True)  
    submitdate = models.DateTimeField(db_column='SubmitDate', blank=True, null=True)  
    approvstatus = models.IntegerField(db_column='ApprovStatus', blank=True, null=True)  
    approvuserid = models.CharField(db_column='ApprovUserid', max_length=20, blank=True, null=True)  
    approvdate = models.DateTimeField(db_column='ApprovDate', blank=True, null=True)  
    batchno = models.CharField(db_column='BatchNo', max_length=10, blank=True, null=True)  

    class Meta:
        
        db_table = 'empepfarrearhdr'


class Empepfdepositebatch(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    epfbatchno = models.CharField(db_column='EpfBatchNo', max_length=10, blank=True, null=True)  
    epfids = models.CharField(db_column='EpfIds', blank=True, null=True , max_length=20)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    batchdate = models.DateTimeField(db_column='BatchDate', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=10, blank=True, null=True)  

    class Meta:
        
        db_table = 'empepfdepositebatch'


class Empepfdepositebatch1(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    epfbatchno = models.CharField(db_column='EpfBatchNo', max_length=10, blank=True, null=True)  
    epfids = models.CharField(db_column='EpfIds', blank=True, null=True , max_length=20)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    batchdate = models.DateTimeField(db_column='BatchDate', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=10, blank=True, null=True)  

    class Meta:
        
        db_table = 'empepfdepositebatch_1'



class Empepfdtleditlog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    epfdid = models.IntegerField(db_column='EpfdId', blank=True, null=True)  
    epfid = models.IntegerField(db_column='Epfid', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    o_eattndays = models.DecimalField(db_column='O_EAttnDays', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_epfemp = models.DecimalField(db_column='O_EPFEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_epfempr = models.DecimalField(db_column='O_EPFEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_epfdeposit = models.DecimalField(db_column='O_EPFDeposit', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_eattndays = models.DecimalField(db_column='N_EAttnDays', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_epfemp = models.DecimalField(db_column='N_EPFEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_epfempr = models.DecimalField(db_column='N_EPFEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_epfdeposit = models.DecimalField(db_column='N_EPFDeposit', max_digits=18, decimal_places=2, blank=True, null=True)  
    type = models.IntegerField(db_column='Type', blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  
    dt = models.DateTimeField(db_column='Dt', blank=True, null=True)  

    class Meta:
        
        db_table = 'empepfdtleditlog'





class Empesidepositebatch(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    esibatchno = models.CharField(db_column='EsiBatchNo', max_length=10, blank=True, null=True)  
    esiids = models.CharField(db_column='EsiIds', blank=True, null=True , max_length=20)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    batchdate = models.DateTimeField(db_column='BatchDate', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=10, blank=True, null=True)  

    class Meta:
        
        db_table = 'empesidepositebatch'


class Empesidtl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    esiid = models.IntegerField(db_column='EsiId', blank=True, null=True)  
    epfid = models.IntegerField(db_column='EpfId', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    sattndays = models.FloatField(db_column='SAttnDays', blank=True, null=True)  
    dailywages = models.DecimalField(db_column='DailyWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    atnwages = models.DecimalField(db_column='AtnWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    salaryesiemp = models.DecimalField(db_column='SalaryESIEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    salaryesiempr = models.DecimalField(db_column='SalaryESIEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    salaryesi = models.DecimalField(db_column='SalaryESI', max_digits=18, decimal_places=2, blank=True, null=True)  
    esiwages = models.DecimalField(db_column='ESIWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    esiempper = models.FloatField(db_column='EsiEmpPer', blank=True, null=True)  
    esiemprper = models.FloatField(db_column='EsiEmprPer', blank=True, null=True)  
    esiper = models.FloatField(db_column='EsiPer', blank=True, null=True)  
    epfattndays = models.FloatField(db_column='EpfAttnDays', blank=True, null=True)  
    esiattndays = models.FloatField(db_column='EsiAttnDays', blank=True, null=True)  
    esiemp = models.DecimalField(db_column='EsiEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    esiempr = models.DecimalField(db_column='EsiEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    esideposit = models.DecimalField(db_column='EsiDeposit', max_digits=18, decimal_places=2, blank=True, null=True)  
    status = models.IntegerField(db_column='Status', blank=True, null=True)  
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  
    muserid = models.CharField(db_column='MUserid', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    processstatus = models.IntegerField(db_column='ProcessStatus', blank=True, null=True)  
    processuserid = models.CharField(db_column='ProcessUserId', max_length=20, blank=True, null=True)  
    processdt = models.DateTimeField(db_column='ProcessDt', blank=True, null=True)  
    releasests = models.IntegerField(db_column='ReleaseSts', blank=True, null=True)  
    releaseuserid = models.CharField(db_column='ReleaseUserId', max_length=20, blank=True, null=True)  
    releasedt = models.DateTimeField(db_column='ReleaseDt', blank=True, null=True)  
    paystatus = models.IntegerField(db_column='PayStatus', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserId', max_length=20, blank=True, null=True)  
    paydt = models.DateTimeField(db_column='PayDt', blank=True, null=True)  

    class Meta:
        
        db_table = 'empesidtl'


class Empesidtleditlog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    esidid = models.IntegerField(db_column='EsidId', blank=True, null=True)  
    esiid = models.IntegerField(db_column='Esiid', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    o_esiattndays = models.DecimalField(db_column='O_EsiAttnDays', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_esiemp = models.DecimalField(db_column='O_EsiEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_esiempr = models.DecimalField(db_column='O_EsiEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_esideposit = models.DecimalField(db_column='O_EsiDeposit', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_esiattndays = models.DecimalField(db_column='N_EsiAttnDays', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_esiemp = models.DecimalField(db_column='N_EsiEmp', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_esiempr = models.DecimalField(db_column='N_EsiEmpr', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_esideposit = models.DecimalField(db_column='N_EsiDeposit', max_digits=18, decimal_places=2, blank=True, null=True)  
    type = models.IntegerField(db_column='Type', blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  
    dt = models.DateTimeField(db_column='Dt', blank=True, null=True)  

    class Meta:
        
        db_table = 'empesidtleditlog'


class Empesihdr(models.Model):
    esiid = models.IntegerField(db_column='EsiId', blank=True, null=True)  
    esino = models.CharField(db_column='EsiNo', max_length=50, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='DId', blank=True, null=True)  
    aid = models.IntegerField(db_column='AId', blank=True, null=True)  
    sid = models.IntegerField(db_column='SId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=50, blank=True, null=True)  
    totalesi = models.FloatField(db_column='TotalESI', blank=True, null=True)  
    totalattn = models.FloatField(db_column='TotalAttn', blank=True, null=True)  
    totalemp = models.IntegerField(db_column='TotalEmp', blank=True, null=True)  
    gdate = models.DateTimeField(db_column='GDate', blank=True, null=True)  
    guserid = models.CharField(db_column='GUserId', max_length=20, blank=True, null=True)  
    submitsts = models.IntegerField(db_column='SubmitSts', blank=True, null=True)  
    submituserid = models.CharField(db_column='SubmitUserid', max_length=20, blank=True, null=True)  
    submitdate = models.DateTimeField(db_column='SubmitDate', blank=True, null=True)  
    approvstatus = models.IntegerField(db_column='ApprovStatus', blank=True, null=True)  
    approvuserid = models.CharField(db_column='ApprovUserid', max_length=20, blank=True, null=True)  
    approvdate = models.DateTimeField(db_column='ApprovDate', blank=True, null=True)  
    batchno = models.CharField(db_column='BatchNo', max_length=10, blank=True, null=True)  
    submitpaysts = models.IntegerField(db_column='SubmitPaySts', blank=True, null=True)  
    submitpayuserid = models.CharField(db_column='SubmitPayUserId', max_length=20, blank=True, null=True)  
    submitpaydate = models.DateTimeField(db_column='SubmitPayDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'empesihdr'


class Emphrnegotiation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=20, blank=True, null=True)  
    hrnegamt = models.FloatField(db_column='HRNegAmt', blank=True, null=True)  
    status = models.IntegerField(db_column='Status', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'emphrnegotiation'

class Employeemst0608(models.Model):
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=10, blank=True, null=True)  
    empname = models.CharField(db_column='EmpName', max_length=100, blank=True, null=True)  
    empfhname = models.CharField(db_column='EmpFHName', max_length=100, blank=True, null=True)  
    empdob = models.DateTimeField(db_column='EmpDob', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  
    mobileno = models.CharField(db_column='MobileNo', max_length=30, blank=True, null=True)  
    emergencyno = models.CharField(db_column='EmergencyNo', max_length=15, blank=True, null=True)  
    bloodgroup = models.CharField(db_column='BloodGroup', max_length=5, blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=15, blank=True, null=True)  
    joinningdate = models.DateTimeField(db_column='JoinningDate', blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  
    desgination = models.CharField(db_column='Desgination', max_length=100, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='Did', blank=True, null=True)  
    preaddress = models.CharField(db_column='PreAddress', max_length=150, blank=True, null=True)  
    precity = models.CharField(db_column='PreCity', max_length=50, blank=True, null=True)  
    predist = models.CharField(db_column='PreDist', max_length=50, blank=True, null=True)  
    prestate = models.CharField(db_column='PreState', max_length=50, blank=True, null=True)  
    prepin = models.CharField(db_column='PrePin', max_length=10, blank=True, null=True)  
    peraddress = models.CharField(db_column='PerAddress', max_length=150, blank=True, null=True)  
    percity = models.CharField(db_column='PerCity', max_length=50, blank=True, null=True)  
    perdist = models.CharField(db_column='PerDist', max_length=50, blank=True, null=True)  
    perstate = models.CharField(db_column='PerState', max_length=50, blank=True, null=True)  
    perpin = models.CharField(db_column='PerPin', max_length=10, blank=True, null=True)  
    unno = models.CharField(db_column='UNNo', max_length=20, blank=True, null=True)  
    aadharno = models.CharField(db_column='AadharNo', max_length=20, blank=True, null=True)  
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    accountno = models.CharField(db_column='AccountNo', max_length=50, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCode', max_length=25, blank=True, null=True)  
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    conv = models.FloatField(db_column='Conv', blank=True, null=True)  
    maxepf = models.FloatField(db_column='MaxEPF', blank=True, null=True)  
    maxesi = models.FloatField(db_column='MaxESI', blank=True, null=True)  
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  
    medical = models.FloatField(db_column='Medical', blank=True, null=True)  
    resallow = models.FloatField(db_column='ResAllow', blank=True, null=True)  
    epfno = models.CharField(db_column='EPFNo', max_length=20, blank=True, null=True)  
    esino = models.CharField(db_column='ESINo', max_length=20, blank=True, null=True)  
    wagestype = models.CharField(db_column='WagesType', max_length=2, blank=True, null=True)  
    billtype = models.CharField(db_column='Billtype', max_length=2, blank=True, null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=2, blank=True, null=True)  
    leave = models.CharField(max_length=2, blank=True, null=True)
    epf = models.CharField(db_column='EPF', max_length=2, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=2, blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    activests = models.IntegerField(db_column='ActiveSts', blank=True, null=True)  

    class Meta:
        
        db_table = 'employeemst_0608'


class Employeemst20230104(models.Model):
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=10, blank=True, null=True)  
    empname = models.CharField(db_column='EmpName', max_length=100, blank=True, null=True)  
    empfhname = models.CharField(db_column='EmpFHName', max_length=100, blank=True, null=True)  
    empdob = models.DateTimeField(db_column='EmpDob', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  
    mobileno = models.CharField(db_column='MobileNo', max_length=30, blank=True, null=True)  
    emergencyno = models.CharField(db_column='EmergencyNo', max_length=15, blank=True, null=True)  
    bloodgroup = models.CharField(db_column='BloodGroup', max_length=5, blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=15, blank=True, null=True)  
    joinningdate = models.DateTimeField(db_column='JoinningDate', blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  
    desgination = models.CharField(db_column='Desgination', max_length=100, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='Did', blank=True, null=True)  
    preaddress = models.CharField(db_column='PreAddress', max_length=150, blank=True, null=True)  
    precity = models.CharField(db_column='PreCity', max_length=50, blank=True, null=True)  
    predist = models.CharField(db_column='PreDist', max_length=50, blank=True, null=True)  
    prestate = models.CharField(db_column='PreState', max_length=50, blank=True, null=True)  
    prepin = models.CharField(db_column='PrePin', max_length=10, blank=True, null=True)  
    peraddress = models.CharField(db_column='PerAddress', max_length=150, blank=True, null=True)  
    percity = models.CharField(db_column='PerCity', max_length=50, blank=True, null=True)  
    perdist = models.CharField(db_column='PerDist', max_length=50, blank=True, null=True)  
    perstate = models.CharField(db_column='PerState', max_length=50, blank=True, null=True)  
    perpin = models.CharField(db_column='PerPin', max_length=10, blank=True, null=True)  
    unno = models.CharField(db_column='UNNo', max_length=20, blank=True, null=True)  
    aadharno = models.CharField(db_column='AadharNo', max_length=20, blank=True, null=True)  
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    accountno = models.CharField(db_column='AccountNo', max_length=50, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCode', max_length=25, blank=True, null=True)  
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    conv = models.FloatField(db_column='Conv', blank=True, null=True)  
    maxepf = models.FloatField(db_column='MaxEPF', blank=True, null=True)  
    maxesi = models.FloatField(db_column='MaxESI', blank=True, null=True)  
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  
    medical = models.FloatField(db_column='Medical', blank=True, null=True)  
    resallow = models.FloatField(db_column='ResAllow', blank=True, null=True)  
    epfno = models.CharField(db_column='EPFNo', max_length=20, blank=True, null=True)  
    esino = models.CharField(db_column='ESINo', max_length=20, blank=True, null=True)  
    wagestype = models.CharField(db_column='WagesType', max_length=2, blank=True, null=True)  
    billtype = models.CharField(db_column='Billtype', max_length=2, blank=True, null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=2, blank=True, null=True)  
    leave = models.CharField(max_length=2, blank=True, null=True)
    epf = models.CharField(db_column='EPF', max_length=2, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=2, blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    activests = models.IntegerField(db_column='ActiveSts', blank=True, null=True)  

    class Meta:
        
        db_table = 'employeemst_20230104'


class Employeemst20230105(models.Model):
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=10, blank=True, null=True)  
    empname = models.CharField(db_column='EmpName', max_length=100, blank=True, null=True)  
    empfhname = models.CharField(db_column='EmpFHName', max_length=100, blank=True, null=True)  
    empdob = models.DateTimeField(db_column='EmpDob', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  
    mobileno = models.CharField(db_column='MobileNo', max_length=30, blank=True, null=True)  
    emergencyno = models.CharField(db_column='EmergencyNo', max_length=15, blank=True, null=True)  
    bloodgroup = models.CharField(db_column='BloodGroup', max_length=5, blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=15, blank=True, null=True)  
    joinningdate = models.DateTimeField(db_column='JoinningDate', blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  
    desgination = models.CharField(db_column='Desgination', max_length=100, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='Did', blank=True, null=True)  
    preaddress = models.CharField(db_column='PreAddress', max_length=150, blank=True, null=True)  
    precity = models.CharField(db_column='PreCity', max_length=50, blank=True, null=True)  
    predist = models.CharField(db_column='PreDist', max_length=50, blank=True, null=True)  
    prestate = models.CharField(db_column='PreState', max_length=50, blank=True, null=True)  
    prepin = models.CharField(db_column='PrePin', max_length=10, blank=True, null=True)  
    peraddress = models.CharField(db_column='PerAddress', max_length=150, blank=True, null=True)  
    percity = models.CharField(db_column='PerCity', max_length=50, blank=True, null=True)  
    perdist = models.CharField(db_column='PerDist', max_length=50, blank=True, null=True)  
    perstate = models.CharField(db_column='PerState', max_length=50, blank=True, null=True)  
    perpin = models.CharField(db_column='PerPin', max_length=10, blank=True, null=True)  
    unno = models.CharField(db_column='UNNo', max_length=50, blank=True, null=True)  
    aadharno = models.CharField(db_column='AadharNo', max_length=20, blank=True, null=True)  
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    accountno = models.CharField(db_column='AccountNo', max_length=50, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCode', max_length=25, blank=True, null=True)  
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    conv = models.FloatField(db_column='Conv', blank=True, null=True)  
    maxepf = models.FloatField(db_column='MaxEPF', blank=True, null=True)  
    maxesi = models.FloatField(db_column='MaxESI', blank=True, null=True)  
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  
    medical = models.FloatField(db_column='Medical', blank=True, null=True)  
    resallow = models.FloatField(db_column='ResAllow', blank=True, null=True)  
    epfno = models.CharField(db_column='EPFNo', max_length=50, blank=True, null=True)  
    esino = models.CharField(db_column='ESINo', max_length=50, blank=True, null=True)  
    wagestype = models.CharField(db_column='WagesType', max_length=2, blank=True, null=True)  
    billtype = models.CharField(db_column='Billtype', max_length=2, blank=True, null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=2, blank=True, null=True)  
    leave = models.CharField(max_length=2, blank=True, null=True)
    epf = models.CharField(db_column='EPF', max_length=2, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=2, blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    activests = models.IntegerField(db_column='ActiveSts', blank=True, null=True)  

    class Meta:
        
        db_table = 'employeemst_20230105'


class Employeemst20230127(models.Model):
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    empcode = models.CharField(db_column='EmpCode', max_length=10, blank=True, null=True)  
    empname = models.CharField(db_column='EmpName', max_length=100, blank=True, null=True)  
    empfhname = models.CharField(db_column='EmpFHName', max_length=100, blank=True, null=True)  
    empdob = models.DateTimeField(db_column='EmpDob', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  
    mobileno = models.CharField(db_column='MobileNo', max_length=30, blank=True, null=True)  
    emergencyno = models.CharField(db_column='EmergencyNo', max_length=15, blank=True, null=True)  
    bloodgroup = models.CharField(db_column='BloodGroup', max_length=5, blank=True, null=True)  
    gender = models.CharField(db_column='Gender', max_length=15, blank=True, null=True)  
    joinningdate = models.DateTimeField(db_column='JoinningDate', blank=True, null=True)  
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  
    desgination = models.CharField(db_column='Desgination', max_length=100, blank=True, null=True)  
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='Did', blank=True, null=True)  
    preaddress = models.CharField(db_column='PreAddress', max_length=150, blank=True, null=True)  
    precity = models.CharField(db_column='PreCity', max_length=50, blank=True, null=True)  
    predist = models.CharField(db_column='PreDist', max_length=50, blank=True, null=True)  
    prestate = models.CharField(db_column='PreState', max_length=50, blank=True, null=True)  
    prepin = models.CharField(db_column='PrePin', max_length=10, blank=True, null=True)  
    peraddress = models.CharField(db_column='PerAddress', max_length=150, blank=True, null=True)  
    percity = models.CharField(db_column='PerCity', max_length=50, blank=True, null=True)  
    perdist = models.CharField(db_column='PerDist', max_length=50, blank=True, null=True)  
    perstate = models.CharField(db_column='PerState', max_length=50, blank=True, null=True)  
    perpin = models.CharField(db_column='PerPin', max_length=10, blank=True, null=True)  
    unno = models.CharField(db_column='UNNo', max_length=50, blank=True, null=True)  
    aadharno = models.CharField(db_column='AadharNo', max_length=20, blank=True, null=True)  
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  
    accountno = models.CharField(db_column='AccountNo', max_length=50, blank=True, null=True)  
    ifsccode = models.CharField(db_column='IFSCCode', max_length=25, blank=True, null=True)  
    basic = models.FloatField(db_column='Basic', blank=True, null=True)  
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    conv = models.FloatField(db_column='Conv', blank=True, null=True)  
    maxepf = models.FloatField(db_column='MaxEPF', blank=True, null=True)  
    maxesi = models.FloatField(db_column='MaxESI', blank=True, null=True)  
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  
    medical = models.FloatField(db_column='Medical', blank=True, null=True)  
    resallow = models.FloatField(db_column='ResAllow', blank=True, null=True)  
    epfno = models.CharField(db_column='EPFNo', max_length=50, blank=True, null=True)  
    esino = models.CharField(db_column='ESINo', max_length=50, blank=True, null=True)  
    wagestype = models.CharField(db_column='WagesType', max_length=2, blank=True, null=True)  
    billtype = models.CharField(db_column='Billtype', max_length=2, blank=True, null=True)  
    bonus = models.CharField(db_column='Bonus', max_length=2, blank=True, null=True)  
    leave = models.CharField(max_length=2, blank=True, null=True)
    epf = models.CharField(db_column='EPF', max_length=2, blank=True, null=True)  
    esi = models.CharField(db_column='ESI', max_length=2, blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    modifyuser = models.CharField(db_column='ModifyUser', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    activests = models.IntegerField(db_column='ActiveSts', blank=True, null=True)  

    class Meta:
        
        db_table = 'employeemst_20230127'




class Employeeslks(models.Model):
    reg_no = models.FloatField(db_column='Reg#No', blank=True, null=True)   
    sl_no_field = models.FloatField(db_column='SL NO#', blank=True, null=True)
    empcode = models.CharField(db_column='EmpCode', max_length=255, blank=True, null=True)  
    employee_name = models.CharField(db_column='Employee Name', max_length=255, blank=True, null=True)   
    father_s_name = models.CharField(db_column="Father's Name", max_length=255, blank=True, null=True)   
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)  
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  
    doj = models.DateTimeField(db_column='DOJ', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mob_no = models.CharField(db_column='Mob No', max_length=255, blank=True, null=True)   
    uan_no = models.CharField(db_column='UAN NO', max_length=255, blank=True, null=True)   
    esic_no = models.CharField(db_column='ESIC NO', max_length=255, blank=True, null=True)   
    aadhar_no = models.CharField(db_column='AADHAR NO', max_length=255, blank=True, null=True)   
    permanent_present_address = models.CharField(db_column='Permanent/Present Address', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    bank_a_c_no = models.CharField(db_column='Bank A/c No', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    dept = models.CharField(db_column='Dept', max_length=255, blank=True, null=True)  
    divison = models.CharField(db_column='Divison', max_length=255, blank=True, null=True)  
    client_site_location = models.CharField(db_column='Client/Site_location', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    district = models.CharField(db_column='DISTRICT', max_length=255, blank=True, null=True)  
    wages = models.FloatField(db_column='Wages', blank=True, null=True)  
    remarks = models.CharField(db_column='Remarks', max_length=255, blank=True, null=True)  
    relationship_manager = models.CharField(db_column='Relationship Manager', max_length=255, blank=True, null=True)   
    f27 = models.CharField(db_column='F27', max_length=255, blank=True, null=True)  

    class Meta:
        
        db_table = 'employeeslks'


class Employeeslksemp(models.Model):
    reg_no = models.FloatField(db_column='Reg#No', blank=True, null=True)   
    sl_no_field = models.FloatField(db_column='SL NO#', blank=True, null=True)
    empcode = models.CharField(db_column='EmpCode', max_length=255, blank=True, null=True)  
    employee_name = models.CharField(db_column='Employee Name', max_length=255, blank=True, null=True)   
    father_s_name = models.CharField(db_column="Father's Name", max_length=255, blank=True, null=True)   
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)  
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  
    doj = models.DateTimeField(db_column='DOJ', blank=True, null=True)  
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  
    mob_no = models.CharField(db_column='Mob No', max_length=255, blank=True, null=True)   
    uan_no = models.CharField(db_column='UAN NO', max_length=255, blank=True, null=True)   
    esic_no = models.CharField(db_column='ESIC NO', max_length=255, blank=True, null=True)   
    aadhar_no = models.CharField(db_column='AADHAR NO', max_length=255, blank=True, null=True)   
    permanent_present_address = models.CharField(db_column='Permanent/Present Address', max_length=255, blank=True, null=True)   
    bank_name = models.CharField(db_column='Bank Name', max_length=255, blank=True, null=True)   
    bank_a_c_no = models.CharField(db_column='Bank A/c No', max_length=255, blank=True, null=True)   
    ifsc_code = models.CharField(db_column='IFSC Code', max_length=255, blank=True, null=True)   
    dept = models.CharField(db_column='Dept', max_length=255, blank=True, null=True)  
    divison = models.CharField(db_column='Divison', max_length=255, blank=True, null=True)  
    client_site_location = models.CharField(db_column='Client/Site_location', max_length=255, blank=True, null=True)   
    client_code = models.CharField(db_column='Client Code', max_length=255, blank=True, null=True)   
    district = models.CharField(db_column='DISTRICT', max_length=255, blank=True, null=True)  
    wages = models.FloatField(db_column='Wages', blank=True, null=True)  
    remarks = models.CharField(db_column='Remarks', max_length=255, blank=True, null=True)  
    relationship_manager = models.CharField(db_column='Relationship Manager', max_length=255, blank=True, null=True)   

    class Meta:
        
        db_table = 'employeeslksemp'



class EmpsalarydtlDelTemp(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    sid = models.IntegerField(db_column='SId', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    attndays = models.FloatField(db_column='AttnDays', blank=True, null=True)  
    wagestype = models.CharField(db_column='WagesType', max_length=2, blank=True, null=True)  
    basic = models.DecimalField(db_column='Basic', max_digits=18, decimal_places=2, blank=True, null=True)  
    dailywages = models.DecimalField(db_column='DailyWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    atnwages = models.DecimalField(db_column='AtnWages', max_digits=18, decimal_places=2, blank=True, null=True)  
    bonus = models.DecimalField(db_column='Bonus', max_digits=18, decimal_places=2, blank=True, null=True)  
    insentive = models.DecimalField(db_column='Insentive', max_digits=18, decimal_places=2, blank=True, null=True)  
    ot = models.DecimalField(db_column='OT', max_digits=18, decimal_places=2, blank=True, null=True)  
    arrear = models.DecimalField(db_column='Arrear', max_digits=18, decimal_places=2, blank=True, null=True)  
    epf = models.DecimalField(db_column='EPF', max_digits=18, decimal_places=2, blank=True, null=True)  
    esi = models.DecimalField(db_column='ESI', max_digits=18, decimal_places=2, blank=True, null=True)  
    ptax = models.DecimalField(db_column='PTax', max_digits=18, decimal_places=2, blank=True, null=True)  
    advance = models.DecimalField(db_column='Advance', max_digits=18, decimal_places=2, blank=True, null=True)  
    uniform = models.DecimalField(db_column='Uniform', max_digits=18, decimal_places=2, blank=True, null=True)  
    others = models.DecimalField(db_column='Others', max_digits=18, decimal_places=2, blank=True, null=True)  
    loans = models.DecimalField(db_column='Loans', max_digits=18, decimal_places=2, blank=True, null=True)  
    sewacharge = models.DecimalField(db_column='SewaCharge', max_digits=18, decimal_places=2, blank=True, null=True)  
    gross = models.DecimalField(db_column='Gross', max_digits=18, decimal_places=2, blank=True, null=True)  
    netpay = models.DecimalField(db_column='NetPay', max_digits=18, decimal_places=2, blank=True, null=True)  
    emprepf = models.DecimalField(db_column='EmprEPF', max_digits=18, decimal_places=2, blank=True, null=True)  
    empresi = models.DecimalField(db_column='EmprESI', max_digits=18, decimal_places=2, blank=True, null=True)  
    muserid = models.CharField(db_column='MUserid', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    processstatus = models.IntegerField(db_column='ProcessStatus', blank=True, null=True)  
    processdt = models.DateTimeField(db_column='ProcessDt', blank=True, null=True)  
    processuserid = models.CharField(db_column='ProcessUserId', max_length=20, blank=True, null=True)  
    releasests = models.IntegerField(db_column='ReleaseSts', blank=True, null=True)  
    releasedt = models.DateTimeField(db_column='ReleaseDt', blank=True, null=True)  
    releaseuserid = models.CharField(db_column='ReleaseUserid', max_length=20, blank=True, null=True)  
    paystatus = models.IntegerField(db_column='PayStatus', blank=True, null=True)  
    paydt = models.DateTimeField(db_column='PayDt', blank=True, null=True)  
    payuserid = models.CharField(db_column='PayUserid', max_length=20, blank=True, null=True)  

    class Meta:
        
        db_table = 'empsalarydtl_del_temp'


class Empsalarydtleditlog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    sdid = models.IntegerField(db_column='SdId', blank=True, null=True)  
    sid = models.IntegerField(db_column='Sid', blank=True, null=True)  
    empid = models.IntegerField(db_column='EmpId', blank=True, null=True)  
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    o_ptax = models.DecimalField(db_column='O_PTax', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_advance = models.DecimalField(db_column='O_Advance', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_uniform = models.DecimalField(db_column='O_Uniform', max_digits=18, decimal_places=2, blank=True, null=True)  
    o_others = models.DecimalField(db_column='O_Others', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_ptax = models.DecimalField(db_column='N_PTax', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_advance = models.DecimalField(db_column='N_Advance', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_uniform = models.DecimalField(db_column='N_Uniform', max_digits=18, decimal_places=2, blank=True, null=True)  
    n_others = models.DecimalField(db_column='N_Others', max_digits=18, decimal_places=2, blank=True, null=True)  
    type = models.IntegerField(db_column='Type', blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  
    dt = models.DateTimeField(db_column='Dt', blank=True, null=True)  

    class Meta:
        
        db_table = 'empsalarydtleditlog'



class Menumst(models.Model):
    mid = models.IntegerField(db_column='Mid', blank=True, null=True)  
    menuname = models.CharField(db_column='MenuName', max_length=50, blank=True, null=True)  
    menupagepath = models.CharField(db_column='MenuPagePath', max_length=100, blank=True, null=True)  
    parentmid = models.IntegerField(db_column='ParentMId', blank=True, null=True)  
    slno = models.IntegerField(db_column='Slno', blank=True, null=True)  
    menuicon = models.CharField(db_column='MenuIcon', max_length=50, blank=True, null=True)  
    status = models.IntegerField(db_column='Status', blank=True, null=True)  
    lvl = models.IntegerField(db_column='Lvl', blank=True, null=True)  

    class Meta:
        
        db_table = 'menumst'


class Menuroleaccess(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    rid = models.IntegerField(db_column='RId', blank=True, null=True)  
    mid = models.IntegerField(db_column='MId', blank=True, null=True)  
    sts = models.IntegerField(db_column='Sts', blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    cuserid = models.CharField(db_column='CUserId', max_length=50, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  
    muserid = models.CharField(db_column='MUserId', max_length=50, blank=True, null=True)  

    class Meta:
        
        db_table = 'menuroleaccess'


class Pibilldtl(models.Model):
    bdid = models.IntegerField(db_column='BDid', blank=True, null=True)  
    bid = models.IntegerField(db_column='BId', blank=True, null=True)  
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)  
    str = models.IntegerField(db_column='Str', blank=True, null=True)  
    wages = models.FloatField(db_column='Wages', blank=True, null=True)  
    wtype = models.IntegerField(db_column='WType', blank=True, null=True)  
    qnty = models.FloatField(db_column='Qnty', blank=True, null=True)  
    total = models.FloatField(db_column='Total', blank=True, null=True)  
    sts = models.IntegerField(db_column='Sts', blank=True, null=True)  
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=50, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'pibilldtl'


class Pibillhdr(models.Model):
    bid = models.IntegerField(db_column='Bid', blank=True, null=True)  
    
    cid = models.IntegerField(db_column='CId', blank=True, null=True)  
    did = models.IntegerField(db_column='DId', blank=True, null=True)  
    
    yearmonth = models.CharField(db_column='YearMonth', max_length=10, blank=True, null=True)  
    billreffno = models.CharField(db_column='BillReffNo', max_length=20, blank=True, null=True)  
    billno = models.CharField(db_column='BillNo', max_length=50, blank=True, null=True)  
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  
    orderno = models.CharField(db_column='OrderNo', max_length=50, blank=True, null=True)  
    address1 = models.CharField(db_column='Address1', max_length=500, blank=True, null=True)  
    address2 = models.CharField(db_column='Address2', max_length=500, blank=True, null=True)  
    gross = models.FloatField(db_column='Gross', blank=True, null=True)  
    epfsts = models.IntegerField(db_column='EpfSts', blank=True, null=True)  
    epfper = models.FloatField(db_column='EpfPer', blank=True, null=True)  
    epf = models.FloatField(db_column='Epf', blank=True, null=True)  
    esists = models.IntegerField(db_column='EsiSts', blank=True, null=True)  
    esiper = models.FloatField(db_column='EsiPer', blank=True, null=True)  
    esi = models.FloatField(db_column='ESI', blank=True, null=True)  
    srvsts = models.IntegerField(db_column='SrvSts', blank=True, null=True)  
    srvon = models.IntegerField(db_column='SrvOn', blank=True, null=True)  
    srvvalue = models.FloatField(db_column='SrvValue', blank=True, null=True)  
    srvcharge = models.FloatField(db_column='SrvCharge', blank=True, null=True)  
    bonussts = models.IntegerField(db_column='BonusSts', blank=True, null=True)  
    bonus = models.FloatField(db_column='Bonus', blank=True, null=True)  
    leavests = models.IntegerField(db_column='LeaveSts', blank=True, null=True)  
    leave = models.FloatField(db_column='Leave', blank=True, null=True)  
    nfholidayssts = models.IntegerField(db_column='NFHolidaysSts', blank=True, null=True)  
    nfholidays = models.FloatField(db_column='NFHolidays', blank=True, null=True)  
    materialsts = models.IntegerField(db_column='MaterialSts', blank=True, null=True)  
    material = models.FloatField(db_column='Material', blank=True, null=True)  
    fulests = models.IntegerField(db_column='FuleSts', blank=True, null=True)  
    fule = models.FloatField(db_column='Fule', blank=True, null=True)  
    machinarysts = models.IntegerField(db_column='MachinarySts', blank=True, null=True)  
    machinary = models.FloatField(db_column='Machinary', blank=True, null=True)  
    otherssts = models.IntegerField(db_column='OthersSts', blank=True, null=True)  
    othersname = models.CharField(db_column='OthersName', max_length=50, blank=True, null=True)  
    others = models.FloatField(db_column='Others', blank=True, null=True)  
    gststs = models.IntegerField(db_column='GstSts', blank=True, null=True)  
    gstper = models.FloatField(db_column='GstPer', blank=True, null=True)  
    gston = models.CharField(db_column='GSTOn', max_length=50, blank=True, null=True)  
    gstgross = models.FloatField(db_column='GSTGross', blank=True, null=True)  
    gst = models.FloatField(db_column='GST', blank=True, null=True)  
    totalbill = models.FloatField(db_column='TotalBill', blank=True, null=True)  
    bankaccid = models.IntegerField(db_column='BankAccId', blank=True, null=True)  
    
    submit = models.IntegerField(db_column='Submit', blank=True, null=True)  
    submitdate = models.DateTimeField(db_column='SubmitDate', blank=True, null=True)  
    submituserid = models.CharField(db_column='SubmitUserId', max_length=20, blank=True, null=True)  
    
    approve = models.IntegerField(db_column='Approve', blank=True, null=True)  
    appdate = models.DateTimeField(db_column='AppDate', blank=True, null=True)  
    appuserid = models.CharField(db_column='AppUserId', max_length=20, blank=True, null=True)  
    
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'pibillhdr'


class TblError(models.Model):
    e_no = models.IntegerField(db_column='E_NO', blank=True, null=True)  
    e_proc = models.CharField(db_column='E_PROC', max_length=128, blank=True, null=True)  
    e_line = models.IntegerField(db_column='E_LINE', blank=True, null=True)  
    e_msg = models.CharField(db_column='E_MSG', max_length=4000, blank=True, null=True)  
    dt = models.DateTimeField(db_column='Dt', blank=True, null=True)  

    class Meta:
        
        db_table = 'tbl_error'







    

class Userclient(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    userid = models.CharField(db_column='UserId', max_length=20, blank=True, null=True)  
    cid = models.IntegerField(db_column='Cid', blank=True, null=True)  
    status = models.IntegerField(db_column='Status', blank=True, null=True)  
    cuserid = models.CharField(db_column='CUserId', max_length=20, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    muserid = models.CharField(db_column='MUserId', max_length=20, blank=True, null=True)  
    mdate = models.DateTimeField(auto_now=True, db_column='MDate', blank=True, null=True)  

    class Meta:
        
        db_table = 'userclient'


class Usermst(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    userid = models.CharField(db_column='UserId', max_length=15, blank=True, null=True)  
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  
    userrole = models.CharField(db_column='UserRole', max_length=50, blank=True, null=True)  
    userpsw = models.CharField(db_column='UserPsw', max_length=50, blank=True, null=True)  
    usersts = models.IntegerField(db_column='UserSts', blank=True, null=True)  
    cuser = models.CharField(db_column='CUser', max_length=50, blank=True, null=True)  
    cdate = models.DateTimeField(auto_now_add=True, db_column='Cdate', blank=True, null=True)
    llogindt = models.DateTimeField(db_column='LLoginDt', blank=True, null=True)  
    isemailverify = models.IntegerField(db_column='IsEmailVerify', blank=True, null=True)  
    bid = models.IntegerField(db_column='Bid', blank=True, null=True)  

    class Meta:
        
        db_table = 'usermst'


class Userrole(models.Model):
    rid = models.CharField(db_column='Rid', max_length=5, blank=True, null=True)  
    role = models.CharField(db_column='Role', max_length=50, blank=True, null=True)  

    class Meta:
        
        db_table = 'userrole'


