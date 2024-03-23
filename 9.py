"""
9.	Considerando que el consumo de servicios de públicos de un
establecimiento ha venido aumentando el alcalde de la ciudad requiere de
un programa que le permita saber cuánto ha pagado al año y por mes le muestre
 cuanto paga para
poder tener un control de su gasto      para este concepto.
"""
def cal_p_anual(c_mensual, p_servicio):
    pago_anual = c_mensual * p_servicio * 12
    return pago_anual

def cal_p_mensual(c_mensual, p_servicio):
    pago_mensual = c_mensual * p_servicio
    return pago_mensual

def main():
    consumo_mensual = float(input("Ingrese el consumo mensual de servicios públicos: "))
    precio_servicio = float(input("Ingrese el precio del servicio por unidad: "))

    pago_anual = cal_p_anual(consumo_mensual, precio_servicio)
    pago_mensual = cal_p_mensual(consumo_mensual, precio_servicio)

    print(f"El establecimiento paga {pago_anual} al año por servicios públicos.")
    print(f"El establecimiento paga {pago_mensual} por mes por servicios públicos.")

if __name__ == "__main__":
    main()
