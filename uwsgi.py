import sys  
import os  
  
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  
sys.path.append('/home/mingluku')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'mingluku.settings'  
  
import django.core.handlers.wsgi  
  
application = django.core.handlers.wsgi.WSGIHandler()  
