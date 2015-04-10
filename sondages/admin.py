from django.contrib import admin
from sondages.models import Choix, Question


admin.AdminSite.site_header = "Administration de La Chête"


class ChoiceInline(admin.TabularInline):
    model = Choix
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['question_text', 'slug', 'open']}),
        ('Information date', {'fields': ['pub_date']}),
    ]
    prepopulated_fields = {'slug': ('question_text',)}
    inlines = [ChoiceInline]
    list_display = ('question_text', 'open', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)