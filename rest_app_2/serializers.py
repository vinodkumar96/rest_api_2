from rest_framework import serializers
#from rest_framework.serializers import Serializer

class CommentSerializer (serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=100)
    created = serializers.DateTimeField()
