from rest_framework.serializers import ModelSerializer
from .models import Hospede
from .models import Quarto
from .models import Pagamento
from .models import FuncaoFuncionario

class HospedeSerializer(ModelSerializer):
    class Meta:
        model = Hospede
        fields = '__all__'

class QuartoSerializer(ModelSerializer):
    class Meta:
        model = Quarto
        fields = '__all__'

class PagamentoSerializer(ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'

class FuncaoFuncionarioSerializer(ModelSerializer):
    class Meta:
        model = FuncaoFuncionario
        fields = '__all__'