from rest_framework import serializers
from my_app.models import Category, News, Post, Videos

class CategorySeralizers(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__' 


class NewsSeralizers(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = '__all__'


class PostSeralizers(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'

class VideoSeralizers(serializers.ModelSerializer):
	class Meta:
		model = Videos
		fields = '__all__'