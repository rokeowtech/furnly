from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from product.models import MyProduct
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import FormMixin
import random

class ProductListView(ListView):
	model = MyProduct
	context_object_name = 'products'
	paginate_by = 6
	ordering = ['-date_posted']

def cart(request):
	return render(request,'cart.html')


def ProductByProducer(request, producer):
    products = MyProduct.objects.all()
    prod = []
    for product in products:
        if product.Producer.username == producer:
            prod.append(product)
    return render(request, 'product/productsByProducer.html',{'products':prod})

class ProductDetailView(DetailView):
	model = MyProduct

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			try:
				subject = 'Testing'
				message = 'Howdy'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = ['thepeakprogrammer@gmail.com',]
				send_mail(subject, message, email_from, recipient_list )
				messages.success(request, f'Order placed, wait for confirmation')
				return redirect('/')
			except:
				messages.info(request, f'Sorry, we encountered a problem, try again')
				return redirect('/')


class ProductPurchaseView(DetailView):
	model = MyProduct

	def post(self,request,*args,**kwargs):
		if request.method == 'POST':
			subject = 'Testing'
			message = 'Howdy'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = ['thepeakprogrammer@gmail.com',]
			send_mail(subject,message, email_from, recipient_list)
# 			print(request.user)
			return redirect('/')

class ProductCreateView(CreateView):
	"""docstring for ClassName"""
	model = MyProduct
	fields = ['ProductThumb', 'ProductName', 'ProductDescription', 'ProductPrice', 'ProductContact', 'location']

	def form_valid(self, form):
		form.instance.Producer = self.request.user
		return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	"""docstring for ClassName"""
	model = MyProduct
	fields = ['ProductThumb', 'ProductName', 'ProductDescription', 'ProductPrice', 'ProductContact', 'location']

	def form_valid(self, form):
		form.instance.Producer = self.request.user
		return super().form_valid(form)

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.Producer:
			return True
		return False

class ProductDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	"""docstring for ProductDeleteView"""
	model = MyProduct
	success_url = '/'


	def test_func(self):
		product = self.get_object()
		if self.request.user == product.Producer:
			return True
		return False
