from django import forms
from insight.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:

        model = Question
        fields = ['answer']

