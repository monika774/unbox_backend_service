from django.urls import path 
from .views import  SpeedDataViewSet

urlpatterns = [ 
    path('speedlist/', SpeedDataViewSet.as_view({'get': 'get_data'}), name='speedometer-data'),
    path('speedlistatintervals/', SpeedDataViewSet.as_view({'get': 'create_data_at_intervals'}), name='speedometerinterval-data'),
] 
