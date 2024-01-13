from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('result/', views.result, name='result'),
    
    path('sirform/',views.sirform,name='sirform'),
    path('studentlogin/',views.studentlogin,name="studentlogin"),
    path('sign/',views.signing,name="signing"),
    

    
]

