from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexView(View):
    """
    Отображение стартовой страницы
    """

    def get(self, request):
        # num_visits = request.session.get('num_visits', 0)
        # request.session['num_visits'] = num_visits + 1
        return render(request, 'catalog/index.html')

