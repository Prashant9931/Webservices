from operator import itemgetter

from webapp.Linked_list import LinkedList as List


class Employee:
    def __init__(self, emp_id, emp_name, salary, location):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        self.location = location

    def add_employee(self):
        list.add_value(self)


def get_all_object():
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {'emp_id': list_data.data.emp_id, 'emp_name': list_data.data.emp_name, 'salary': list_data.data.salary,
             'location': list_data.data.location}
        data_list.append(d)
        list_data = list_data.next
    return data_list


def filter_by_id(emp_id):
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {}
        if list_data.data.emp_id == str(emp_id):
            d['emp_id'] = list_data.data.emp_id
            d['emp_name'] = list_data.data.emp_name
            d['salary'] = list_data.data.salary
            d['location'] = list_data.data.location
            data_list.append(d)
        list_data = list_data.next
    return data_list


def filter_by_name(emp_name):
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {}
        if list_data.data.emp_name == emp_name:
            d['emp_id'] = list_data.data.emp_id
            d['emp_name'] = list_data.data.emp_name
            d['salary'] = list_data.data.salary
            d['location'] = list_data.data.location
            data_list.append(d)
        list_data = list_data.next
    return data_list


def display():
    return list.get_head()


def delete_emp(emp_id):
    list.delete(emp_id)


def get_top_five():
    data=get_all_object()
    data.sort(key=itemgetter('salary'))
    return data



list = List.LinkedList()
