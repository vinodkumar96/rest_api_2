from django.shortcuts import render
from .serializers import CommentSerializer
from datetime import datetime
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
class Comment:
    def __init__(self,email,content,created=None):
        self.email=email
        self.content=content
        self.created=created or datetime.now()
#1st way-- json format
# def myapi (request):
#     comment=Comment(email="vinodkumar@gmail.com",content="this is the testing of api")
#     serializer=CommentSerializer(comment)
#     return HttpResponse(JSONRenderer().render(serializer.data))   #,content_type="application/json"

#2nd way-- text format

def myapi(request):
    comment1 = Comment('vinod@gmail.com','this is test 1')
    comment2 = Comment(email='kumar@gmail.com', content='this is test 2')
    comment3 = Comment(email='venkata@gmail.com', content='this is test 3')
    c=[comment1,comment2,comment3]
    serializer=CommentSerializer(c,many=True)
    return HttpResponse(JSONRenderer().render(serializer.data),content_type="text/html")