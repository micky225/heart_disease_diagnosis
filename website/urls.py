from django.urls import path
from website.views import *

app_name = 'website'


urlpatterns = [
    path('', History.as_view(), name='history'),
    path('input-data/', InputData.as_view(), name='input-data'),
    path('prediction-results/<str:id>/', PredictionResults.as_view(), name='results'),
    path("delete-results/<str:result_id>/", delete_result, name="delete-result"),
]
