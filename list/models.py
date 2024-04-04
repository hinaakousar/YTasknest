from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=100)

class List(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Item(models.Model):
    content = models.TextField()
    description = models.TextField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)        
