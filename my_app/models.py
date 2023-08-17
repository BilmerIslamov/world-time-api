from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100,null=False,blank=False)

	class Meta:
		verbose_name = "Categoriyalar"
		verbose_name_plural = "Categoriyalar"

	def __str__(self):
		return self.name

class News(models.Model):
	title = models.CharField(max_length=250,null=False,blank=False)
	image = models.ImageField(upload_to='images/',blank=True)
	text = models.TextField()
	category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		verbose_name = "Yengliklar"
		verbose_name_plural = "Yengliklar"


	def __str__(self):
		return self.title


class Videos(models.Model):
	video_url = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)

class Post(models.Model):
	sarlavha = models.TextField()
	text = models.TextField()


	def __str__(self):
		return self.sarlavha