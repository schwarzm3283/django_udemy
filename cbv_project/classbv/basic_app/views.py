from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from . import models


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #school_List

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolDeleteView(DeleteView):
    context_object_name = 'school_detail'
    model = models.School
    success_url = reverse_lazy("basic_app:list")


#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'first injection'
#         context['secondinjection'] = 'second injection'
#         return context


#
# # Create your views here.
# def index(request):
#     return render(request,'index.html')
