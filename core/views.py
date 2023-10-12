from django.shortcuts import render
from core.models import GeneralSetting,ImageSetting,Skill,Experience
# Create your views here.
def index(request):
    site_title=GeneralSetting.objects.get(name='site_title').paramater
    site_keywords = GeneralSetting.objects.get(name='site_keywords').paramater
    site_description = GeneralSetting.objects.get(name='site_description').paramater
    home_banner_name=GeneralSetting.objects.get(name='home_banner_name').paramater
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').paramater
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').paramater
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').paramater
    about_footer = GeneralSetting.objects.get(name='about_footer').paramater
    favicon=ImageSetting.objects.get(name='favicon').file
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_img = ImageSetting.objects.get(name='home_banner_img').file
    skills=Skill.objects.all()
    experiences=Experience.objects.all()
    context={
        'site_title':site_title,
        'site_keywords':site_keywords,
        'site_description':site_description,
        'home_banner_name':home_banner_name,
        'home_banner_title':home_banner_title,
        'home_banner_description':home_banner_description,
        'about_myself_welcome':about_myself_welcome,
        'about_footer':about_footer,
        'favicon':favicon,
        'header_logo':header_logo,
        'home_banner_img':home_banner_img,
        'skills':skills,
        'experiences':experiences,

    }
    return render(request,'index.html',context)

