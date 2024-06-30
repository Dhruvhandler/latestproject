"""
URL configuration for Data_Science project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from DataApp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('base', views.base),
    path('nav', views.nav),
    path('indexpage', views.indexpage, name="indexpage"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('aitools', views.aitools, name="aitools"),
    path('detailedaitools/<str:name>', views.detailedaitools, name="detailedaitools"),
    path('chat/', views.chat, name="chat"),
    path('footer', views.footer),
    path('allfaq', views.allfaq, name="allfaq"),
    path('contactus', views.contact, name="contactus"),
    path('maps', views.maps, name="maps"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('profile', views.profile, name="profile"),
     path('editprofile', views.editprofile, name="editprofile"),
    path('register', views.register, name="register"),
     path('register1', views.register1, name="register1"),
    path('changepassword', views.change , name="changepassword"),
    path('review', views.reviews,name="reviews"),
    path('allvideos', views.allvideo, name="allvideos"),
    path('forgetpassword', views.forget, name="forgetpassword"),
    path('allarticles', views.allarticle, name="allarticle"),
    path('livenews', views.livenews, name="livenews"),
    path('jobsearching', views.jobsearching, name="jobsearching"),
     path('allinitiative', views.allinitiative, name="allinitiative"),
     path('detailedarticle/<int:id>', views.detailarticle, name="detailedarticle"),
    path('helpandsupport', views.helpandsupport, name="helpandsupport"),
    path('sidebar', views.sidebar),
    path('md1',views.md1, name="md1"),
    path('md2',views.md2, name="md2"),
    path('md3', views.md3, name="md3"),
    path('md4', views.md4, name="md4"),
    path('md5', views.md5, name="md5"),
    path('md6', views.md6, name="md6"),
    path('heading1', views.heading1, name="heading1"),
    path('md11', views.md11, name="md11"),
    path('md12', views.md12, name="md12"),
    path('md13', views.md13, name="md13"),
    path('md14', views.md14, name="md14"),
    path('md15', views.md15, name="md15"),
    path('md16', views.md16, name="md16"),
    path('md17', views.md17, name="md17"),
    path('md21', views.md21, name="md21"),
    path('md22', views.md22, name="md22"),
    path('md23', views.md23, name="md23"),
    path('md24', views.md24, name="md24"),
    path('md25', views.md25, name="md25"),
    path('md26', views.md26, name="md26"),
    path('md31', views.md31, name="md31"),
    path('md32', views.md32, name="md32"),
    path('md33', views.md33, name="md33"),
    path('md34', views.md34, name="md34"),
    path('md35', views.md35, name="md35"),
    path('md36', views.md36, name="md36"),
    path('heading2', views.heading2, name="heading2"),
    path('heading3', views.heading3,name="heading3"),
    path('heading4', views.heading4,name="heading4"),
    path('detailarticle<int:id>',views.detailarticle,name='detailarticle'),
    path('jobprediction', views.jobprediction,name="jobprediction"),
    path('cumulatativebillsprediction', views.cumulatativebillsprediction,name="cumulatativebillsprediction"),
    path('newlyfundedAIcompanies', views.newlyfundedAIcompanies,name="newlyfundedAIcompanies"),
    path('expenseprediction', views.expenseprediction,name="expenseprediction"),
    ]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

