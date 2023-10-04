from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.Home,name="Home"),
    path('python/',views.python,name="python"),
    path('java/',views.java,name="java"),
    path('mern/',views.mern,name="mern"),
    path("python_n/",views.pythonnotes,name="python_n"),
    path("java_n/",views.javanotes,name="java_n"),
    path("mern_n/",views.mernnotes,name="mern_n"),

]