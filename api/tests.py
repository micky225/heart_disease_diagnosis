from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import HeartParameter
import json

class HeartApiTests(APITestCase):

    def setUp(self):
        self.heart_param = HeartParameter.objects.create(
            age=55, sex=1, chest_pain_type=3, resting_blood_pressure=140, 
            serum_cholesterol=250, fasting_blood_sugar_level=0, resting_electrocardiographoc_results=1, 
            maximum_heart_rate=160, exercise_induced_agina=0, st_depression=2.3, 
            slope=2, number_of_major_vessels=0, thallium_stress_test_results=3
        )


    def test_get_heart_parameters(self):
        url = reverse('heart-api') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_post_heart_parameter(self):

        url = reverse('heart-api')
        data = {
            "age": 55,
            "sex": 1,
            "chest_pain_type": 3,
            "resting_blood_pressure": 140,
            "serum_cholesterol": 233,
            "fasting_blood_sugar_level": 0,
            "resting_electrocardiographoc_results": 1,
            "maximum_heart_rate": 150,
            "exercise_induced_agina": 0,
            "st_depression": 2.3,
            "slope": 0,
            "number_of_major_vessels": 0,
            "thallium_stress_test_results": 2
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

