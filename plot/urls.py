from django.urls import path

from plot import views

app_name = 'plot'
urlpatterns = [
    path('', views.PlotIndexView.as_view(), name='plot_index'),
    # path('show/', views.PlotShowView.as_view(), name='plot_show'),
    ]
