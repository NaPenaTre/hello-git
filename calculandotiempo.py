## Como calcular tiempo entre experiensas - mmuy rebuscado pero funciono - creo
from selectors import SelectSelector


def calculame_esto(years, months, days):
    #Empecemos con los días#
    if days >=30: # Sí hay más de 30 días, convertirlo en meses
        month_created_by_days = int(days / 30) # Con esto tengo mis meses
        restdays = days % 30  # Con esto sabemos los días que quedan
   #     print(f"El numero de meses creados con los dias es: {month_created_by_days} y quedan {restdays} dias. Estos dias seran contabilizados al final\n")
    else:
        restdays = 0
        month_created_by_days = 0
     #   print(f"El numero de dias es {days}\n")

    #Ahora calculemos el número de meses - Considerando los meses creados por los días #
    months_added = months + month_created_by_days
    if months_added >= 12:# si tengo mas de 12 meses, convertirlo en anos
        years_created_by_months = months_added // 12 #Es el numero de anos creado
        restmont = (months_added % 12)   # Si no se juntaron años esto es lo que queda en meses
    #    print(f"El total de anos creados con los meses es {years_created_by_months} y me quedan {restmont} meses\n")
    else:
        restmont = 0
        years_created_by_months = 0
   #     print(f"El numero de anos es {years} con {months} meses\n")

        #Una vez que tenemos los meses veamos los totales

    if  month_created_by_days !=0:
        total_days= restdays
    else:
        total_days = days

    if  years_created_by_months !=0:
        total_months = restmont
    else:
        total_months = months

    if years_created_by_months !=0:
        total_years = years + years_created_by_months
    else:
        total_years = years

 #   print("Ahora x fin tenemos el total del tiempo")
    return total_years,total_months,total_days



for expected_years,expected_months,expected_days,_years, _months, _days in [
    (4, 6, 0, 3, 13, 150),
    (4, 4, 0, 3, 11, 150),
    (0, 11, 29, 0, 11, 29),
    (1, 0, 0, 0, 12, 0),
    (5, 0, 3, 3, 24, 3),
    (1, 1, 0, 0, 11, 60),
    # (0, 11, 29, 0, 11, 29),
    ]:
    real_total_years,total_rest_months,real_total_days = calculame_esto (_years,_months,_days)
    print(f"({_years},{_months},{_days})El gran total es {real_total_years} anos, con {total_rest_months} meses y  {real_total_days} dias\n")
    assert real_total_years == expected_years, f" El valor obtenido {real_total_years} es diferente del valor esperado {expected_years}"
    assert total_rest_months == expected_months,f" El valor obtenido {total_rest_months} es diferente del valor esperado {expected_months}"
    assert real_total_days == expected_days,f"El valor obtenido {real_total_days} es diferente del valor esperado {expected_days}"

#
# for nombre_variable in range(0,10,1):
#     print(nombre_variable)
#
#
#