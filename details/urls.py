from django.urls import path
from . import views
urlpatterns = [path('list/', views.show, name = 'details'),
               path('list/students',views.add_form, name = 'add_student' ),
               path('list/marks',views.add_marks, name = 'add_marks' ),
               path('list/show_mark/<int:id>',views.show_mark, name = 'show_mark' ),
               path('list/update_stu/<int:id>',views.update_stu, name = 'upd_stu' ),
               path('list/update_mark/<int:id>',views.update_mark, name = 'upd_mar' ),
               path('list/del_stu/<int:id>',views.del_student, name = 'del_stu' ),
               path('list/delete_mark/<int:id>', views.del_mark, name = 'del_mark'),
               path('delete_mark/<int:id>', views.del_mark, name = 'del_mark'),
               path('update_mark/<int:id>',views.update_mark, name = 'upd_mar' ),
               path('del_stu/<int:id>',views.del_student, name = 'del_stu' ),
               path('update_stu/<int:id>',views.update_stu, name = 'upd_stu' ),
               path('students',views.add_form, name = 'add_student' ), 
               path('marks',views.add_marks, name = 'add_marks' ),              
               path('home/',views.home, name = 'home'),
               path('', views.Form_in, name = 'Form_in'),
               path('web/', views.web, name = 'web'),
               path('Form_out/',views.Form_out, name = 'Form_out'),  
               path('json/<int:id>', views.json_view, name = 'json') ,
               path('list_json/', views.Json_show.as_view(), name = 'list_json')
               ]