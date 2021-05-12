from django.db import models
from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment


User.objects.all().values('id', 'username')  - вывести всех юзеров
<QuerySet [{'id': 2, 'username': 'User1'}, {'id': 3, 'username': 'User2'}, {'id': 1, 'username': 'admin'}, {'id': 4, 'username': 'user1'}]>
User1 = User.objects.get(id=2)   - напомнить переменные
User2 = User.objects.get(id=3)

Author.objects.all().values('id', 'author')  - вывести всех авторов     
<QuerySet [{'id': 1, 'author': 2}, {'id': 2, 'author': 3}, {'id': 3, 'author': 4}]>
author1 = Author.objects.get(id=1)   - напомнить переменные
author2 = Author.objects.get(id=2)

Category.objects.all().values('id', 'category')  - вывести все категирии       
<QuerySet [{'id': 1, 'category': 'politics'}, {'id': 2, 'category': 'science'}, {'id': 3, 'category': 'sport'}, {'id': 4, 'category': 'culture'}]>
category1 = Category.objects.get(id=1)    - напомнить переменные
category2 = Category.objects.get(id=2)
category3 = Category.objects.get(id=3)
category4 = Category.objects.get(id=4)

Post.objects.all().values() - вывести все посты
Post.objects.all().values('id', 'post_type',)
<QuerySet [{'id': 1, 'author_id': 1, 'post_type': 'AR', 'post_datetime': datetime.datetime(2021, 5, 10, 13, 58, 58, 866004, tzinfo=<UTC>), 'post_title': 'Заголовок1', 'post_text': 'Текст1', 'post_rating': 0},
{'id': 2, 'author_id': 1, 'post_type': 'AR', 'post_datetime': datetime.datetime(2021, 5, 10, 15, 15, 50, 601599, tzinfo=<UTC>), 'post_title': 'Заголовок1', 'post_text': 'Текст1', 'post_rating': 0},
{'id': 3, 'author_id': 1, 'post_type': 'AR', 'post_datetime': datetime.datetime(2021, 5, 10, 15, 34, 51, 431556, tzinfo=<UTC>), 'post_title': 'Заголовок2', 'post_text': 'Текст2', 'post_rating': 0},
{'id': 4, 'author_id': 2, 'post_type': 'NW', 'post_datetime': datetime.datetime(2021, 5, 10, 15, 37, 47, 311113, tzinfo=<UTC>), 'post_title': 'Заголовок новости1', 'post_text': 'Текст новости1', 'post_rating': 0}]>  
article1 = Post.objects.get(id=1)
article2 = Post.objects.get(id=2)
article3 = Post.objects.get(id=3)
new1 = Post.objects.get(id=4)

comment1 = Comment.objects.get(id=1) - напомнить переменные
comment2 = Comment.objects.get(id=2)
comment3 = Comment.objects.get(id=3)
comment4 = Comment.objects.get(id=4)


Создание статьи должно быть таким:
article1 = Post.objects.create(author=author1, post_type='AR', post_title='Заголовок1', post_text='Текст1',)
А затем:
# article1 .PostCategory.add(category1, category2) - что-то не работает
article1.category.add(category1, category2)  - это работает :)

Создание новости
new1 = Post.objects.create(author=author2, post_type='NW', post_title='Заголовок новости1', post_text='Текст новости1',)
new1.category.add(category4)


user1 = User.objects.create(username='user1', email='user1@user1', password='user1password')
user2 = User.objects.create(username='user2', email='user2@user2', password='user2password')

author1 = Author.objects.create(author=User1)
author2 = Author.objects.create(author=User2)

category1 = Category.objects.create(category='politics')
category2 = Category.objects.create(category='science')
category3 = Category.objects.create(category='sport')
category4 = Category.objects.create(category='culture')

comment1 = Comment.objects.create(post=article1, user=User1, comment_text='Текст 1 комментария - к статье 1')
comment2 = Comment.objects.create(post=article2, user=User1, comment_text='Текст 2 комментария - к статье 2')
comment3 = Comment.objects.create(post=article2, user=User2, comment_text='Текст 3 комментария - к статье 3')
comment4 = Comment.objects.create(post=new1, user=User2, comment_text='Текст 4 комментария - к новости 1')

comment1.like()
comment1.dislike()
article1.like()
article1.dislike()
new1.like()
new1.dislike()










