from django.urls import path

from sns_comment import views

app_name = 'sns_comment'

urlpatterns = [
    path('', views.SnsCommentIndexView.as_view(), name='sns_index'),
    path('detail/<int:pk>', views.SnsDetailView.as_view(), name='sns_detail'),
    path('create/', views.SnsCreateView.as_view(), name='sns_create'),
    path('update/<int:pk>', views.SnsUpdateView.as_view(), name='sns_update'),
    path('delete/<int:pk>', views.SnsDeleteView.as_view(), name='sns_delete'),
    path('comment/<int:id>', views.SnsCommentView.as_view(), name='sns_comment'),
    ]
