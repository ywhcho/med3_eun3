from django.db import models

# Create your models here.

class Ingredient(models.Model):
    """성분 모델"""
    name = models.CharField('성분명', max_length=200, unique=True)
    description = models.TextField('설명', blank=True)
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    
    class Meta:
        verbose_name = '성분'
        verbose_name_plural = '성분'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Company(models.Model):
    """제조회사 모델"""
    name = models.CharField('회사명', max_length=200, unique=True)
    address = models.CharField('주소', max_length=500, blank=True)
    phone = models.CharField('전화번호', max_length=50, blank=True)
    website = models.URLField('웹사이트', blank=True)
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    
    class Meta:
        verbose_name = '제조회사'
        verbose_name_plural = '제조회사'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Efficacy(models.Model):
    """효능 모델"""
    name = models.CharField('효능명', max_length=200, unique=True)
    description = models.TextField('설명', blank=True)
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    
    class Meta:
        verbose_name = '효능'
        verbose_name_plural = '효능'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Medicine(models.Model):
    """의약품 모델"""
    name = models.CharField('제품명', max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='제조회사', related_name='medicines')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='성분', related_name='medicines')
    efficacies = models.ManyToManyField(Efficacy, verbose_name='효능', related_name='medicines')
    
    # 상세 정보
    dosage = models.TextField('용법용량', blank=True)
    precautions = models.TextField('주의사항', blank=True)
    side_effects = models.TextField('부작용', blank=True)
    storage = models.CharField('보관방법', max_length=500, blank=True)
    
    # 추가 정보
    approval_date = models.DateField('허가일자', null=True, blank=True)
    approval_number = models.CharField('허가번호', max_length=100, blank=True)
    
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    
    class Meta:
        verbose_name = '의약품'
        verbose_name_plural = '의약품'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

