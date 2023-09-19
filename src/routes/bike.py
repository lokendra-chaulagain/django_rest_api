from django.urls import path
from ..repositories.bike import BikeViewset


urlpatterns = [
    path('bike/', BikeViewset.as_view()),
    path('bike/<int:id>', BikeViewset.as_view())
]
