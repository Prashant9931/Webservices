from django.contrib import admin
from django.urls import path
from webapp.views import EmpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp_api/', EmpView.as_view(), name="call")

]
