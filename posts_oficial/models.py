from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey('posts_oficial.Tag', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo