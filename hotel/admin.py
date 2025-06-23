from django.contrib import admin
from .models import Hóspede
from .models import Quarto
from .models import Pagamento
from .models import FunçãoFuncionário

admin.site.register(Hóspede)
admin.site.register(Quarto)
admin.site.register(Pagamento)
admin.site.register(FunçãoFuncionário)