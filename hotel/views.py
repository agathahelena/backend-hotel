from rest_framework.viewsets import ModelViewSet
from .models import Reserva
from .models import Funcionario
from .models import Servico
from .serializers import ReservaSerializer
from .serializers import FuncionarioSerializer
from .serializers import ServicoSerializer
from .models import Hospede
from .serializers import HospedeSerializer
from .models import Quarto
from .serializers import QuartoSerializer
from .models import Pagamento
from .serializers import PagamentoSerializer
from .models import FuncaoFuncionario
from .serializers import FuncaoFuncionarioSerializer

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

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
