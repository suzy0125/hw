from .models import Post,Product
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','body')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title','body','pr')