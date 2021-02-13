from django.shortcuts import render
from django.views import View


# Create your views here.

class IndexView(View):
    """
    Отображение стартовой страницы
    """

    def get(self, request):
        return render(request, 'catalog/index.html')