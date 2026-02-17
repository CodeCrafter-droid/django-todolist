from django.shortcuts import render
from rest_framework import viewsets
from core.models import taskdata
from core.serializers import TaskSerializers
from rest_framework.permissions import IsAdminUser

# Create your views here.
class TaskAPIs(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = taskdata.objects.all()
    serializer_class = TaskSerializers


#superuser access tokens :-
#refresh :- eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3MTQzNzY3OCwiaWF0IjoxNzcxMzUxMjc4LCJqdGkiOiJkN2ZkY2I1YjIyMGM0MTExYTE3NzY0Y2U4ZGYxMWRiNCIsInVzZXJfaWQiOiIzIn0.sVGiS5YBG6NXzxgDgDnmshu3AIfPZhfDpwKiQarGAZs
# acees :- eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxMzUxNTc4LCJpYXQiOjE3NzEzNTEyNzgsImp0aSI6ImMxNzM2ZDU2NWIzNDQ0NjRhN2NhZjM1ZWJkZTYyZWUyIiwidXNlcl9pZCI6IjMifQ.HM9mj8OMsxZb3pDwFxWJ5uTBxJKJ9BoDVOuWfnzaEH8
