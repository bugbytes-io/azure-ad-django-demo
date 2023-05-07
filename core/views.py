from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

from django.conf import settings
ms_identity_web = settings.MS_IDENTITY_WEB

@ms_identity_web.login_required
def secret_page(request):
    return render(request, 'secret.html', {})