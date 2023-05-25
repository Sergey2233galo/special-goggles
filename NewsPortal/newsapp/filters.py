from django_filters import (FilterSet, ModelChoiceFilter, CharFilter, DateTimeFilter, ChoiceFilter)
from django.forms import DateTimeInput
from .models import Post, Category, CATEGORY_CHOISES

class PostFilter(FilterSet):
    title = CharFilter(
        field_name= 'title',
        label='Название',
        lookup_expr='icontains',
    )
    category =ModelChoiceFilter(
        field_name='category__name',
        queryset=Category.objects.all(),
        label='Категории',
    )
    date_creation = DateTimeFilter(
        field_name='date_creation',
        label='Опубликовано после',
        lookup_expr='gt',
        widget= DateTimeInput(
            format='%d-%m-%Y',
            attrs={'type': 'datetime-local'},
            )
    )
    category_type = ChoiceFilter(
        choices=CATEGORY_CHOISES,
        label='Тип публикации'
    )

