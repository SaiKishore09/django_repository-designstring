from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import users
from . serializers import userserializers

class userlist(APIView):

    def get(self,request):
        user1=users.objects.all()
        serializer=userserializers(user1,many=True)
        return Response(serializer.data)

