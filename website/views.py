from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from api.models import HeartParameter
from website.forms import HeartParameterForm
# Create your views here.

class History(View):
    template_name = 'history.html'

    def get(self, request):
        historys = HeartParameter.objects.all()
        return render(request, self.template_name, {'historys':historys})


class InputData(View):
    template_name = 'input-data.html'

    def get(self, request):
        form = HeartParameterForm()
        return render(request, self.template_name, {'form':form})
    

class PredictionResults(View):
    template_name = 'results.html'

    def get(self, request, id):
        results = get_object_or_404(HeartParameter, pk=id)
        return render(request, self.template_name, {'results':results})
    

def delete_result(request, result_id):
    result = get_object_or_404(HeartParameter, id=result_id)
    result.delete()
    return redirect('website:history')