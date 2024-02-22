from django import forms

from django import forms
from company.models import Employee
from company.models import Employee, Team

class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=50)
    salary=forms.IntegerField()
    title=forms.CharField(max_length=50)
    team=forms.ChoiceField(choices=[(team.pk,team.pk)for team in Team.objects.all()],required=False)
    # team_name=forms.CharField(max_length=30)
    # manager=forms.CharField(max_length=30)



class EmployeeForm2(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
# class TeamForm(forms.ModelForm):
#     class Meta:
#         model = Team
#         fields = ['name','manager']
