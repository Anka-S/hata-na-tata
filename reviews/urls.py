from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_view, name='reviews'),
    path('review/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
      path('review/delete/<int:review_id>/', views.review_delete, name='review_delete'),
]