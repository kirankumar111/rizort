from django.db import models
from django.conf import settings



# class Pool(models.Model):
#     active=models.BooleanField(default=True)
#     pool_name = models.CharField(max_length=200)
#     pool_id = models.IntegerField
    
# class DrawingRoom(models.Model):
#     active=models.BooleanField(default=True)
#     swimming_pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
#     drawing_room = models.CharField(max_length=200)
#     room_id = models.IntegerField
    
# class BeachResort(models.Model):
#     active=models.BooleanField(default=True)
#     swimming_pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
#     drawing_room = models.ForeignKey(DrawingRoom, on_delete=models.CASCADE)
#     rizort_id = models.IntegerField
#     arrival_dt = models.DateTimeField(auto_now=True, editable=False)
#     dept_dt = models.DateTimeField(auto_now=True, editable=False)


class Nodes(models.Model):
    node_cd = models.CharField(max_length=200,primary_key=True)
    node_name = models.CharField(max_length=200,unique=True)
    def save(self, **kwargs):
        super(Nodes, self).save(**kwargs)

class Relationship(models.Model):
    node_1  = models.ForeignKey(Nodes,to_field='node_name',on_delete=models.CASCADE, related_name="start_node")
    node_2 = models.ForeignKey(Nodes,to_field='node_name',on_delete=models.CASCADE, related_name="end_node")
    link_name = models.CharField(max_length=50)
    def save(self, **kwargs):
        super(Relationship, self).save(**kwargs)


# Create your models here.
