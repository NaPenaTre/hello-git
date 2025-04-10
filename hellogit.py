# print( "hello git")
# print ("New hello GITg dfgdfgfd")


years = 8
months = 29
days = 68

if months >= 12:# si tengo mas de 12 meses, convertirlo en anos
    years_from_months = months // 12
    restmont = ((months % 12)*30)   # lo que sobra convertirlo en dias
    total_years = years + years_from_months
print(f"El total de anos es {total_years} y me quedan {restmont} dias")


if days >=7: # Si hay mas de 7 dias, convertirlo en semanas
    weeks_from_days = int(days / 7) # Con esto tengo mis semanas
    restdays = days % 7  # saber los dias que me quedaron
print(f"El total de semanas de los dias es: {weeks_from_days} semanas y me quedan {restdays} dias")

# Una vez que tengo las semanas, pasarlas a meses
if weeks_from_days >= 4:
    months_from_weeks = int(weeks_from_days / 4) # con esto se cuantos meses obtuve de las semanas
    restweeks = ((weeks_from_days % 4))
    total_months_from_weeks = (weeks_from_days + months_from_weeks)
print(f"EL total de meses obtenido de las semanas y lo qu queso de los anos es {total_months_from_weeks} y restan {restweeks} dias")

# Veamos cuanto quedo de los dias
restodelosdias = restweeks*7
total_days = restmont + restdays + restodelosdias
print(f"De los meses quedaron {restmont}, de los dias quedaron {restdays} y de las semanas quedaron {restodelosdias}")
print(f" En total quedaron {total_days} dias")


print("_______________________________")

days2 = days + restmont # como fueron muchos dias que sobran de los meses los agregamos aqui
if days2 >=7: # Si hay mas de 7 dias, convertirlo en semanas
    weeks_from_days2 = int(days2 / 7) # Con esto tengo mis semanas
    restdays2 = days2 % 7  # saber los dias que me quedaron
print(f"El total de semanas de los otros dias es: {weeks_from_days2} semanas y me quedan {restdays2} dias")

# Una vez que tengo las semanas, pasarlas a meses
if weeks_from_days2 >= 4:
    months_from_weeks2 = int(weeks_from_days2 / 4) # con esto se cuantos meses obtuve de las semanas
    restweeks2 = ((weeks_from_days2 % 4))
    total_months_from_weeks2 = (weeks_from_days2 + months_from_weeks2)
print(f"EL total de meses obtenido de las semanas y lo qu queso de los anos es {total_months_from_weeks} y restan {restweeks} dias")