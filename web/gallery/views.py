from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Image
from django.db.models import Q
from .filters import FilterImage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# главная страница Галереи с фильтрами
def home(request):
    images = Image.objects.all().order_by('-date_posted')
    myFilter = FilterImage(request.GET, queryset=images)
    images = myFilter.qs
    context = {
        'images': images,
        'myFilter': myFilter,
    }
    return render(request, 'gallery/home_filter.html', context)


# вывод изображений на страницу Галереи !!! только для зарегистрированных пользователей
class ImageListView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'gallery/home.html'
    ordering = ['-date_posted']
    paginate_by = 6

    # отображает страницу только для зарегистрированных пользователей
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(ImageListView, self).dispatch(request, *args, **kwargs)


# поиск по сайту
class SearchResultsView(ListView):
    model = Image
    template_name = 'gallery/search_results.html'
    context_object_name = 'images'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        q = Q(title__icontains=query) | Q(description__icontains=query) | Q(date_posted__icontains=query)
        object_list = Image.objects.filter(q)
        return object_list


# изображения принадлежащие пользователю
class UserImageListView(ListView):
    model = Image
    template_name = 'gallery/user_images.html'
    context_object_name = 'images'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Image.objects.filter(author=user).order_by('-date_posted')


# просмотр изображения
class ImageDetailView(DetailView):
    model = Image


# добавление нового изображения Галереи
class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'gallery/image_form_create.html'
    fields = ['picture', 'title', 'geo_location', 'peoples', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# обновление изображения Галереи
class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    template_name = 'gallery/image_form_update.html'
    fields = ['picture', 'title', 'geo_location', 'peoples', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False


# удалить изображение Галереи
class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/'

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False


# О галерее
def about(request):
    return render(request, 'gallery/about.html', {'title': 'Об исполнителе'})