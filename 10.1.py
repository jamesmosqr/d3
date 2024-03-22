def c_smensual(salarios):
    total_salarios = sum(salarios)
    pro_sal = total_salarios / len(salarios)
    return pro_sal


def increSalarios(salarios, incporce):
    salarios_incrementados = [salario * (1 + incporce / 100) for salario in salarios]
    return salarios_incrementados


def main():
    salarios_empleados = []


    for i in range(3):
        salario = float(input(f"Ingrese el salario del empleado {i + 1}: "))
        salarios_empleados.append(salario)

    promedio_salarios = c_smensual(salarios_empleados)


    salarios_incrementados = increSalarios(salarios_empleados, 2.5)


    print(f"El promedio de los salarios mensuales es: {promedio_salarios}\n")

    print("Salarios antes y después del aumento del 2.5%:")
    for i, salario in enumerate(salarios_empleados):
        salario_incrementado = salarios_incrementados[i]
        print(f"Empleado {i + 1}: Salario anterior: {salario}, Salario con aumento: {salario_incrementado}")


if __name__ == "__main__":
    main()
