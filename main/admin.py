from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Narx)
admin.site.register(Contact)
@admin.register(Xizmat)
class XizmatAdmin(admin.ModelAdmin):
	list_display = ['title',]
	list_display_links = ['title',]
	prepopulated_fields = {'slug':('title',)}


admin.site.register(Narx_ru)
admin.site.register(Contact_ru)
@admin.register(Xizmat_ru)
class Xizmat_ruAdmin(admin.ModelAdmin):
	list_display = ['title',]
	list_display_links = ['title',]
	prepopulated_fields = {'slug':('title',)}