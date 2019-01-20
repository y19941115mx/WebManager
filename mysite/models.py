from django.db import models
from datetime import datetime

# Create your models here.


class Banner(models.Model):
    type_choices = (
        (0, '首页轮播图'),
        (1, '活动轮播图')
    )
    type = models.IntegerField('轮播图类型', choices=type_choices)
    desc = models.CharField('轮播图描述', default="", max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return Banner.type_choices[self.type][1]