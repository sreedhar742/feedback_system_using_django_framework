from django.contrib import admin

# Register your models here.
from .models import Question, Choice,Sir,Student,Registration

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = "Feedback Admin"
admin.site.site_title = "Feedback Admin Area"
admin.site.index_title = "Welcome to the Feedback Admin Area"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)




admin.site.register(Sir)
admin.site.register(Student)

admin.site.register(Registration)