#coding=utf8
"""mingluku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import include
from django.conf.urls import url
#from django.contrib import admin
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from minglu import views
from django.views.static import  serve
import xadmin                 # 添加该行
 

#xadmin.autodiscover()     # 添加该行
      
#from xadmin.plugins import xversion    # 添加该行
 
#xversion.registe_models()
#xversion.register_models()
#xversion.registe_models()                    # 添加该行

#admin.autodiscover()
#urlpatterns = [
#    #url(r'^admin/', include(admin.site.urls)),
##    # Notice this line
#]

urlpatterns = [
    #url(r'^$', 'minglu.views.showindex',name='showindex'),  #老版本语法
    #url(r'^admin/doc/', admindocs.urls),
    #url(r'^admin/', admin.site.urls), #cssmlk88666
    #url(r'^xadmin/', xadmin.site.urls),            # 添加该行
    
    url(r'^$', views.showindex),
    url(r'^qiye/$', views.show),
    url(r'^geti/$', views.showgeti),
    url(r'^zhuxiao/$', views.showzhuxiao),
    url(r'^sheli/$', views.showsheli),
    url(r'^qyxx$', views.showqyxx),     
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),  
    url(r'^exportcsv/$', views.exportCSV),
    url(r'^query/$', views.querydata),

]


