from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class LoginView(View):

    # def dispatch(self, request, *args, **kwargs):
    #     print('dispatch')
    #     # return View.dispatch(self,request, *args, **kwargs)
    #     return super().dispatch(request,*args,**kwargs)
    #     # return HttpResponse('ok')

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return HttpResponse('ok')
