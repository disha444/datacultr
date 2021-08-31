import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


@csrf_exempt
@api_view(['POST', 'GET'])
@permission_classes([AllowAny, ])
def find_data(request):
    if request.method == 'GET':
        name1 = request.query_params.get('name')
        print(request.query_params)
        res_data = []
        try:
            data = Employee.objects.filter(name=name1)

            length = len(data)
            print("data point available is",length)

            for i in range(length):
                user_designation = data[i].designation
                user_department = data[i].department
                user_email = data[i].email
                dict1 = {
                    "designation": user_department,
                    "department": user_designation,
                    "email": user_email
                }
                print(dict1)
                res_data.append(dict1)
        except Exception as exp:
            print(str(exp))
            return Response({"msg": "invalid request"})

        return Response({"data":res_data}, status=status.HTTP_200_OK)

    if request.method == 'POST':


        name1 = request.data.get('name')
        des1 = request.data.get('designation')
        dep1 = request.data.get('department')
        em1 = request.data.get('email')

        user = Employee.objects.create(name=name1, designation=des1, department=dep1, email=em1)
        return Response({"message":"record has been created!!"}, status=status.HTTP_201_CREATED)
