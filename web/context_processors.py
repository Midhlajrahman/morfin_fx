from .models import Service

def main_context(request):
    services = Service.objects.all()
    return {
        'header_services': services
    }