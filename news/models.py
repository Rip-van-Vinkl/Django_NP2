from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    
    author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя автора')
    author_rating = models.IntegerField(default=0, verbose_name='Рейтинг автора')
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
    def __str__(self):
        return self.author


    def update_rating(self):

        author_posts = Post.objects.filter(author=self.id, post_type='articles') 

        author_posts_sum_rating = 0
        for post in author_posts:
            author_posts_sum_rating += post.post_rating * 3

        author_comments_sum_rating = 0
        for comment in Comment.objects.filter(user=self.author):
            author_comments_sum_rating += comment.comment_rating

        author_posts_comments_sum_rating = 0
        for authorPostsRating in Comment.objects.filter(post=author_posts.id):
            author_posts_comments_sum_rating += authorPostsRating

        self.author_rating = author_posts_sum_rating + author_comments_sum_rating + author_posts_comments_sum_rating
        self.save()

class Category(models.Model):
    
    category = models.CharField(max_length=40, unique=True, default='...')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.category


class Post(models.Model):
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    news = 'NW'
    articles = 'AR'

    TYPE = [
        (news, 'news'),
        (articles, 'articles'),

    ]

    post_type = models.CharField(max_length=2, choices=TYPE)

    post_datetime = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0.0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return str(self.post_text[0:125], '...')


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self):
        return self.post


class PostCategory(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    comment_text = models.TextField()
    comment_datetime = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
    def __str__(self):
        return self.post