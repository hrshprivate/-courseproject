
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('mono/<int:item_id>', views.mono, name='mono'),
    path('delete/<int:task_id>', views.delete_task, name='delete'),
    path('profile', views.profile, name='profile'),
    path('password-change', views.PasswordsChangeView.as_view(template_name='testApp/password-change.html'), name='password_change'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('chattwo', views.chattwo, name='chattwo'),
    path('getcheckview', views.getcheckview, name='getcheckview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('deleteuser/<int:chat_id>', views.DeleteChatUser, name='deleteuser')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

