    

from django.shortcuts import render
from . import views
import matplotlib.pyplot as plt
from tkinter import messagebox
import re
from django.contrib import messages
import smtplib
from django.http import*
from datetime import datetime
from MCA.models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def reg(req):
	return render(req,'register.html')


def reg1(req):
    name=req.POST.get('Uname')
    pwd=req.POST.get('Pwd')
    Email=req.POST.get('Email')
    phone=req.POST.get('PNum')
    Adhar=req.POST.get('AD')
    Image=req.POST.get('img')
    x=register1(name=name,email=Email,password=pwd,phno=phone,adharno=Adhar,Image=Image)
    x.save()
    return render(req,"register.html",{'msg':'Registerd sucessfully'})

def index(req):
    return render(req,'index.html')




def userindex(req,proid):
    x = register1.objects.get(name=req.session['id'])
    print("--"*20)
    print(x.name)
    print("--"*20)
    protask=report1.objects.filter(user_id=proid)
    print(protask)
    return render(req,'userinfo.html',{'list1':x,'protask':protask})

def logout(req):
    return render(req,"register.html",{'error':"you have logged out"})


def login11(req):
    Name=req.POST.get('name')
    pwd=req.POST.get('pwd')

    ulist=register1.objects.all().values()
    uname_list=[]
    for i in ulist:
        
        Password=register1.objects.get(name=Name)
        if(Password.password==pwd):
            x=register1.objects.all()
            req.session['id']=Name
            list1=x.values()
            m = register1.objects.get(name=req.session['id'])
            print(m.name)
            return render(req,'userinfo.html',{'list1':m})
        else:
            return render(req,'register.html',{"error":"inccorect usernmae and password"})
            



def login1(req):
    return render(req,'admin.html')

def admin11(req):
    Name=req.POST.get('name')
    pwd=req.POST.get('pwds')

    ulist=admin1.objects.all().values()
    uname_list=[]
    for i in ulist:
        
        Password1=admin1.objects.get(username=Name)
        if(Password1.password==pwd):
            x=register1.objects.all()
            y=x.values()
            
            
            return render(req,'dash.html' ,{'use':y})
        else:
            return render(req,'admin.html',{"error":"inccorect usernmae and password"})


def profile(req):
    x = register1.objects.get(name=req.session['id'])
    print("--"*20)
    print(x.name)
    print("--"*20)
    return render(req,"profile.html",{"list1":x})

'''def sendmail(req):
    return render(req,'Mail.html')
 
def dash(req):
    x=pho4.objects.all()
    y=pho4.objects.count()
    file1=x.values()

    return render(req,'dash.html',{"file1":file1,"y":y})'''


'''def smtp_sendmail(email,subject,body,file):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("karthiks7520@gmail.com","hkdjkldoqehkrvow")

    message=f"subject:{subject}\n\n{body}\n\n{file}"
    server.sendmail("karthiks7520@gmail.com",email,message)
    server.quit()
    print("mail sent")'''



# Create your views here.







def profile1(request,issueid):
    issuedetails=issue1.objects.get(id=issueid)
    return render(request,'verify.html',{'details':issuedetails})


def useD(req):
    x=register1.objects.all()
    y=x.values()
    return render(req,'dash.html',{'use':y})

def pdf(req):
    x=register1.objects.all()
    y=x.values()
    return render(req,'pdf.html',{'use':y})
def sav(req):
    uid=req.POST.get('mp')
    Sug=req.POST.get('su')
    Mol=req.POST.get('mo')
    Fil=req.POST.get('fi')
    Bagg=req.POST.get('ba')
    Stra=req.POST.get('st')
    Top=req.POST.get('topp')
    Tott=req.POST.get('to')
    date=req.POST.get('d')
    edate=req.POST.get('edd')
    tt=req.POST.get('ttt')
    x=report1(sugar=Sug,molass=Mol,filt=Fil,baga=Bagg,straw=Stra,tops=Top,total=Tott,user_id=uid,dt=date,ed=edate,tton=tt)
    x.save()
    y=report1.objects.all()
    z=y.values()
    return render(req,"storepdf.html",{'msg':'Saved sucessfully','z':z})

def pd(req):
    y=report1.objects.all()
    z=y.values()
    return render(req,'storepdf.html',{'z':z})

def preview(req,show):
    aa=report1.objects.get(id=show)
    mm=aa.user_id
    kk= register1.objects.get(id=mm)
    return render(req,'printpdf.html',{'pdf1':aa,'nam':kk})

def pre(req,show1):
    x = register1.objects.get(name=req.session['id'])
    bb=report1.objects.get(id=show1)
    return render(req,'Userindex.html',{'pdf2':bb,'list1':x})

def mail(req):
    Ename=req.POST.get('ename')
    idd=req.POST.get('useid1') 
    idd=str(idd)
    print(idd)
    a="C:/Users/user/Downloads"+'/'+idd+'.pdf'
    print(a)
    body = '''Hello,This is the body of the Sugarcane report.'''
    sender = 'agritrack2023@gmail.com'
    password = 'qskafzbiunczvmug'
    receiver = Ename  
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Report for your sugarcane'
     
    message.attach(MIMEText(body, 'plain')) 
    pdfname = a
    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')
     
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())
     
    # enconding the binary into base64
    encoders.encode_base64(payload)
     
    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)
     
    #use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)
     
    #enable security
    session.starttls()
     
    #login with mail_id and password
    session.login(sender, password)
     
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent')
    return render(req, 'printpdf.html',{'msg1':'Mail sent sucessfully'})




