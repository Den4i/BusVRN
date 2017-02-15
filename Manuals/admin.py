from django.contrib import admin

# Register your models here.

from .models import Project, Route, ProjRouts, Object


class ObjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основные данные',               {'fields': ['name', 'project', 'route']}),
        ('Последние данные', {'fields': ['last_time', 'last_lat', 'last_lon', 'last_speed']}),
        ('Остальные данные',  {'fields': ['phone', 'year_release', 'date_inserted']}),
    ]

    #list_display = ('upper_case_name',)
    list_filter = ('name', )

    #def upper_case_name(self, obj):
    #     return ("%s %s" % (obj.name, obj.project)).upper()
    # upper_case_name.short_description = 'Name'

admin.site.register((Project, Route, ProjRouts))

admin.site.register(Object, ObjectAdmin)
