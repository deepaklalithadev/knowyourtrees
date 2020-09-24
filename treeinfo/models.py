from django.db import models

# Create your models here.


class treeinfo(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    sciname = models.CharField(max_length=50)
    localname1 = models.CharField(max_length=50)
    localname2 = models.CharField(max_length=50,blank=True)
    desc = models.CharField(max_length=1000)
    uses = models.CharField(max_length=500,blank=True)

    maxheight = models.FloatField(default=0)
    lifespan = models.IntegerField(default=0)
    timbervalue = models.IntegerField(default=0)
    avgtreeweight = models.IntegerField(default=0)
    matureage = models.IntegerField(default=0)

    req_soil = models.CharField(max_length=50,blank=True)
    req_temp = models.CharField(max_length=50,blank=True)
    req_water = models.CharField(max_length=50,blank=True)
    req_rain = models.CharField(max_length=50,blank=True)
    req_alt = models.CharField(max_length=50,blank=True)
    req_girth = models.CharField(max_length=50,blank=True)
    req_other = models.CharField(max_length=50,blank=True)

    treedesc = models.CharField(max_length=300,blank=True)
    treepic = models.ImageField(default='treepic.jpg',upload_to='images/')
    trunkdesc = models.CharField(max_length=300,blank=True)
    trunkpic = models.ImageField(default='trunkpic.jpg',upload_to='images/',blank=True)
    leavesdesc = models.CharField(max_length=300,blank=True)
    leavespic = models.ImageField(default='leavespic.jpg',upload_to='images/',blank=True)
    flowerdesc = models.CharField(max_length=300,blank=True)
    flowerpic = models.ImageField(default='flowerpic.jpg',upload_to='images/',blank=True)
    other1desc = models.CharField(max_length=300,blank=True)
    other1pic = models.ImageField(default='other1pic.jpg',upload_to='images/',blank=True)
    other2desc = models.CharField(max_length=300,blank=True)
    other2pic = models.ImageField(default='other2pic.jpg',upload_to='images/',blank=True)

