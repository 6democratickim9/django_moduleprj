
from django.db import models
from django.db.models import F


class it_news(models.Model):
    title = models.CharField(max_length=100,unique=True)
    time = models.CharField(max_length=100)
    preview = models.CharField(max_length=500,unique=True)

    def update_result(self):
        obj = it_news.objects.create(val=100)
        it_news.objects.filter(pk=obj.pk).update(val=F('val')+1)
        obj.refresh_from_db()
        self.assertEqual(obj.val,101)
