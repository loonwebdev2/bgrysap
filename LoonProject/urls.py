


from django.conf.urls import url
from MNList import views 

from django.contrib import admin

urlpatterns = [    
    url('admin/', admin.site.urls),
    url(r'^$', views.MainPage, name='mainpage'),    
    url(r'^MNList/new$', views.new_ibrgy, name='new_ibrgy'),    
    url(r'^MNList/(\d+)/$', views.view_ibrgy, name='view_ibrgy'),    
    url(r'^MNList/(\d+)/add_info$', views.add_info, name='add_info'),]
    

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

