from django.contrib import admin

from .models import Reserva
from .models import Funcionario
from .models import Servico

admin.site.register(Reserva)
admin.site.register(Funcionario)
admin.site.register(Servico)
