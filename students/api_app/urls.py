from django.urls import path
from .views import result, resultUpdate

urlpatterns = [
    path('stu/', result.as_view()),
    path('stu1/<int:stu_id>', resultUpdate.as_view()),
    
]