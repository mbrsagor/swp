from django.forms import ModelForm, DateTimeInput
from portal.models.profile import Profile


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        read_only_fields = ('user',)
        fields = (
            'name', 'father_name', 'mother_name', 'board_roll', 'cgpa', 'gender',
            'date_of_birth', 'ssc_passing_year', 'hsc_passing_year',
        )

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }

            self.fields['date_of_birth'].widget = DateTimeInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': field,
                'type': 'date'
            })
            self.fields['ssc_passing_year'].widget = DateTimeInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': field,
                'type': 'date'
            })
            self.fields['hsc_passing_year'].widget = DateTimeInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': field,
                'type': 'date'
            })
