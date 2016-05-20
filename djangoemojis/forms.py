"""
	:author: David Casado Martínez <dcsasadomartinez@gmail.com>
	Ejemplo para crear mensajes con emojis en Django.
	Se utiliza el proyecto http://ellekasai.github.io/twemoji-awesome/ para generar los emojis en el código html.
	Más información en http://buhoprogramador.com
"""
from django import forms
from djangoemojis.models import Message


class MessageForm(forms.ModelForm):
	""" Formulario basado en el modelo Message. Será el que los usuarios utilicen para insertar su mensaje.
	"""

	class Meta:
		# Nombre del modelo.
		model = Message
		# Campos del modelo que vamos a mostrar en el formulario.
		fields = ('author', 'message')
		# Etiqueta `label` para esos campos.
		labels = {
			'author': 'Autor',
			'message': 'Mensaje'
		}
