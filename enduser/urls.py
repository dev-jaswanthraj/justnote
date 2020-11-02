from django.contrib.auth.models import AnonymousUser
from django.urls import path
from .views import (
    home,
    sign_up, 
    login_page,
    logout_page,
    para,
    create_para, todo_done,
    update,
    delete_note,
    check_box,
    todo_done, 
    todo_del,
    post_view,
    home_user,
    search
)

urlpatterns = [
    path('', home, name = 'home'),
    path('home/', home_user, name='home_user'),
    path('signup/', sign_up, name = 'signup'),
    path('login/', login_page, name = 'login'),
    path('logout/', logout_page, name='logout'),
    path('paragraph/<int:id>/', para, name='para'),
    path('create/<int:id>/', create_para, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete_note, name = 'delete'),
    path('todo/<int:id>', check_box, name='checkbox'),
    path('done/<int:id>', todo_done, name='todo_done'),
    path('todo_delete/<int:id>', todo_del, name='todo_del'),
    path('post_view/<int:id>',post_view, name = 'post_view'),
    path('search/', search, name='search')
]