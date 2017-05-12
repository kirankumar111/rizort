from django.db import models
from django.conf import settings



# class Pool(models.Model):
# 	active=LitBooleanField(editable=True)
#     pool_name = models.CharField(max_length=200)
#     pool_id = models.IntegerField(max_length=200)

# class DrawingRoom(models.Model):
# 	active=LitBooleanField(editable=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     swimming_pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
#     room_id = models.IntegerField(max_length=200)

# class BeachResort(models.Model):
# 	active=LitBooleanField(editable=True)
#     swimming_pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
#     drawing_room = models.ForeignKey(DrawingRoom, on_delete=models.CASCADE)
#     rizort_id = models.IntegerField(max_length=200)
#     arrival_dt = LitDateTimeField(auto_now=True, editable=False)
#     dept_dt = LitDateTimeField(auto_now=True, editable=False)

class Relationship(models.Model):
    node_1  = models.ForeignKey(Nodes, on_delete=models.CASCADE)
    node_2 = models.ForeignKey(Nodes, on_delete=models.CASCADE)

class Nodes(models.Model):
    node_name = models.CharField(max_length=200)
    node_links = models.ManyToMany(Relationship)

		
# Create your models here.
