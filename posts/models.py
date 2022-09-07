from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class aparteman(models.Model):
    STATUS_BUY = (
        ('برای خرید', 'برای خرید'),
        ('برای اجاره', 'برای اجاره'),
    )
    #برای رهن و اجاره
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاحات ارضی', 'اصلاحات ارضی'),
    )

    titr = models.CharField(max_length=150, verbose_name='تیتر')
############### impo ######################
    # nevisande = models.ForeignKey(
    #     User, on_delete=models.CASCADE, verbose_name='نویسنده')
###########################################    
    status_buy = models.CharField(
        max_length=50, choices=STATUS_BUY, default='برای خرید', verbose_name='برای خرید/رهن و اجاره')
    gheymat = models.PositiveIntegerField(
        default=0, verbose_name='قیمت')
    gheymat_rahn = models.PositiveIntegerField(
        default=0, verbose_name='قیمت رهن')
    gheymat_ejare = models.PositiveIntegerField(
        default=0, verbose_name='قیمت اجاره')
    locations = models.TextField(verbose_name='ادرس اپارتمان')
    sanad = models.CharField(
        max_length=32, choices=SANAD_CHOICES, default='شش دانگ', verbose_name='نوع سند')
    andaze = models.PositiveIntegerField(verbose_name='متراژ',default=0)
    tabaghe = models.PositiveIntegerField(verbose_name='طبقه')
    tedad_tabaghe = models.PositiveSmallIntegerField(verbose_name='تعداد طبقه')
    tedad_vahed_tabaghe = models.PositiveSmallIntegerField(
        verbose_name='تعداد واحد در هر طبقه',default=0)
    tedad_otagh = models.CharField(max_length=2, verbose_name='تعداد اتاق')
    tedad_dastshoe = models.PositiveSmallIntegerField(
        verbose_name='تعداد سرویس بهداشتی')
    sal_sakht = models.IntegerField(verbose_name='سال ساخت')
    tozihat_karbar = models.TextField(verbose_name='توضیحات کاربر')
    tozihat_khososy = models.TextField(
        blank=True, null=True, verbose_name='توضیحات خصوصی')
    image = models.ImageField(verbose_name='عکس اصلی',null=True)
    upload_time = models.DateField(auto_now=True, verbose_name='زمان ثبت')
    parking = models.BooleanField(default='False')
    ghabel_moaveze = models.BooleanField(default=False, verbose_name='قابل معاوضه؟')
    vise = models.BooleanField(default=False, verbose_name='ویژه؟')
    active = models.BooleanField(default=True, verbose_name='نمایش داده شود؟')
    # hits = models.ManyToManyField(IPAddressApa,blank=True,related_name='hits')
    #--------------------BooleanField----------------
    tahvie = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    trass = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    bed = models.BooleanField(default=False)
    micro = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    sahel = models.BooleanField(default=False)
    system_garmayeshi= models.BooleanField(default=False)
    sigary = models.BooleanField(default=False)
    #-----------------------    
    def __str__(self):
        return self.titr

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'اپارتمان'
        verbose_name_plural = 'اپارتمان ها'

class aparteman_images(models.Model):
    place = models.ForeignKey(aparteman,on_delete=models.CASCADE)
    image = models.ImageField()
    alt = models.CharField(max_length=50)
