from django.shortcuts import render, redirect
from djangoemojis.models import Message, EMOJIS
from djangoemojis.forms import MessageForm


def index_view(request):
	messages = Message.objects.all().order_by('-created')
	emojis = [{'classname': cln, 'name': name} for name, cln in EMOJIS.items()]

	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('djangoemojis:index')

	else:
		form = MessageForm()

	return render(request, 'twa-index.html', {'form': form, 'messages': messages, 'emojis': emojis})
