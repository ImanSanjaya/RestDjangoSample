from rest_framework.decorators import api_view
from rest_framework.response import Response

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

    if request.method == 'GET':
        print('KAMU HIT GET METHOD')
        return Response(courses)
    elif request.method == 'POST':
        print('KAMU HIT POST METHOD')
        return Response(courses)
    elif request.method == 'PUT':
        print('KAMU HIT PUT METHOD')
        return Response(courses)

