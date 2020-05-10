from django.shortcuts import render
from testApp.models import hydjobs
# Create your views here.
def home(request):
    return render(request,'testApp/home.html')

def hydjobsinfo(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/hydjobs.html',context=my_dict)
