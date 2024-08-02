from .models import *
import datetime
import calendar


class RentServices():
    def salvarRent(self, request):
        comprou_antes = False
        a = Address(street = request.POST['street'],
                 number = request.POST['number'],
                 complement = request.POST['complement'], 
                 district = request.POST['district'],
                 city = request.POST['city'],
                 state = request.POST['state'] )
        a.save()
        
        r = Rent(date=request.POST['date'], 
                 start_hours=request.POST['start_hours'],
                 end_hours=request.POST['end_hours'],
                 client_id= request.POST['select_client'],
                 theme_id = request.POST['select_theme'],
                 address = a )
        given_date = datetime.datetime.strptime(r.date, "%Y-%m-%d")
        if r.date == given_date.isoweekday(5) or r.date == given_date.isoweekday(6) or r.date == given_date.isoweekday(7):
            price = price - (price * 0.4)
        for i in Rent.objects.all():
            if i.client.id == r.client_id:
                comprou_antes = True
        if comprou_antes == True:
            price = price - (price * 0.1)
        if (comprou_antes == True) and (r.date == given_date.isoweekday(5) or r.date == given_date.isoweekday(6) or r.date == given_date.isoweekday(7)):
            price = price - (price * 0.5)
        return r.save()