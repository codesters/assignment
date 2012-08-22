from django.contrib import admin
from assignment.home.models import Teacher, Course, Subject, Assignment, Question, Answer, Student

class CourseAdmin(admin.ModelAdmin):
    list_display=('cname', 'session_start', 'session_end')

admin.site.register(Teacher)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
