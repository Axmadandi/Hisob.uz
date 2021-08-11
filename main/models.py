from django.db import models
from django.urls import reverse
# Create your models here.

class Xizmat(models.Model):
	title = models.CharField('Nomi',max_length=150)
	slug = models.SlugField('*',max_length=1000,unique=True)
	date = models.DateTimeField(auto_now=True)
	body = models.TextField('Text')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('main:xizmat_detail', kwargs={'xizmat_slug':self.slug})

class Narx(models.Model):
	qiymati = models.CharField('Qiymati',max_length=200)
	summasi = models.CharField('Summasi',max_length=200)
	slug = models.SlugField('*',max_length=1000,unique=True)
	date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.qiymati

class Contact(models.Model):
	name = models.CharField('Toliq Ismingiz',max_length=50)
	tel = models.CharField('Tel',max_length=50)
	message = models.TextField('Xabar',max_length=500)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contactlar'