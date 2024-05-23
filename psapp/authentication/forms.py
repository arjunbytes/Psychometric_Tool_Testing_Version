from django import forms

class SurveyForm(forms.Form):
    question1 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question2 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question3 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question4 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question5 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question6 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question7 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question8 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question9 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
    question10 = forms.ChoiceField(choices=[(2, 'Yes'), (0, 'No')], widget=forms.RadioSelect)
