"""
7.	Desarrolle un programa que calcule el promedio de edad hombre y
mujeres de un grupo de estudiantes.
"""
def pro_edad(t_personas, edades):
    if t_personas == 0:
        return 0
    suma_edades = sum(edades)
    promedio = suma_edades / t_personas
    return promedio

def main():
    c_hom = int(input("Ingrese la cantidad de hombres en el grupo: "))
    edades_hombres = []
    for i in range(c_hom):
        edad = int(input(f"Ingrese la edad del hombre {i+1}: "))
        edades_hombres.append(edad)

    cantidad_mujeres = int(input("Ingrese la cantidad de mujeres en el grupo: "))
    edades_mujeres = []
    for i in range(cantidad_mujeres):
        edad = int(input(f"Ingrese la edad de la mujer {i+1}: "))
        edades_mujeres.append(edad)

    pro_hom = pro_edad(c_hom, edades_hombres)
    pro_muj = pro_edad(cantidad_mujeres, edades_mujeres)

    print(f"El promedio de edad de los hombres es: {pro_hom}")
    print(f"El promedio de edad de las mujeres es: {pro_muj}")

if __name__ == "__main__":
    main()
