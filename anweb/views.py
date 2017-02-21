from django.shortcuts import render
# Create your views here.
from event import allevent
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_http_methods
from anweb.models import Group
from django.forms.models import model_to_dict
from django.core import serializers
from util import toJSON
import json
@require_http_methods(["GET","POST"])
def index(request):
    #return HttpResponse('this is test result')
    return render(request, 'index.html',{})


@require_http_methods(["GET","POST"])
def Index(request):
    #servicer_list=Servicer.objects.all().order_by('id')
    return render(request, 'index.html',{
                                   #      'servicer':encoder.toJSON(servicer_list[0]),
                                         })

@require_http_methods(["GET",])
def get_group_list(request):
    a=Group.objects.all()
    list=[]
    for i in a:
        list.append(toJSON(i))
    print(list)
    return HttpResponse(json.dumps({
            'group_list':list
        }))