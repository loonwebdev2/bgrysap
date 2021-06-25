

from django.urls import path
from django.conf.urls import url
from MNList import views 
#from updater import views

from django.contrib import admin

urlpatterns = [  
    path("update_server/", views.update, name="update"),	  
    url('admin/', admin.site.urls),
   
    #url ng 1st page   
    url(r'^$', views.MainPage, name='mainpage'),
    #url ng data 1st page   
    url(r'^new_residents$', views.new_ibrgy, name='new_ibrgy'), 
    
     
    #url ng 2nd page    
    url(r'^(\d+)/$', views.view_ibrgy, name='view_ibrgy'),
    #url ng data 2nd page      
    url(r'^(\d+)/add_info$', views.add_info, name='add_info'),
       

   
    
    #url ng 3rd page 
    url(r'^(\d+)/beneficiary$', views.view_beneficiary, name='view_beneficiary'),
    #url ng data 3rd page      
    url(r'^(\d+)/add_beneficiary$', views.add_beneficiary, name='add_beneficiary'),
    
    #url ng 4th page 		 
    url(r'^distribution$', views.view_distribution, name='view_distribution'),
    url(r'^add_distribution$', views.add_distribution, name='add_distribution'),
    
    #url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    
    url(r'^modify/(?P<id>\d+)$', views.modify, name='modify'),
    url(r'^modify/update/(?P<id>\d+)$', views.mupdate, name='mupdate'),
    
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^status$', views.s_status, name='s_status'),
    url(r'^about$', views.s_about, name='s_about'),

  #url ng 5th page 
    url(r'^status$', views.view_status, name='view_status'),
    #url ng data 5th page      
    url(r'^add_status$', views.add_status, name='add_status'),
    

]
       
    #url(r'^s_info$', views.s_info, name='s_info'),
    #url(r'^s_distribution$', views.s_distribution, name='s_distribution'),
    #url(r'^(\d+)/s_benefeciary$', views.s_benefeciary, name='s_benefeciary'),   
    #url(r'^s_status$', views.s_status, name='s_status'),]
    
    
    


'''
here the name of my app is updater so I add the import my view from there
replace updater with your app-name where you have your views.py
'''



    

'''
urlpatterns = [    
    url(r'^new$', views.new_list, name='new_list'),    
    url(r'^(\d+)/$', views.view_list, name='view_list'),   
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),]
from django.conf.urls import include, url
from MNList import views as list_views  
from MNList import urls as list_urls  
urlpatterns = [    
    url(r'^$', views.MainPage, name='mainpage'), 
    url(r'^MNList/', include(list_urls)),  ]
urlpatterns = [    
    url(r'^$', views.MainPage, name='mainpage'),    
    url(r'^MNList/new$', views.new_list, name='new_list'),    
    url(r'^MNList/(\d+)/$', views.view_list, name='view_list'),    
    url(r'^MNList/(\d+)/add_item$', views.add_item, name='add_item'),]
    
urlpatterns = [    
    url(r'^$', views.MainPage, name='mainpage'),    
    url(r'^MNList/new$', views.new_list, name='new_list'),    
    url(r'^MNList/(d.+)/$', views.view_list, name='view_list'),
]    
urlpatterns = [   
    url(r'^$', views.MainPage, name='home'),       
    url(r'^MNList/new$', views.new_list, name='new_list'),    
    url(r'^MNList/the-only-list-in-the-world/$', views.view_list, name='view_list'),]
'''
"""RloonProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


