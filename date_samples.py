from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time

now = datetime.now()
print(now)
print(datetime.timestamp(now))

print(now.strftime("%Y%m%d%H%M%S"))

a_date = date(1977, 3, 23)
print(a_date)
print(type(a_date))

# dia
print('O dia ', a_date.day)

# mes
print('O mes ', a_date.month)

# dia
print('O ano ', a_date.year)

# dia da semana
print('dia da semana ', + a_date.weekday())

# hoje
print('hoje ' + str(date.today()))

# adicionar 2 dia mais
hoje = date.today()
print('Hoje é ', hoje)
depois_de_amanha = hoje + timedelta(days=2)
print('mais dois dia é ', depois_de_amanha)

# hora
hora = time(23, 59, 59, 9999)
print(hora)
print(type(hora))

print('hora ' + str(hora.hour))
print('minuts ' + str(hora.minute))
print('segundos ' + str(hora.second))
print('milisegundos ' + str(hora.microsecond))

# diferenca entre duas datas
# diff = date.today() - a_date
# anos = int(diff.days / 365)
# print('diferenca ', anos)
anos = (date.today() - a_date).days // 365
meses = int(((date.today() - a_date).days / 365) * 12)
dias = (date.today() - a_date).days
# if anos == 1:
# print(f'Voce tem: {anos} ano de idade, {meses} meses e {dias} dias vividos.')
# else:
print(f'Voce tem: {anos} anos de idade, {meses} meses e {dias} dias vividos.')

# se é dia da semana # 0 domingo 1 segunda 2 terca 3 quarta 4 quinta 5 sexta 6 sabado
print(date.today().isoweekday())

# cria uma data de um string
data_str = '2024-02-17'
data_resultante = datetime.strptime(data_str, '%Y-%m-%d')
print(data_resultante)

data_str = '1-1-2024'
data_resultante = datetime.strptime(data_str, '%d-%m-%Y')
print(data_resultante)

data_str = '23 March, 1977'
data_resultante = datetime.strptime(data_str, '%d %B, %Y')
print(data_resultante.date())
