import random
import string

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from .forms import GenerateForm
from .models import User, Molecular


class HomeView(View):
    def get(self, *args, **kwargs):
        form = GenerateForm(self.request.GET or None)
        context = {"form": form}
        if form.is_valid():
            context['data'] = form.cleaned_data
        return render(self.request, "home.html", context)


class DetailView(DetailView):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass


class CompareView(View):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass


class SaveListView(View):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass