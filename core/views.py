from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from . models import Product
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(available=True, product_of_month=True)[:3]
        return context


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = _('Mesajınız uğurla göndərildi, tezliklə sizinlə əlaqə saxlanılacaq')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'about.html'

class ShowRoomView(TemplateView):
    template_name = 'showroom.html'

class ProductListView(ListView):

    model = Product
    context_object_name = 'products'
    template_name = 'products.html'
    queryset = Product.objects.filter(available=True)
    paginate_by = 9


class ProductDetailView(DetailView):

    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'




def search(request):
    products = Product.objects.filter(name__contains = request.GET['search'])

    context = {
        'products':products
    }

    return render(request, 'search.html', context)
