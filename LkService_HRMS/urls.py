
from django.contrib import admin
from django.urls import path , include
from HRMS import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/' , views.admin_dashboard , name="admin_dashboard"),
    path('' , views.admin_login , name="admin_login"),
    path('admin_logout_view' , views.admin_logout_view , name="admin_logout_view"),
    path('admin_dashboard_old' , views.admin_dashboard_old , name="admin_dashboard_old"),
    
    path('LKService/' , include("HRMS.urls"))
]
