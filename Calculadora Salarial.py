print("Calculadora Salarial - v 1.00 \nCreado por: Leonardo Paniagua Muñoz\n")

deducciones_ccss = 0.1067
valor_por_hora_extra = 1.5
valor_feriados = 2

def calculadora_salarial ():
    contar = 0
    while contar == 0:
        control_quincena = 0
        while control_quincena == 0:
            quincena = input("¿A este trabajador se le paga por quincena? Ingrese 'S' o 'N': \n")
            if quincena.lower() != "s" and quincena.lower() != "n":
                print("Por favor ingrese 'S' o 'N'.")
            else:
                control_quincena = 1

        while True:
            try:
                salario_bruto = int(input("Ingrese el sueldo bruto: \n"))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

        primera_quincena = salario_bruto * (1 - deducciones_ccss) / 2
        valor_por_hora = salario_bruto / 30 / 4

        control_horas_extras = 0
        while control_horas_extras == 0:
            horas_extras = input("¿Trabajó horas extra? Ingrese 'S' o 'N': \n")
            if horas_extras.lower() != "s" and horas_extras.lower() != "n":
                print("Por favor ingrese 'S' o 'N'.")
            else:
                control_horas_extras = 1

        if horas_extras.lower() == "s":

            while True:
                try:
                    cantidad_horas_extras = int(input("Ingrese la cantidad de horas extra trabajadas SIN CONTAR FERIADOS: \n"))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            total_pago_extras_regulares = cantidad_horas_extras * valor_por_hora * valor_por_hora_extra

            control_feriados = 0
            while control_feriados == 0:
                feriados = input("¿Trabajó feriados? Ingrese 'S' o 'N': \n")
                if feriados.lower() != "s" and feriados.lower() != "n":
                    print("Por favor ingrese 'S' o 'N'.")
                else:
                    control_feriados = 1

            if feriados.lower() == "s":
                while True:
                    try:
                        horas_en_feriado = int(input("Ingrese la cantidad de horas trabajadas en feriado: \n"))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

                total_pago_feriados = horas_en_feriado * valor_por_hora * valor_feriados
                total_sueldo_mensual = salario_bruto + total_pago_extras_regulares + total_pago_feriados
                total_retenciones = total_sueldo_mensual * deducciones_ccss
                sueldo_por_pagar = total_sueldo_mensual - total_retenciones
                print(f"Los resultados son los siguientes:\n\nSalario bruto: ₡{total_sueldo_mensual:,.2f}\nTotal horas extra regulares: ₡{total_pago_extras_regulares:,.2f}\nTotal horas extra en feriados: ₡{total_pago_feriados:,.2f}\nRetenciones: ₡{total_retenciones:,.2f}\nSueldo por pagar: ₡{sueldo_por_pagar:,.2f}\n")
            else:
                total_sueldo_mensual = salario_bruto + total_pago_extras_regulares
                total_retenciones = total_sueldo_mensual * deducciones_ccss
                sueldo_por_pagar = total_sueldo_mensual - total_retenciones
                print(f"Los resultados son los siguientes:\n\nSalario bruto: ₡{total_sueldo_mensual:,.2f}\nTotal horas extra regulares: ₡{total_pago_extras_regulares:,.2f}\nRetenciones: ₡{total_retenciones:,.2f}\nSueldo por pagar: ₡{sueldo_por_pagar:,.2f}\n")

        else:
            total_sueldo_mensual = salario_bruto
            total_retenciones = total_sueldo_mensual * deducciones_ccss
            sueldo_por_pagar = total_sueldo_mensual - total_retenciones
            print(f"Los resultados son los siguientes:\n\nSalario bruto: ₡{total_sueldo_mensual:,.2f}\nRetenciones: ₡{total_retenciones:,.2f}\nSueldo por pagar: ₡{sueldo_por_pagar:,.2f}\n")


        if quincena.lower() == "s":
            print(f"Primera quincena: ₡{primera_quincena:,.2f}\nSegunda quincena: ₡{sueldo_por_pagar - primera_quincena:,.2f}\n")

        control_volver = 0
        while control_volver == 0:
            volver = input("¿Desea hacer otro cálculo? Ingrese 'S' o 'N': \n")
            if volver.lower() != "s" and volver.lower != "n":
                print("Por favor ingrese 'S' o 'N'.")
            else:
                control_volver = 1
                
        if volver.lower() == "n":
            contar += 1

calculadora_salarial()
    