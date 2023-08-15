from django.views.generic import (TemplateView, DetailView, ListView, CreateView)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from . import (models, forms)


class VisionDetailView(DetailView):
    """
    Class-based view for Vision detail template
    """
    template_name = 'visions/vision-detail.html'
    queryset = models.Vision.objects.filter(admin_approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add form for creating a Response object to this Vision object
        context['response_create_form'] = forms.ResponseCreateForm
        # Add list of responses that relate to the current vision and have been approved by admin
        context['responses'] = models.Response.objects.filter(vision=self.object.id, admin_approved=True)
        return context


class VisionListView(ListView):
    """
    Class-based view for Vision list template
    """
    template_name = 'visions/vision-list.html'
    queryset = models.Vision.objects.filter(admin_approved=True)
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_all_visions'] = self.queryset.count()
        return context


class VisionCreateView(CreateView):
    """
    Class-based view to create a new Vision object in the database
    """

    template_name = 'visions/vision-create.html'
    form_class = forms.VisionCreateForm
    success_url = reverse_lazy('visions:vision-create-success')

    def post(self, request):
        """
        Save the main form for the new Vision object and
        create child VisionAdditionalImage objects
        """
        form = forms.VisionCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # Save main object
            new_vision = form.save()
            # Create child VisionAdditionalImage objects
            additionalimages = request.FILES.getlist('additionalimages')
            for additionalimage in additionalimages:
                models.VisionAdditionalImage.objects.create(
                    vision=new_vision,
                    image=additionalimage
                )
            return HttpResponseRedirect(reverse('visions:vision-create-success'))
        else:
            return HttpResponseRedirect(reverse('visions:vision-create'))


class VisionCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the vision create success template
    """

    template_name = 'visions/vision-create-success.html'


class ResponseCreateView(CreateView):
    """
    Class-based view to create a new models.Response object in the database
    This works by passing data to the forms.ResponseCreateForm form
    """

    form_class = forms.ResponseCreateForm
    template_name = 'visions/response-create-failed.html'
    success_url = reverse_lazy('visions:response-create-success')


class ResponseCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the response create success template
    """

    template_name = 'visions/response-create-success.html'
