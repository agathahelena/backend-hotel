from django.contrib import admin
from .models import Hospede
from .models import Quarto
from .models import Pagamento
from .models import FuncaoFuncionario

admin.site.register(Hospede)
admin.site.register(Quarto)
admin.site.register(Pagamento)
admin.site.register(FuncaoFuncionario)