from django.forms import ModelForm, Textarea
from django import forms
from farm_rizort.models import Nodes,Relationship

class NodeForm(ModelForm):
    node_name = forms.CharField()
    node_cd = forms.CharField()
    class Meta:
        model = Nodes
        fields = ['node_cd','node_name']
        widgets = {
            'node_name': Textarea(),
            'node_cd': Textarea(),
        }
        labels = {
            'node_name': 'Node Name',
            'node_cd': 'Node Code',
        }

class RelationshipForm(ModelForm):
    # node_1 = forms.ChoiceField()
    # node_2 = forms.ChoiceField()
    link_name = forms.CharField()

    class Meta:
        model = Relationship
        fields = ['node_1', 'node_2','link_name']
        labels = {
            'node_1': 'Start Node',
            'node_2': 'End Node',
            'link_name': 'Link Name',
        }