from django_filters import FilterSet # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post
import django_filters
from django.forms import DateInput
 
 
# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля по которым будет фильтроваться (т.е. подбираться) информация о новостях
    
    post_datetime = django_filters.DateFilter(field_name='post_datetime', widget=DateInput(attrs={'type': 'date'}),  lookup_expr='gt', label='Позже даты')
    post_title = django_filters.CharFilter(field_name='post_title', lookup_expr='icontains', label='Заголовок')
    author_name = django_filters.CharFilter(field_name='author__author__username', lookup_expr='icontains', label='Автор')
    
#    class Meta:
#
#        model = Post
#        fields = ('post_datetime', 'post_title', 'author') 
#
#        fields = {
#            'post_datetime':['gt'],
#            'post_title': ['icontains'],
#            'author__author__username': ['icontains'],
#        }    



