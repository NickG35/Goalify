from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('history', views.history, name='history'),
    path("journal/<int:journal_id>", views.entry, name='entry' ),
    path("timer/<int:timer_id>", views.timer, name='timer' )
]