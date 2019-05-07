from django.urls import path,include
from . import views


urlpatterns=[
   
    path('myprofile/', views.myprofile, name="myprofile"),
    path('detail/<int:detail_id>', views.detail, name="detail"),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),
    path('create_competition', views.create_competition, name='create_competition'),
    path('create_event', views.create_event, name='create_event'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('delete/<int:del_detail_id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name='update'),
    #path('page1/<int:detail_id>', views.page1, name="page1"),
    
    # path('login/', views.login, name='login'),

]
