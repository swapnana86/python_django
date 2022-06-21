from django.urls import path

from todoapp import views

urlpatterns = [

    path('', views.add, name="add"),
    # path('details', views.details, name="details"),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('cbgvhome/', views.TasklistviewGen.as_view(), name='cbgvhome'),
    path('cbgvdetail/<int:pk>/', views.TaskdetailviewGen.as_view(), name='cbgvdetail'),
    path('cbgvupdate/<int:pk>/', views.TaskupdateviewGen.as_view(), name='cbgvupdate'),
    path('cbgvdelete/<int:pk>/', views.TaskdeleteviewGen.as_view(), name='cbgvdelete'),
]
