from django import forms
from mptt_hierarchy.models import File
from mptt.forms import TreeNodeChoiceField


class FileAddForm(forms.Form):
    name = forms.CharField(max_length=75)
    parent = TreeNodeChoiceField(queryset=File.objects.all())
