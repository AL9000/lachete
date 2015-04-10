from django import forms


class VoteForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)