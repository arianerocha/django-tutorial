# https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/index.html
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    # 'ForeignKey' significa que author está relacionado ao Usuário
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        )
    # 'Charfield' Campo de texto curto, com carcters limitado
    title = models.CharField(max_length=200)
    # 'TextField' Campo para textos longos, sem limite de caracter
    text = models.TextField()
    # 'DateTimeField' Campo de Data e Hora 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        # Os objetos serão ordenados por data de criação, do último para o primeiro
        ordering = ['-created_date']
        # Nome no singular
        verbose_name = 'Post'
        # Nome no plural
        verbose_name_plural = 'Meus Posts'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # Todo objeto salvo retorna o título
        return self.title


class Comment(models.Model):
    # campo post está relacionado ao Model Post
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # 'BooleanField' - Campo booleano, sempre será True ou False
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.name
        
class About(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        # {} format - Concatenação de String
        # https://docs.python.org/3/library/stdtypes.html#str.format
        # https://pyformat.info/#simple
        return '{}...'.format(self.bio[:100])
