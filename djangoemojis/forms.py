from django import forms
from djangoemojis.models import Message

class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ('author', 'message')
		labels = {
			'author': 'Autor',
			'message': 'Mensaje'
		}