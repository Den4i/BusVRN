from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):    # TabularInline - вариант отображения табами,
                                            # а StackedInline - отображение вниз
    model = Choice
    extra = 3                               # количество форм добавления ответов


class QuestionAdmin(admin.ModelAdmin):
    # можно разбить форму на группу полей с помощью fieldsets (название группы, словарь полей)
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),    # collapse отображает группу полей
                                                                                    # изначально скрытой
    ]
    inlines = [ChoiceInline]
    # настройка страницы списка объектов:
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # кортеж, состоящий из названий полей модели
    list_filter = ['pub_date']                                  # добавляет “Фильтр” по полю pub_date в боковой панели
    search_fields = ['question_text']                                   # добавление поиска, используется запрос LIKE

admin.site.register(Question, QuestionAdmin)
