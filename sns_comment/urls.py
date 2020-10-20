from django.urls import path

from sns_comment import views

app_name = 'sns_comment'

urlpatterns = [
    path('', views.SnsCommentIndexView.as_view(), name='sns_comment_index'),
    path('detail/<int:pk>', views.SnsCommentDetailView.as_view(), name='sns_comment_detail'),
    path('create/', views.SnsCommentCreateView.as_view(), name='sns_comment_create'),
    path('update/<int:pk>', views.SnsCommentUpdateView.as_view(), name='sns_comment_update'),
    path('delete/<int:pk>', views.SnsCommentDeleteView.as_view(), name='sns_comment_delete'),
    ]
