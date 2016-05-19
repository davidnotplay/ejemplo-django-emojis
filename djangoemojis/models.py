from django.db import models
from django.utils.html import escape


EMOJIS = {
	'heart': 'heart',
	'sparkles': 'sparkles',
	'hatching_chick': 'hatching-chick',
	'smile': 'smile',
	'hushed': 'hushed',
	'angry': 'angry',
	'zzz': 'zzz',
	'collision': 'collision',
	'dancer': 'dancer',
	'alien': 'alien'
}


def parse_twa(text):
	text = escape(text)
	for name, classname in EMOJIS.items():
		text = text.replace(':%s:' % name, '<span class="twa twa-lg twa-%s"></span>' % classname)

	return text


class Message(models.Model):
	author = models.CharField(max_length=40)
	message = models.TextField()
	message_parsed = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def str__(self):
		return self.message[:100]

	def save(self, *args, **kwargs):
		self.message_parsed = parse_twa(self.message)
		super(Message, self).save(*args, **kwargs)
