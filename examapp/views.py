
from django.db import connection
from django.shortcuts import render
from examapp.models import Question, Result 
from django.contrib import auth
from django.contrib import messages




# Create your views here.def startTest(request):

def giveMePage1(request):
    return render(request,'examapp/questionmanagement.html')

def giveMePage2(request):
    return render(request,'examapp/resultanalysis.html')

def giveMePage3(request):
    return render(request,'examapp/admindashboard.html')


def search(request,pageno):

   # subject=request.GET["subject"]

    endindex=int(pageno)*3
    startindex=endindex-3

    queryset=Result.objects.filter(subject='python')[startindex:endindex]

    print(queryset)

    return render(request,'examapp/resultanalysis.html',{'results':queryset})


    


def startTest(request):

    subjectname=request.GET["subject"]

    request.session["subject"]=subjectname

    queryset=Question.objects.filter(subject=subjectname)

    questionobject=queryset[0]

    return render(request,'examapp/question.html',{'question':questionobject})


# 0  1  2
# 
def nextQuestion(request):
    
    if 'op' in request.GET:

        dictionary=request.session["answers"]

        dictionary[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["answer"],request.GET["op"]] 

        print(dictionary)

    questionlist=Question.objects.filter(subject=request.session["subject"])
    
    if(request.session["qindex"]<len(questionlist)-1):

        request.session["qindex"]=request.session["qindex"] + 1

        questionobject=questionlist[request.session["qindex"]]

        qno=questionobject.qno
        qno=str(qno)

        dictionary=request.session["answers"]

        if qno in dictionary:

            questiondetails=dictionary[qno]

            previousanswer=questiondetails[3]

        else:
            previousanswer=''

        return render(request,'examapp/question.html',{'question':questionobject,'previousanswer':previousanswer})
    
    else:

        return render(request,'examapp/question.html',{'question':questionlist[len(questionlist)-1],'message':"questions over.click on previous or end exam"})
       

#0 1 2

def previousQuestion(request):
        
    if 'op' in request.GET:

        dictionary=request.session["answers"]

        dictionary[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["answer"],request.GET["op"]] 

        print(dictionary)

    questionlist=Question.objects.filter(subject=request.session["subject"])
    
    if  request.session["qindex"]>0 :

        request.session["qindex"]=request.session["qindex"] - 1

        questionobject=questionlist[request.session["qindex"]]

        qno=questionobject.qno
        qno=str(qno)

        dictionary=request.session["answers"]

        if qno in dictionary:

            questiondetails=dictionary[qno]

            previousanswer=questiondetails[3]

        else:
            previousanswer=''

        return render(request,'examapp/question.html',{'question':questionobject,'previousanswer':previousanswer})
    
    else:

        return render(request,'examapp/question.html',  { 'question':questionlist[0]  ,  'message':"questions over.click on next or end exam" }    )
       

def endexam(request):
          
     if 'op' in request.GET:
        
        dictionary=request.session["answers"]

        dictionary[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["answer"],request.GET["op"]] 

        print(dictionary)

     dictionary=request.session["answers"]

     listoflist=dictionary.values()

     #[ ['1', 'what is module?', 'python file', 'folder'] ,  ['2', 'what is package ?', 'folder', 'folder'] ]

     for list in listoflist:
         if list[2]==list[3]:
             request.session["score"]=request.session["score"]+1
    
     finalscore=request.session["score"]
     username=request.session["username"]
     subjectname=request.session["subject"]

     Result.objects.create(username=username,score=finalscore,subject=subjectname)

     print(connection.queries)

     # create() method will create object and save it in db also

     auth.logout(request) # it will remove all keys from session

     return render(request,'examapp/score.html',{'username':username,'score':finalscore,'listoflist':listoflist})
    

def addQuestion(request):

    Question.objects.create(qno=request.GET["qno"],subject=request.GET["subject"],answer=request.GET["answer"],qtext=request.GET["qtext"],op1=request.GET["op1"],op2=request.GET["op2"],op3=request.GET["op3"],op4=request.GET["op4"])
    
    return render(request,"examapp/questionmanagement.html",{'message':'question added'})


def viewQuestion(request):
   
    question=Question.objects.get(qno=request.GET["qno"],subject=request.GET["subject"])

    print(connection.queries)

    return render(request,"examapp/questionmanagement.html",{'question':question})


def updateQuestion(request):

    question=Question.objects.filter(qno=request.GET["qno"],subject=request.GET["subject"])

    question.update(qtext=request.GET["qtext"],answer=request.GET["answer"],op1=request.GET["op1"],op2=request.GET["op2"],op3=request.GET["op3"],op4=request.GET["op4"])
    
    print(connection.queries)

    return render(request,"examapp/questionmanagement.html",{'message':"Record Updated"})


def deleteQuestion(request):

    queryset=Question.objects.filter(qno=request.GET["qno"],subject=request.GET["subject"])
    
    queryset.delete()

    print(connection.queries)

    return render(request,"examapp/questionmanagement.html",{'message':"Record Deleted"})