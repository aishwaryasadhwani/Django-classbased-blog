from django.contrib import admin
from blogapp.models import PostBlog,Comment
# Register your models here.
admin.site.register(PostBlog)
admin.site.register(Comment)
