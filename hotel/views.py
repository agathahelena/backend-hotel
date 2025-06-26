from rest_framework.viewsets import ModelViewSet
from .models import Hospede
from .serializers import HospedeSerializer
from .models import Quarto
from .serializers import QuartoSerializer
from .models import Pagamento
from .serializers import PagamentoSerializer
from .models import FuncaoFuncionario
from .serializers import FuncaoFuncionarioSerializer

class HospedeViewSet(ModelViewSet):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer

class QuartoViewSet(ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class FuncaoFuncionarioViewSet(ModelViewSet):
    queryset = FuncaoFuncionario.objects.all()
    serializer_class = FuncaoFuncionarioSerializer