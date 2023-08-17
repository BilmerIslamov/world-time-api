from rest_framework.generics import ListCreateAPIView  ,RetrieveUpdateDestroyAPIView
from my_app.models import Category,News,Post
from .serializers import CategorySeralizers,NewsSeralizers,PostSeralizers
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

# All categories views
@api_view(['GET'])
def get_category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer =  CategorySeralizers(category,many=True)
        return Response(serializer.data)

# All Category views and Create
class Add_Category_Detail(ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class  = CategorySeralizers

class Category_Detail(RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class  = CategorySeralizers


# All News views
@api_view(['GET'])
def get_all_news(request):
    if request.method == 'GET':
        all_news = News.objects.all()
        serializer = NewsSeralizers(all_news,many=True)
        return Response(serializer.data)

# All News views and Create
class Add_News_Detail(ListCreateAPIView):
  queryset = News.objects.all()
  serializer_class  = NewsSeralizers


# one reference belonging to a category
class ProductView(APIView):
    def get(self,request,pk):
        news = News.objects.all().filter(category=pk)
        # if no such information is found
        if news:
            serializer = NewsSeralizers(news,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        response = {
            'message': 'HTTP_404_NOT_FOUND'
        }
        return Response(response,status=status.HTTP_404_NOT_FOUND )


################################################################## Categoriyaga tegishli bo'lgan malumotlar chiqarish
@api_view(['GET'])
def get_category_all(request, category_id):
    if request.method == "GET":
        try:
            category_view = Category.objects.get(pk=category_id)
            new_view = News.objects.filter(category_id=category_id)

            category_serializer = CategorySeralizers(category_view)
            news_serializer = NewsSeralizers(new_view, many=True)

            response_data = {
                'category': category_serializer.data,
                'news_items': news_serializer.data
            }

            return Response(response_data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)

#############################################################   POST_DETAILVIEW 
@api_view(['GET'])
def post_detailview(request, news_id):
    if request.method == "GET":
        try:
            news_detail = get_object_or_404(News, pk=news_id)
            # Joriy yangilik bilan bir xil kategoriyaga tegishli boshqa yangiliklarni olish
            new_foreign = News.objects.filter(category_id=news_detail.category_id).exclude(pk=news_id)

            news_detail_serializer = NewsSeralizers(news_detail)
            news_foreign_serializer = NewsSeralizers(new_foreign, many=True)

            response_data = {
                'news_detail_serializer': news_detail_serializer.data,
                'news_foreign_serializer': news_foreign_serializer.data
            }
            return Response(response_data)
        except News.DoesNotExist:
            return Response({'error': 'Yangilik topilmadi'}, status=404)

# class View(ListCreateAPIView ):
# 	permission_classes = (permissions.IsAuthenticated,)
# 	queryset = User.objects.all()
# 	serializer_class  = UserSeralizers


# class UserDetail(RetrieveUpdateDestroyAPIView):
# 	permission_classes = (permissions.IsAuthenticated,)
# 	queryset = User.objects.all()
# 	serializer_class  = UserSeralizers


# # clientlar uchun
# class ClientView(ListCreateAPIView ):
# 	permission_classes = (permissions.IsAuthenticated,)
# 	queryset = Client.objects.all()
# 	serializer_class  = ClientSeralizers



# class ClientDetail(RetrieveUpdateDestroyAPIView):
# 	permission_classes = (permissions.IsAuthenticated,)
# 	queryset = Client.objects.all()
# 	serializer_class  = ClientSeralizers



# 	from django.views.generic import ListView
# from .models import News,Category
# from django.shortcuts import render,get_object_or_404
# from django.shortcuts import render



# class BlogListView(ListView):
#     model = News
#     template_name = 'index.html'


# def category(request,category_id):
#     string = Category.objects.get(pk=category_id)
#     string1 = News.objects.all().filter(category_id=category_id)
#     if len(string1)>0:
#         b = string1[0]
#     else:b={}
#     states = {
#         'asd': string1,
#         "st": string,
#         "b": b
#     }
#     return render(request, "category.html",states)


