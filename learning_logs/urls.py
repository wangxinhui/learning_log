from django.conf.urls import url
from . import views

urlpatterns =[
	# home
	url(r'^$',views.index,name='index'),
	# 显示所有主题
	url(r'^topics/$',views.topics,name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
	url(r'^new_topic/$',views.new_topic,name='new_topic'),
	url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
]

app_name='learning_logs'
