"""
1. (Optional) Move to project dir
2. Create 'urls.py'
3. Register this Django App in the projects's urls.py file
4. Register this Django App in settings.py 'INSTALLED_APPS'
"""
from django.urls import path
from mysite.tasks import views

urlpatterns = [
 path('', views.index)
]
