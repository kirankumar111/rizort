from django.shortcuts import render
from farm_rizort.forms import NodeForm,RelationshipForm
from farm_rizort.models import Nodes,Relationship
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
import json

@csrf_protect
def index(request):
    Form = NodeForm()
    if request.method == 'GET':
        form = NodeForm()
    else:
    	form = NodeForm(request.POST)
    	if form.is_valid():
            form.save()
            return HttpResponseRedirect('node_links')
        else:
        	return form
    return render(request, 'rizort_graph.html', {'node_form': Form,'link_form':RelationshipForm})

@csrf_protect
def node_links(request):
    Form = RelationshipForm()
    if request.method == 'GET':
        Form = RelationshipForm()
    else:
    	form = RelationshipForm(request.POST)
    	if form.is_valid():
            form.save()
            return HttpResponseRedirect('node_links')
        else:
        	return form
    return render(request, 'link_nodes.html', {'link_form':RelationshipForm})

@csrf_protect
def draw_graph(request):
    data = {}
    objNodes = list(Nodes.objects.values())
    objLinks = Relationship.objects.all()
    values = ['node_1_id', 'node_2_id']
    objLinks_new =  list(objLinks.values(*values))
    data1 = json.dumps(objNodes)#serializers.serialize("json", objNodes)
    data2 = json.dumps(objLinks_new)
    data['nodes'] = data1
    data['links'] = data2
    return HttpResponse(json.dumps(data),content_type='application/json')
# Create your views here.
