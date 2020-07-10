from django.contrib import admin
from .models import AdvUser
import datetime


class NonActivatedFilter(admin.SimpleListFilter):
    title = "Прошли активацию"
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли активацию'),
            ('three_days', 'Не прошли более 3 дней назад'),
            ('week', 'Не прошли более недели назад')
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'three_days':
            three_days_ago = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=three_days_ago)
        elif val == 'week':
            week_ago = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=week_ago)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonActivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser'),
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(AdvUser, AdvUserAdmin)
