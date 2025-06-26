from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from hotel.views import HospedeViewSet
from hotel.views import QuartoViewSet
from hotel.views import PagamentoViewSet
from hotel.views import FuncaoFuncionarioViewSet

router = DefaultRouter()
router.register(r'Hóspedes', HospedeViewSet)
router.register(r'Quartos', QuartoViewSet)
router.register(r'Pagamento', PagamentoViewSet)
router.register(r'Função dos Funcionários', FuncaoFuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]