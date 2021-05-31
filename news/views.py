from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm # импортируем нашу форму

from django.core.paginator import Paginator

import datetime


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.order_by('-id')
    paginate_by = 5 # поставим постраничный вывод в один элемент

    form_class = PostForm # добавляем форм класс, чтобы получать доступ к форме через метод POST


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = len(Post.objects.all())
        context['time_now'] = datetime.datetime.now()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра

        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) # создаём новую форму, забиваем в неё данные из POST запроса 
 
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()
 
        return super().get(request, *args, **kwargs) # отправляем пользователя обратно на GET-запрос.


class SearchNews(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    queryset = Post.objects.order_by('-id')


    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # вписываем наш фильтр в контекст
        context['filter'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


# дженерик для получения деталей о товаре
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html'  # название шаблона будет product.html
    context_object_name = 'new'  # название объекта. в нём будет


# дженерик для получения деталей о товаре
# class ProductDetailView(DetailView):
#    template_name = 'sample_app/product_detail.html'
#    queryset = Product.objects.all()



# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    # permission_required = ('NewsPaper.add_post')
    template_name = 'add_post.html'
    form_class = PostForm


# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    # permission_required = ('NewsPaper.edit_post')
    template_name = 'add_post.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'delete_post.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'new'  # название объекта. в нём будет