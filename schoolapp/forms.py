# from django import forms


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['course'].queryset = Course.objects.none()

#     #     if 'department' in self.data:
#     #         try:
#     #             department_id = int(self.data.get('department'))
#     #             self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
#     #         except (ValueError, TypeError):
#     #             pass

from django import forms

from .models import Student, Department, Course , Material


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')