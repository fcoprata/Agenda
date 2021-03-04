from django.contrib import admin
from core.models import Evento
# Register your models here.


class EventoAdm(admin.ModelAdmin):
    list_display = ('titulo', 'date_evento', 'date')


admin.site.register(Evento, EventoAdm)