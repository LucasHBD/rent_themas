from .models import *
cliente_comprou_antes = False
import datetime
import calendar
from django.shortcuts import get_object_or_404


class RentServices():
    def salvarRent(self, a, r):
        desconto_de_dia_da_semana = 0
        desconto_de_cliente_previo = 0
        tema = get_object_or_404(Theme, pk = r.theme.id)
        cliente = get_object_or_404(Client, pk = r.client.id)

        a.save()
        # negocio: 
        # caso o cliente já tiver comprado antes, dar um desconto de 10%.
        # caso o aluguel seja feito para dias dentro do intervalo de segunda e quinta feira, recebe um desconto de 40%.
        date_em_datetime = datetime.datetime.strptime(r.date, "%Y-%m-%d")
        if not date_em_datetime.isoweekday() > 4: # aplica desconto de dia da semana
            desconto_de_dia_da_semana = tema.price * 0.40

        for aluguel in Rent.objects.all():
            if aluguel.client == cliente:
                desconto_de_cliente_previo = tema.price * 0.1

        r.valor_total = tema.price - (desconto_de_cliente_previo + desconto_de_dia_da_semana)

        return r.save()