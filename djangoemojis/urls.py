from django.conf.urls import url

# import pygmentstest.views as views
import djangoemojis.views as views

urlpatterns = [
	url(r'^$', views.index_view, name='index')
]
