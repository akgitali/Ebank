from django.shortcuts import render
from . models import Account
import random
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    return render(request,"index.html")

def createaccount(request):
    return render(request,"createaccount.html")
    
def create(request):
    acno=''
    for i in range(6):
        acno=acno+str(random.randint(1,9))
    acno=int(acno) 
    name=request.POST['name']
    address=request.POST['address']
    contectno=request.POST['contectno']
    email=request.POST['email']
    panno=request.POST['panno']
    aadharno=request.POST['aadharno']
    balance=request.POST['balance']
    password=request.POST['password']
    ac=Account(
        acno=acno,
        name=name,
        address=address,
        contectno=contectno,
        email=email,
        panno=panno,
        aadharno=aadharno,
        balance=balance,
        password=password
    )
    ac.save()
    msg="Your account no is =  "+str(acno)
    return render(request,"index.html",{'msg':msg})
   
def login(request):
    return render(request,"login.html")
   
def logcode(request):
    acno=request.POST['acno']
    password=request.POST['password']
    operation=request.POST['operation']
    msg=''
    try:
        obj=Account.objects.get(acno=acno,password=password)
        if operation=='Deposit':
            acno=obj.acno
            request.session['acno']=acno
            return render(request,"Deposit.html")
        elif operation=='Withdraw':
            acno=obj.acno
            request.session['acno']=acno
            return render(request,"Withdraw.html")
        elif operation=='Transfer':
            acno=obj.acno
            request.session['acno']=acno
            return render(request,"transfer.html")
        elif operation=='Enquiry':
            balance=obj.balance
            msg="You current balance :"+str(balance)
            return render(request,"index.html",{'msg':msg})            
    except ObjectDoesNotExist:
        msg='Invalid Account No.'
    except  ValueError:
        msg='Please given values'
    return render(request,"login.html",{'msg':msg})

def depositamt(request):
    try:    
        amt=int(request.POST['amt'])
        obj=Account.objects.get(acno=request.session['acno'])
        balance=obj.balance
        balance=balance+amt
        acno=obj.acno
        Account.objects.filter(pk=acno).update(balance=balance)
        msg="Amount is credited"
        request.session['acno']=None
    except ValueError:
        msg="Enter Amount"
        return render(request,"Deposit.html",{'msg':msg})        
    return render(request,"index.html",{'msg':msg})

def withdrawamt(request):
    try:
        amt=int(request.POST['amt'])
        obj=Account.objects.get(acno=request.session['acno'])
        balance=obj.balance
        msg=''
        if balance<amt:
            msg='insufisiante balance'
            return render(request,"index.html",{'msg':msg})
        balance=balance-amt
        acno=obj.acno
        Account.objects.filter(pk=acno).update(balance=balance)
        msg="Amount is debited"
        request.session['acno']=None
    except ValueError:
        msg="Enter Amount"
        return render(request,"Withdraw.html",{'msg':msg})        
    return render(request,"index.html",{'msg':msg})
    

def transferamt(request):
    try:
        bcno=request.POST['bcno']
        amt=int(request.POST['amt'])
        msg=''
        try:
            obj2=Account.objects.get(acno=bcno)
            obj1=Account.objects.get(acno=request.session['acno'])
            balance1=obj1.balance
            if balance1<amt:
                msg=msg+'Insufficient balance'
                return render(request,"index.html",{'msg':msg})
            elif obj1==obj2:
                msg='No such Match Account'
                return render(request,"transfer.html",{'msg':msg})
            balance1=balance1-amt
            balance2=obj2.balance
            balance2=balance2+amt
            Account.objects.filter(pk=obj1.acno).update(balance=balance1)
            Account.objects.filter(pk=obj2.acno).update(balance=balance2)
            msg=msg+"Fund transfered"
            return render(request,"index.html",{'msg':msg})
    
        except ObjectDoesNotExist:
            msg=msg+'Benificiary account is invailed'
    except ValueError:
        msg="fill the from"
        return render(request,"transfer.html",{'msg':msg})
    return render(request,"index.html",{'msg':msg})

    
    
    
    
    
    
    
    
    
    