from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Person
        # digunakan jika ingin memetakan field model secara spesfik
        # fields = ['name' , 'age' , 'a']
        # digunakan jika ingin memetakan secara seluruh field yang ada di dalam models
        fields = '__all__'

