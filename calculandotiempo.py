## Como calcular tiempo entre experiensas - mmuy rebuscado pero funciono - creo

def calculame_esto(years, months, days):

    if months >= 12:# si tengo mas de 12 meses, convertirlo en anos
        years_from_months = months // 12
        restmont = (months % 12)   #Esto queda en meses
        total_years = years + years_from_months
        print(f"El total de anos es {total_years} y me quedan {restmont} meses\n")
    else:
        restmont = 0
        total_years = 0
        print(f"El numero de anos es {years} con {months} meses\n")

    print(f"Ahora vamos a ver cuantos meses son con los {days} dias iniciales")

    if days >=7: # Si hay mas de 7 dias, convertirlo en semanas
        weeks_from_days = int(days / 7) # Con esto tengo mis semanas
        restdays = days % 7  # saber los dias que me quedaron
        print(f"El total de semanas obtenido con el total de los dias es: {weeks_from_days} semanas y aun quedan {restdays} dias, que no juntan ni una semana")
    else:
        weeks_from_days = 0
        print(f"El numero de dias es {days}")

    # Una vez que tengo las semanas, pasarlas a meses
    if weeks_from_days >= 4:
        months_from_weeks = int(weeks_from_days / 4) # con esto sé cuantos meses obtuve de las semanas
        restweeks = ((weeks_from_days % 4))
        print(f"EL total de meses obtenido de las semanas en total es: {months_from_weeks} meses, y aun quedan {restweeks} semanas, que ya no juntan un mes\n")
    else:
        restweeks = 0
        months_from_weeks = 0
        print("no hay semanas")

    print("Veamos si el total de meses restantes junta otro ano")
    total_rest_months = (restmont + months_from_weeks)
    if total_rest_months >= 12: # si tengo mas de 12 meses, convertirlo en anos
        other_years_from_months = total_rest_months // 12
        rest_of_months = ((total_rest_months % 12))   # lo que sobra en meses
        print(f"El total de anos es {other_years_from_months} anos y quedan {rest_of_months} meses \n")
    else:
        other_years_from_months = 0
        print(f"El total de meses restantes es {total_rest_months}")

    print("Ahora x fin tenemos el total del tiempo")
    real_total_years = years + total_years + other_years_from_months
    print(f"El gran total de anos es {real_total_years}")
    real_total_days = (restweeks * 7) + restdays
    return real_total_years,total_rest_months,real_total_days


for expected_years,expected_months,expected_days,_years, _months, _days in [
    (4, 1, 15, 3, 13, 15),
    #(4, 3, 29, 3, 15, 29),
    ]:
    real_total_years,total_rest_months,real_total_days = calculame_esto (_years,_months,_days)
    print(f"El gran total es {real_total_years} anos, con {total_rest_months} meses y  {real_total_days} dias\n")
    assert real_total_years == expected_years, f" El valor obtenido {real_total_years} es diferente del valor esperado {expected_years}"
    assert total_rest_months == expected_months,f" El valor obtenido {total_rest_months} es diferente del valor esperado {expected_months}"
    assert real_total_days == expected_days,f"El valor obtenido {real_total_days} es diferente del valor esperado {expected_days}"

#
# for nombre_variable in range(0,10,1):
#     print(nombre_variable)
#
#
#