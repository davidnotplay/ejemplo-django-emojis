from django.shortcuts import render, redirect
from djangoemojis.models import Message, EMOJIS
from djangoemojis.forms import MessageForm


def index_view(request):
	""" Vista del índice de la aplicación. """

	# Extraemos todos los mensajes.
	messages = Message.objects.all().order_by('-created')
	# Extremos los emojis del diccionario `EMOJIS` para mostrarlos en la plantilla.
	emojis = [{'classname': cln, 'name': name} for name, cln in EMOJIS.items()]

	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			# Guardamos los datos del formulario y redireccionamos al índice.
			form.save()
			return redirect('djangoemojis:index')

	else:
		form = MessageForm()

	return render(request, 'djangoemojis/index.html', {'form': form, 'messages': messages, 'emojis': emojis})
