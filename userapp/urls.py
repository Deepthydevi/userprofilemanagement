from django.urls import path
from . import views



urlpatterns = [
    path('',views.CreateProfile,name='create'),
    path('listview/',views.listdetails,name='details'),
    path('updatedetails/<int:user_id>/', views.editdetails, name='edit'),
    path('deletedetails/<int:user_id>/', views.deletedetails, name='delete')

]

