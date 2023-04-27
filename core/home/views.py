from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

from home.models import Person
from home.serializer import PeopleSerializer
# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

@api_view(['GET' , 'POST', 'PUT'])
def index(request):

    courses = {
        'course_name' : 'Python',
        'learn' : ['Flask', 'Django', 'Tornado', 'FastApi'],
        'course_provider' : 'Sitektif Learning Center'
    }

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM home_person")
        my_objects1 = cursor.fetchall()

    # with connection.cursor() as ambil_data:
    #     ambil_data.execute("SELECT * FROM django_migrations")
    #     my_objects2 = ambil_data.fetchall()


    if request.method == 'GET':
        # (hit kesini -> http://127.0.0.1:8000/api/index?search=Vinka)
        # print(request.GET.get('search'))
        print('KAMU HIT GET METHOD')
        return Response(my_objects1)
    elif request.method == 'POST':
        # (hit kesini -> http://127.0.0.1:8000/api/index/)
        data = request.data
        print('*****')
        print(data)
        print('*****')
        print('KAMU HIT POST METHOD')
        return Response(courses)
    elif request.method == 'PUT':
        # (hit kesini -> http://127.0.0.1:8000/api/index/)
        print('KAMU HIT PUT METHOD')
        return Response(courses)
    


@api_view(['GET' , 'POST' , 'PUT' , 'PATCH', 'DELETE'])
def person(request):

    if request.method == 'GET':
        # (hit kesini -> http://127.0.0.1:8000/api/person?search=Vinka)
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs , many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT': 
        data = request.data
        objs = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(objs, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH': 
        data = request.data
        objs = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(objs, data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'DELETE': 
        data = request.data
        objs = Person.objects.get(id = data['id'])
        objs.delete()
        return Response({'message' : 'person deleted'})