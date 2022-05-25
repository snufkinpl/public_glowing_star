from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import book
from .forms import PositionForm


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('books')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('books')
        return super(RegisterPage, self).get(*args, **kwargs)


class bookList(LoginRequiredMixin, ListView):
    model = book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['books'].filter(user=self.request.user)
        context['count1'] = context['books'].filter(complete=False).count()
        context['count2'] = context['books'].filter(borrow=True).count()
        context['count3'] = context['books'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['books'] = context['books'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class bookDetail(LoginRequiredMixin, DetailView):
    model = book
    context_object_name = 'book'
    template_name = 'base/book.html'


class bookCreate(LoginRequiredMixin, CreateView):
    model = book
    fields = ['author', 'title', 'complete', 'borrow']
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(bookCreate, self).form_valid(form)


class bookUpdate(LoginRequiredMixin, UpdateView):
    model = book
    fields = ['author', 'title', 'complete', 'borrow']
    success_url = reverse_lazy('books')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = book
    context_object_name = 'book'
    success_url = reverse_lazy('books')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class bookReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_book_order(positionList)

        return redirect(reverse_lazy('books'))
