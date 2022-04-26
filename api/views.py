# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import GeeksSerializer
from rest_framework.response import Response
from dermacupid.models import User
from rest_framework.views import APIView


# create a viewset
# class GeeksViewSet(viewsets.ModelViewSet):
#     # define queryset
#     queryset = User.objects.all()
#
#     # specify serializer to be used
#     serializer_class = GeeksSerializer

class GeeksViewSet(APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        queryset = User.objects.all()
        return Response(queryset)
