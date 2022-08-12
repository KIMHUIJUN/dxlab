from django.urls import path

from . import views

app_name = "insight"

urlpatterns = [
    path('', views.index, name = 'index'),
<<<<<<< HEAD
    path('detail/',views.detail,),
    path('test/',views.test),
=======
    path('detailpage/', views.detailp, name = 'detailpage'),
    path('test',views.test, name = 'test'),
>>>>>>> 8d2afae291b76b797b57cac3ee668f26e954357f
]