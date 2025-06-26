from rest_framework.viewsets import ModelViewSet
from .models import Reserva
from .models import Funcionario
from .models import Servico
from .serializers import ReservaSerializer
from .serializers import FuncionarioSerializer
from .serializers import ServicoSerializer


class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer