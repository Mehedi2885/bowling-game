from django.db import models

# Create your models here.


class Frames(models.Model):
    player_name = models.CharField(default="Player", max_length=150, unique=True)
    frame1_first = models.CharField(default=0, max_length=10,blank=True, null=True)
    frame1_second = models.CharField(default=0, max_length=10,blank=True, null=True)
    frame2_first = models.CharField(default=0, max_length=10,blank=True, null=True)
    frame2_second = models.CharField(default=0, max_length=10,blank=True, null=True)
    frame3_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame3_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame4_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame4_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame5_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame5_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame6_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame6_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame7_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame7_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame8_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame8_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame9_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame9_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame10_first = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame10_second = models.CharField(default=0, max_length=10, blank=True, null=True)
    frame10_bonus = models.CharField(default=0, max_length=10, blank=True, null=True)
    total_score = models.IntegerField(blank=True, default=0, null=True)
    all_frame_score = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.player_name
