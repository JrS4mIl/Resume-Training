from django.db import models

# Create your models here.
class AbstractModel(models.Model):
    update_date = models.DateTimeField(blank=True, auto_now=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        abstract=True
class GeneralSetting(AbstractModel):
    name=models.CharField(default='',max_length=100,blank=True)
    description=models.CharField(default='',max_length=254,blank=True)
    paramater=models.CharField(default='',max_length=254,blank=True)



    def __str__(self):
        return f'General Setting:{self.name}'

    class Meta:
        verbose_name='General Setting'
        verbose_name_plural='General Settings'
        ordering=('name',)

class ImageSetting(AbstractModel):
    name=models.CharField(default='',max_length=120,blank=True,verbose_name='Name')
    description = models.CharField(default='', max_length=254, blank=True)
    file=models.ImageField(default='',verbose_name='Image',blank=True,upload_to='images/')

    def __str__(self):
        return f'Image Setting:{self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)