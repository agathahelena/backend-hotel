from rest_framework.serializers import ModelSerializer
from .models import Reserva, Funcionario, Servico

class ReservaSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'