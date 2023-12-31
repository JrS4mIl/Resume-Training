from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from resume.custom_storages import DocumentStorage,ImageSettingStorage
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
    file=models.ImageField(default='',verbose_name='Image',blank=True,storage=ImageSettingStorage())

    def __str__(self):
        return f'Image Setting:{self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)

class Skill(AbstractModel):
    order=models.IntegerField(default='0',verbose_name='Order')
    name=models.CharField(default='',max_length=120,blank=True,verbose_name='Name')
    percentage=models.IntegerField(default=50,verbose_name='Percentage',validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return f'Skill:{self.name}'

    class Meta:
        verbose_name='Skill'
        verbose_name_plural='Skills'
        ordering=('order',)

class Experience(AbstractModel):
    company_name=models.CharField(default='',max_length=120,blank=True,verbose_name='Company Name')
    job_title=models.CharField(default='',max_length=120,blank=True,verbose_name='Job Title')
    job_location=models.CharField(default='',max_length=120,blank=True,verbose_name='Jop Location')
    start_date=models.DateField()
    end_date=models.DateField(default='',blank=True,null=True,verbose_name='End Date')

    def __str__(self):
        return f'Experience:{self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('start_date',)


class Education(AbstractModel):
    school_name=models.CharField(default='',max_length=120,blank=True,verbose_name='School Name')
    major=models.CharField(default='',max_length=120,blank=True,verbose_name='Major')
    departman=models.CharField(default='',max_length=120,blank=True,verbose_name='Departman')
    start_date=models.DateField()
    end_date=models.DateField(default='',blank=True,null=True,verbose_name='End Date')

    def __str__(self):
        return f'Education:{self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('start_date',)

class SosyalMedia(AbstractModel):
    order = models.IntegerField(default='0', verbose_name='Order')
    link=models.URLField(default='',max_length=200,verbose_name='Link',blank=True)
    icon=models.CharField(default='',max_length=200,verbose_name='Icon',blank=True)

    def __str__(self):
        return f'SosyalMedia: {self.link}'

    class Meta:
        verbose_name = 'SosyalMedia'
        verbose_name_plural = 'SosyalMedias'
        ordering=('order',)

class Document(AbstractModel):
    order = models.IntegerField(default='0', verbose_name='Order')
    slug = models.SlugField(default='', max_length=200, verbose_name='Slug')
    file=models.FileField(default='',verbose_name='Document Name',storage=DocumentStorage(),)
    button_text=models.CharField(default='', max_length=120, blank=True, verbose_name='Butoon Text')

    def __str__(self):
        return f'Document:{self.slug}'
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)
