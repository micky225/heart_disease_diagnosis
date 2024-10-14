from django import forms
from api.models import HeartParameter


class HeartParameterForm(forms.ModelForm):

    class Meta:
        model = HeartParameter
        fields = [
            'age','sex','chest_pain_type','resting_blood_pressure',
            'serum_cholesterol','fasting_blood_sugar_level',
            'resting_electrocardiographoc_results',
            'maximum_heart_rate','exercise_induced_agina',
            'st_depression','slope','number_of_major_vessels',
            'thallium_stress_test_results',
            ]
        

    age = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Age of the patient in years',
                'class':'form-control form-control-alternative'
            }
        )
    )  

    sex = forms.ChoiceField(
        choices=HeartParameter.SEX,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-alternative',
            }
        )
    )

    chest_pain_type = forms.ChoiceField(
        choices=HeartParameter.CHEST_PAIN_TYPE,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-alternative',
            }
        )
    )

    resting_blood_pressure = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Resting blood pressure in mm Hg',
                'class':'form-control form-control-alternative'
            }
        )
    )

    serum_cholesterol = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Serum cholesterol in mg/dl',
                'class':'form-control form-control-alternative'
            }
        )
    )

    fasting_blood_sugar_level = forms.ChoiceField(
        choices=HeartParameter.FASTING_BLOOD_SUGAR_LEVEL,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-alternative',
            }
        )
    )

    resting_electrocardiographoc_results = forms.ChoiceField(
        choices=HeartParameter.RESTING_ELECTROCARDIOGRAPHOC_RESULTS,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-alternative',
            }
        )
    )

    maximum_heart_rate = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Maximum heart rate achieved during a stress test',
                'class':'form-control form-control-alternative'
            }
        )
    )   

    exercise_induced_agina = forms.ChoiceField(
        choices=HeartParameter.EXERCISE_INDUCED_AGINA,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-alternative',
            }
        )
    )  

    st_depression = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Induced by exercise relative to rest',
                'class':'form-control form-control-alternative'
            }
        )
    ) 


    slope = forms.ChoiceField(
        choices=HeartParameter.SLOPE,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-alternative',
            }
        )
    )

    number_of_major_vessels = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'(0-4) colored by fluoroscopy',
                'class':'form-control form-control-alternative'
            }
        )
    )

    thallium_stress_test_results = forms.ChoiceField(
        choices=HeartParameter.THALLIUM_STRESS_TEST_RESULTS,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-alternative',
            }
        )
    )