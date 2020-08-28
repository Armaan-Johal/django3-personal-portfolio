
from django.urls import path
import blog.views

app_name = 'blog'

urlpatterns = [
    path('', blog.views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', blog.views.detail, name='detail'),
]
