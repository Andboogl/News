"""Models"""

from os.path import splitext
from datetime import datetime
from django.db import models


def get_image_path(instance, filename) -> str:
    """Get image path"""
    return f"{datetime.now()}{splitext(filename)[1]}"


# Create your models here.
class News(models.Model):
    """News model"""
    image = models.ImageField(
        verbose_name="Зображення", upload_to=get_image_path,
        blank=True, null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    text = models.TextField(verbose_name="Текст")

    class Meta:
        db_table = "news"
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self) -> str:
        if self.image:
            return "Новина з зображенням"

        else:
            return "Новина без зображення"
