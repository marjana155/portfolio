
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name="blogs"),
    path('<int:blog_id>', views.detail, name='detail'),
    path('<blog_category>', views.category, name='category')

]
