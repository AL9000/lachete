from django.contrib import admin
from sondages.models import Choix, Question


admin.AdminSite.site_header = "Administration de La Chête"


class ChoiceInline(admin.TabularInline):
    model = Choix
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'open', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)