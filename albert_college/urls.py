from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('student', views.StudentViewset)

urlpatterns = [
    path('class', views.classroom_list),
    path('class/<int:id>', views.classroom_detail),
    path('parents', views.parent_list),
    path('parents/<int:id>', views.parent_detail),
    path('', include(router.urls)), 

]
