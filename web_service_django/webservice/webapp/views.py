from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Employee
from . import models
import json
from .serializers import EmployeeSerializers


class EmpView(APIView):

    def get(self, request):
        params = request.GET.keys()
        if not params:
            data = models.get_all_object()
            # data_json=EmployeeSerializers(data)
            return HttpResponse(json.dumps(data))
        else:
            filter_query = list(params)[0]
            if filter_query == 'emp_id':
                emp_id = request.GET.get(filter_query)
                data = models.filter_by_id(emp_id)
                return HttpResponse(json.dumps(data))

            elif filter_query == 'emp_name':
                emp_name = request.GET.get(filter_query)
                data = models.filter_by_name(emp_name)
                return HttpResponse(json.dumps(data))

            else:
                data=models.get_top_five()
                return HttpResponse(json.dumps(data))

    def post(self, request):
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        # Create your models here.
        emp_obj = Employee(emp_id, emp_name, salary, location)
        emp_obj.add_employee()

        return HttpResponse("data_inserted")

    def delete(self, request):
        emp_id = request.POST.get('emp_id')
        models.delete_emp(emp_id)

        return HttpResponse("deleted")

