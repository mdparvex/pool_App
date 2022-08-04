from django.forms import ModelForm

from .models import Poll

class CreateForm(ModelForm):
	
	class Meta:
		model = Poll
		fields = ['question', 'option1', 'option2', 'option3']