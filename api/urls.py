from django.urls import path
from .views import get_category,ProductView,get_all_news,Add_News_Detail,Add_Category_Detail,Category_Detail,get_category_all
from . import views


urlpatterns = [
			path('get_category/',get_category,name='get_category'),
			path('get_all_news/',get_all_news,name='get_all_news'),
			path('get_news/<int:pk>/',ProductView.as_view()),
			path('add_news/',Add_News_Detail.as_view()),
			path('add_category_detail/',Add_Category_Detail.as_view()),
			path('update_delete_category/',Category_Detail.as_view()),
			path('category/<int:category_id>/', views.get_category_all),
			path('news/<int:news_id>/', views.post_detailview, name='post_detailview'),

]