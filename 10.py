"""
10.	Desarrolle un programa que permita saber el salario de 20
empleados por mes se requiere el promedio de estos y el pago de cado uno de igual
 manera cuanto ganaran si se hace un incremento del 2.5%
"""


def c_s_mensual(salarios):
    ttl_sal = sum(salarios)
    promedio_salarios = ttl_sal / len(salarios)
    return promedio_salarios


def incr_sal(salarios, incr_porcentaje):
    salarios_incrementados = [salario * (1 + incr_porcentaje / 100) for salario in salarios]
    return salarios_incrementados


def main():

    sal_empleados = []

    for i in range(5):
        salario = float(input(f"Ingrese el salario del empleado {i + 1}: "))
        sal_empleados.append(salario)


    pro_salarios = c_s_mensual(sal_empleados)

    # Calcular los salarios incrementados en un 2.5%
    salarios_incrementados = incr_sal(sal_empleados, 2.5)


    print(f"El promedio de los salarios mensuales es: {pro_salarios}")

 
    print("\nSalarios incrementados en un 2.5%:")
    for i, salario in enumerate(salarios_incrementados):
        print(f"Empleado {i + 1}: {salario}")


if __name__ == "__main__":
    main()
