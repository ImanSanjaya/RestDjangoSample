from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

@api_view(['GET'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'learn' : ['Flask', 'Django', 'Tornado', 'FastApi'],
        'course_provider' : 'Sitektif Learning Center'
    }
    return Response(courses)