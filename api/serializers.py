# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from dermacupid.models import User


# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = User
        fields = ('phoneno',)