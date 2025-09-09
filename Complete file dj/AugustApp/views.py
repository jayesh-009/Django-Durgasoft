from django.shortcuts import render
from django.http import HttpResponse
import datetime

from AugustApp.models import Employee,Student,Stud,Movie

from AugustApp.forms import StudentForm,StudForm,MovieForm,LoginForm

from .import forms

from AugustApp.forms import*

from django.contrib.auth.decorators import login_required


# Create your views here.

def display(request):

    s="<h1>Welcome to Jayesh page here..... </h1>"
    return HttpResponse(s)

def good_morning(request):

    return HttpResponse('<h1>Frnd  good morning</h1>')

def good_afternoon(request):

    return HttpResponse('<h1>Frnd  good afternoon</h1>')

def gr_view(request):
    return HttpResponse('<h2>Have a nice day from gr view 1</h2>')

def url1(request):
    return HttpResponse('<h2>urls in app folder view 1</h2>')

def herosecond(request):

    date=datetime.datetime.now()

    my_dict={'insert_date':date}


    return render(request,'wish.html',my_dict)

def tempview(request):

    dt=datetime.datetime.now()

    name='Durga'
    roll=101
    marks=100

    my_show={'date':dt,'name':name,'roll':roll,'marks':marks}

    return render(request,'wish2.html',my_show)

def date12(request):

    date=datetime.datetime.now()

    msg='Hello Guest !!! very very good'

    h=int(date.strftime('%H'))
    if h<12:
        msg+='Morning!!!'
    elif h<16:
        msg+='Afternoon!!!'
    elif h<21:
        msg+='Evening'
    else:

        msg='Hello Guest !!! very very ood night...!!!'


    myval={'insert_date':date,'insert_msg':msg}

    return render(request,'date1.html',myval)


#Durga soft portel here.........................................................

def movies(request):

    mydict1={'head_msg':'Movies Information...',
             
             'sub_msg1':'sonali slowly getting cured..',
             'sub_msg2':'bahubali 3 is just planning...',
             'sub_msg3':'Salman khan ready to marriage',

             } 
    return render(request,'durganews.html',context=mydict1)

def sports(request):
    mydict2={
        'head_msg':'Sports Information....',

        'sub_msg1':'anushka shrama flying ',
        'sub_msg2':'virat kohli and anushka get married',
        'sub_msg3':'worst performence by india-sehwag',
    }  

    return render(request,'durganews.html',context=mydict2)

def politics(request):

    mydict3={
        'head_msg':'Politisc Information....',
        'sub_msg1':'Acche din aa gaye....',
        'sub_msg2':'Narendra modi is prime minister of india..',
        'sub_msg3':'he is a most populer character....',
    }
    return render(request,'durganews.html',mydict3)

def index(request):

    return render(request,'durgasoft.html')
#-----------------------------------------------------------------------

def empdata(request):

    emp_list=Employee.objects.order_by('eno')

    mydict4={'emp_list':emp_list}

    return render(request,'emp.html',context=mydict4)

def studdata(request):
    stud_list=Student.objects.order_by('marks')

    mydict5={'stud_list':stud_list}

    return render(request,'stud.html',context=mydict5)

#-----------------------------------------------------

def studentinput(request):

    send=False

    if request.method=='POST':
        form=StudentForm(request.POST)

        if form.is_valid():

            print("form validation success and print data")

            print('Name:',form.cleaned_data['name'])
            print('marks:',form.cleaned_data['marks'])

            send=True

    form=StudentForm()

    return render(request,'input.html',{'form':form,'send':send})

def studview(request):

    form=StudForm()
    if request.method=='POST':

        form=StudForm(request.POST)


        if form.is_valid():

            form.save()

        
    return render(request,'studview.html',{'form':form})

#movie Website

def indexview(request):
    return render(request,'index.html')


def addmovie(request):
    form=MovieForm()

    if request.method=='POST':

        form=MovieForm(request.POST)

        if form.is_valid():
            form.save()

            return indexview(request)
        
    return render(request,'addmovie.html',{'form':form})

def listmovie(request):

    movie_list=Movie.objects.all().order_by('-rating')

    return render(request,'listmovie.html',{'movie_list':movie_list})

#Cookies 

def index1(request):

    request.session.set_test_cookie()

    return HttpResponse('<h1>Index Page</h1>')  

def countview(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1

    else:
        newcount=1
    response=render(request,'count.html',{'count':newcount})

    response.set_cookie('count',newcount)
    return response

#============================================

def homeview1(request):
    form=LoginForm()

    return render(request,'home.html',{'form':form})


def datetime(request):

    name=request.GET['name']

    response=render(request,'datetime.html',{'name':name})

    response.set_cookie('name',name)

    return response

def result_view(request):

    name=request.COOKIES['name']

    datetime=datetime.datetime.now()
    mydict={'name':name,'datetime':datetime}

    return render(request,'result1.html',context=mydict)
#=====================================================================
def name_view(request):
    return render(request,'name.html')
def age_view(request):
    name=request.GET['name']

    response=render(request,'age.html',{'name':name})
    response.set_cookie('name',name)

    return response
def gf_view(request):
    age=request.GET['age']

    name=request.COOKIES['name']
    response=render(request,'gf.html',{'name':name})

    response.set_cookie('age',age)
    return response
def result_view(request):
    gfname=request.GET['gfname']

    name=request.COOKIES['name']
    age=request.COOKIES['age']

    response=render(request,'resultt.html',{'name':name,'age':age,'gfname':gfname})

    response.set_cookie('gfname',gfname)

    return response
#--------------------------------------------------------------------------
def add_item_form(request):
    form=AddItemForm()
    if request.method=='POST':

        name=request.POST['name']
        quantity=request.POST['quantity']


        request.session[name]=quantity

    return render(request,'additem.html',{'form':form})

def display_item_view(request):
    return render(request,'displayitem.html')



#exam application Authentication application
def home_page_view1(request):
    
    return render(request,'homepage1.html')
#@login_required
def login_view(request):
    return render(request,'login.html')

#@login_required
def java_exam_view(request):
    return render(request,'javaexam.html')

#@login_required
def python_exam_view(request):
    return render(request,'pythonexam.html')

#@login_required
def aptitude_exam_view(request):
    return render(request,'aptitudeexam.html')

def logout_view(request):

    return render(request,'logout.html')







    
 




    






