from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib import auth

from examapp.models import Question
from loginapp.models import MyUser


# Create your views here.

def giveMePage1(request):
    return render(request,'loginapp/addition.html')



def login(request):
    
    if request.method=="GET":
        return render(request,'loginapp/login.html')
    
    else:

        userobject=auth.authenticate(username=request.POST["username"] , password=request.POST["password"])

        if(userobject.username!='admin'):

            print(connection.queries)

            print(userobject)

            print(userobject.id)

            queryset=MyUser.objects.filter(user_ptr_id=userobject.id)

            imagepath=queryset[0].imagepath

            print(queryset[0].imagepath)


        if userobject==None:
            return render(request,'loginapp/login.html',{'message':"credentials are not correct"})
        
        else:
            
            auth.login(request,userobject) # it will start session 

            queryset=Question.objects.all().values('subject').distinct()

            #queryset=Question.objects.all()

            # select distinct subject from question

            print(f"subjects from db are :- {queryset}")
            print(connection.queries)
            
            request.session["username"]=userobject.username
            request.session["score"]=0
            request.session["qindex"]=0
            request.session["answers"]={}

            if userobject.is_superuser==0:
                
                return render(request,'examapp/subject.html',{'listofdictionary':queryset,'imagepath':imagepath})
            else:
                return render(request,'examapp/admindashboard.html')




    
def saveUser(request):

    if request.method=="GET":
        
        return render(request,'loginapp/register.html')

    photo=request.FILES['photo']
    imagepath='/upload/'+photo.name

    with open('loginapp/static/upload/'+photo.name, 'wb+') as destination:  
                for byte in photo.chunks():  
                    destination.write(byte)
   

    MyUser.objects.create_user(username=request.POST["username"] , email=request.POST["email"],password=request.POST["password"],imagepath=imagepath)

    # userobject.save() # save() will save user's details in auth_user table .

    print(connection.queries)

    return render(request,'loginapp/login.html',{'message':"registration successful"})


# addition/<no1>/<no2>
# localhost:8000/loginapp/addition/10/20
def addition(request,no1,no2):
     
     answer=int(no1) + int(no2)
     
     return HttpResponse(f'{no1} + {no2}= {answer}')

# http://localhost:8000/loginapp/sum/?no1=10&no2=20

# request ==> [GET {'no1':'10' , 'no2':'20'}] request object

def sum(request):
     
     no1=request.GET["no1"] 
     no2=request.GET["no2"]
     
     answer=int(no1)+int(no2)

     return HttpResponse(f'{no1} + {no2}= {answer}')