from django.urls import path
import views
app_name = 'Flights'

urlpatterns = [
    path('', views.index, name='index')
]
 
