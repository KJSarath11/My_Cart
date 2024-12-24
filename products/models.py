from django.db import models

#! Product Model
class Products(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,"Live"),(DELETE,"Delete"))
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to="media/")
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)#automatic date 
    updated_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
