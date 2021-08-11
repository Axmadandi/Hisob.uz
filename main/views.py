from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	xizmatlar = Xizmat.objects.all()
	narxlar = Narx.objects.all()
	if request.method=="POST":
		contact = Contact()
		name = request.POST.get('name')
		message = request.POST.get('message')
		tel = request.POST.get('tel')
		contact.name=name
		contact.message=message
		contact.tel=tel
		contact.save()
		return render(request,'index.html')
	context = {
		'xizmatlar':xizmatlar,
		'narxlar':narxlar
	}
	return render(request, 'index.html',context)

