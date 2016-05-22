"""
	:author: David Casado Martínez <dcsasadomartinez@gmail.com>
	Ejemplo para crear mensajes con emojis en Django.
	Se utiliza el proyecto http://ellekasai.github.io/twemoji-awesome/ para generar los emojis en el código html.
	Más información en http://buhoprogramador.com
"""

from django.db import models
from django.utils.html import escape


# lista de emojis. La clave es el nombre del emoji en el mensaje. El valor es el nombre de la clase css
# Visita http://www.emoji-cheat-sheet.com/ para ver todo los emojis disponibles.
EMOJIS = {
	'heart': 'heart',
	'sparkles': 'sparkles',
	'hatching_chick': 'hatching-chick',
	'smile': 'smile',
	'hushed': 'hushed',
	'angry': 'angry',
	'zzz': 'zzz',
	'poop': 'poop',
	'dancer': 'dancer',
	'alien': 'alien'
}


def transform_message(text):
	# Función que transforma el código `:emoji-name:` en código html con el emoji seleccionado.

	# Escapamos los caracteres html del texto. Para poder utilizar el texto con seguridad en las plantillas.
	text = escape(text)

	# Transformamos los saltos de lineas en etiquetas <br>
	text = text.replace('\r\n', '<br>').replace('\n', '<br>').replace('\r', '<br>')

	# Accedemos al diccionario EMOJIS y reemplazamos las coincidencias del texto por el código html.
	for name, classname in EMOJIS.items():
		text = text.replace(':%s:' % name, '<span class="twa twa-lg twa-%s"></span>' % classname)

	return text


class Message(models.Model):
	"""
		Modelo para los mensajes que vamos a crear.
	"""

	class Meta:
		# Nombre del modelo
		verbose_name = 'Mensaje'
		# Nombre del modelo en plural.
		verbose_name_plural = 'Mensajes'

	# Cadena con el author del mensaje.
	author = models.CharField(max_length=40)
	# Texto del mensaje sin transformar. Se utilizará si se quieren hacer modificaciones en el mensaje.
	message = models.TextField()
	# Texto del mensaje ya transformado. Será el que se muestre al público.
	message_parsed = models.TextField()
	# Fecha de la creación del mensaje
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message[:100]

	def save(self, *args, **kwargs):
		# Antes de guardar el mensaje en la BD.
		# Se transforma el texto del mensaje y se guarda en `self.messaged_parsed`

		self.message_parsed = transform_message(self.message)
		super(Message, self).save(*args, **kwargs)
