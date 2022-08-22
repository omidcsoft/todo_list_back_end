from rest_framework import routers
from .views import ToDoViewSet
from django.urls import path,include

router = routers.SimpleRouter()
router.register('todos',ToDoViewSet, basename="todo")

urlpatterns = [

   path("",include(router.urls)),
   
]