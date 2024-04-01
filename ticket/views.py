
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.


class start_p(TemplateView):
    template_name = 'dash.html'
    
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(start_p, self).dispatch(*args, **kwargs)
    
    


    
