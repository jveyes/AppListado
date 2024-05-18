from corsheaders.signals import check_request_enabled

from AppListado.models import AppListado


def cors_allow_mysites(sender, request, **kwargs):
    return AppListado.objects.filter(host=request.headers["origin"]).exists()


check_request_enabled.connect(cors_allow_mysites)