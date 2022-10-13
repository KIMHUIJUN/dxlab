from django.urls import path

from . import views

app_name = "insight"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detailpage/', views.detailp, name = 'detailpage'),
    path('test/',views.test, name = 'test'),
    path('end/',views.end,name = 'end'),
    path('suggestion/',views.suggestion,name = 'suggestion'),
    path('test_page',views.test_page),

]