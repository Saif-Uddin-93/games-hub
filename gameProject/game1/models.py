from django.db import models

GENRES = (
    ("RPG", "Role-Playing Game"),
    ("FPS", "First Person Shooter"),
    ("TBS", "Turn  Based Strategy"),
)

# Create your models here.
class GameLink(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    genre = models.CharField(choices=GENRES,max_length=3)
    description = models.TextField(max_length=500)