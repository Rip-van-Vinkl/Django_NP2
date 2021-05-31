from django.urls import path
from .views import PostList, PostDetail, SearchNews, PostCreateView, PostDeleteView, PostUpdateView # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', PostList.as_view()),  # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view()),
    path('search', SearchNews.as_view()),
    path('add/', PostCreateView.as_view()), # Ссылка на создание товара

    path('<int:pk>/edit/', PostUpdateView.as_view()),
    path('edit/<int:pk>', PostUpdateView.as_view()),
    
    path('<int:pk>/delete/', PostDeleteView.as_view()),
    path('delete/<int:pk>', PostDeleteView.as_view()),
]
