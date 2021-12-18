
from django.urls import path, re_path
from blog import views

urlpatterns = [

    # The home page
    path('home', views.tester, name='home'),

 	# Upload Location
    #path('upload/csv', views.upload_csv, name='upload_csv'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

    # AWS
    path('', views.aws, name='aws'),



]
