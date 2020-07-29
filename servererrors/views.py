
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.


def internalServerErrorView(request):
    return render(request, 'servererrors/internal_server_error.html', status=500)

# class internalServerErrorView(TemplateView):

#     template_name = "servererrors/internal_server_error.html"

#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         return self.render_to_response(context, status=500)