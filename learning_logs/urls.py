from django.conf.urls import url
from . import views

urlpatterns =[
	# home
	url(r'^$',views.index,name='index'),
	# 显示所有主题
	url(r'^topics/$',views.topics,name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topics'),
	url(r'^new_topics/$',views.new_topic,name='new_topics'),
]

app_name='learning_logs'
