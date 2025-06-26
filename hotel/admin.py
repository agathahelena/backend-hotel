from django.contrib import admin
from .models import Hospede
from .models import Quarto
from .models import Pagamento
from .models import FuncaoFuncionario
from .models import Reserva
from .models import Funcionario
from .models import Servico

admin.site.register(Reserva)
admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(Hospede)
admin.site.register(Quarto)
admin.site.register(Pagamento)
admin.site.register(FuncaoFuncionario)
