from django.urls import path
from . import views
# If you want to define path, you need to bring path package
# Then we need a url for homepage, so need to import view.
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')

]
