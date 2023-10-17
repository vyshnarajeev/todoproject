from django .urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
 #   path('details',views.details,name="details")
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbvhome/',views.Tasklistview.as_view(),name="cbvhome"),
    path('details/<int:pk>/',views.TaskDetailView.as_view(),name="details"),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name="cbvupdate"),
]