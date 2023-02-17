from django.urls import path 

from .views import add_attendence, addstudent, attendence, changestatics, statistics, studentdetails, studentlist, studentmenu,total,today

urlpatterns = [
        path("attendence",attendence),
        path("total",total),
        path("today",today),
        path("addstudent",addstudent),
        path("student",studentlist),
        path("details/<int:id>",studentdetails),
        path("smenu/<int:id>",studentmenu),
        path("statistics/<int:id>",statistics),
        path("changes/<int:id>/<int:attri>/<int:val>",changestatics),
        path("addattendence/<int:id>/<int:val>/<str:date>",add_attendence)
        ]