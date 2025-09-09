"""Aug2023 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from AugustApp import views as v1
from SecondApp import views as v2
#from AugustApp.views import gr_view


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('display/',v1.display),
    path('afternoon/',v1.good_afternoon),
    path('good_morning/',v1.good_morning),

    path('gr_view/',v1.gr_view),
    path('time_info/',v2.time_info_view),
    path('herosecond',v1.herosecond),
    path('tempview',v1.tempview),
    path('date12',v1.date12),

    #durga soft portal....

    path('index/',v1.index),
    path('movies/',v1.movies),
    path('sports/',v1.sports),
    path('politics/',v1.politics),

    #...........................................

    path('empdata',v1.empdata),
    path('studdata',v1.studdata),

    #forms-----------------------------------------------

    path('studentinput/',v1.studentinput),
    path('studview',v1.studview),
    #movie website

    path('indexview',v1.indexview),
    path('addmovie/',v1.addmovie),
    path('listmovie/',v1.listmovie),
    
    #-------------------------------------------------------
    path('index1',v1.index1),

    path('countview',v1.countview),

    path('homeview1',v1.homeview1),
    path('datetime2',v1.datetime),
    path('result',v1.result_view),
    #------------------------------
    path('name',v1.name_view),
    path('age',v1.age_view),
    path('gf',v1.gf_view),
    path('resultt',v1.result_view),

    #-----------------------------------
    path('additem1',v1.add_item_form),
    path('display1',v1.display_item_view),
    
    #exam application Authentication application
    path('',v1.home_page_view1),
    path('javaexam',v1.java_exam_view),
    path('pythonexam',v1.python_exam_view),
    path('aptiexam',v1.aptitude_exam_view),
    path('logout',v1.logout_view),
    path('login',v1.login_view),
    #----------------------------------------------








    


]
