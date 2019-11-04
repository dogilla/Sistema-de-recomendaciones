from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, View
from Pagina.models import Pagina
from Pagina.forms import PaginaForm
from Pagina.Kmeans import Kmeans
import csv

class HomeView(CreateView):
    model = Pagina
    template_name = "Pagina/home.html"
    form_class = PaginaForm
    success_url =  reverse_lazy('resultado')

    def get(self, request, *args, **kwargs):
        context = {'form': PaginaForm(initial=self.initial)}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            solucion = form.save()
            appname = str(solucion.recomendacion)
            k = Kmeans(5)
            recomendaciones = k.k_mean_resultado(appname)
        context = {
            'form': form,
            'appname': appname,
            'recomendaciones': recomendaciones
        }
        return render(request, "Pagina/resultado.html" , context)

class ResultadoView(View):
    form_class = PaginaForm
    template_name = "Pagina/resultado.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()



