from django import forms
from .models import Complaint,Student

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"

    def save(self, commit=True):
    	complaint = super().save(commit=False)
    	if commit:
    		complaint.save()
    	return complaint


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def save(self, commit=True):
    	student = super().save(commit=False)
    	if commit:
    		student.save()
    	return student
