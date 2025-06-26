from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from hotel.views import ReservaViewSet, FuncionarioViewSet, ServicoViewSet

router = DefaultRouter()
router.register(r'reserva', ReservaViewSet)
router.register(r'funcionario', FuncionarioViewSet)
router.register(r'servico', ServicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
