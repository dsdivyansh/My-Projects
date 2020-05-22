"""Blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog import views as v1
from django.contrib.auth import authenticate
from django.conf import settings

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',v1.base_view),
    path('home/',v1.Home_view,name='home'),
    path('PostBlog/',v1.PostBlog_view),
    path('Viewasblog/',v1.post_list_view),
    path('SignupForm/',v1.SignupForm_view),
    path('<int:pk>',v1.Post_Detail.as_view()),
    path('abc/<int:pk>',v1.Post_Detail_Crud.as_view()),
    # path('admin_blog/',v1.Admin_blog),
    path('my_post/',v1.My_post),
    # path('comment/',v1.post_detail),
    path('delete/<int:pk>',v1.delete_view.as_view()),
    path('post/<int:pk>/comment/', v1.add_comment_to_post, name='add_comment_to_post'),
    path('postdetail/',v1.post_detail_view,name='post_detail'),
    path('update/<int:pk>',v1.update_view.as_view()),
    # path('post/<int:pk>/comment/', v1.add_comment_to_post, name='add_comment_to_post'),

]
