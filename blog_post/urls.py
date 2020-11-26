from django.urls import path
from .views import *
urlpatterns = [
	path('post_details/',post_details, name='post_details'),
	path('post_add/',post_add, name='post_add'),
	path('<int:id>/post_edit/',post_edit, name='post_edit'),
	path('<int:id>/post_delete/',post_delete, name='post_delete'),
	path('<int:id>/post_wise_details/',post_wise_details, name='post_wise_details'),
	path('<int:id>/comment_add/',comment_add, name='comment_add'),
	path('<int:id>/comment_edit/',comment_edit, name='comment_edit'),
]
