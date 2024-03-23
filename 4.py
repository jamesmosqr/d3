def obtener_ganador(votos_candidatos):
    max_votos = max(votos_candidatos.values())
    ganadores = [candidato for candidato, votos in votos_candidatos.items() if votos == max_votos]

    if len(ganadores) == 1:
        return ganadores[0]
    else:
        return "Empate"


def main():
    candidatos = ["Candidato 1", "Candidato 2", "Candidato 3"]
    votos_candidatos = {candidato: 0 for candidato in candidatos}

    num_electores = 10
    for i in range(num_electores):
        print(f"Electror {i + 1}: ¿Por quién vota? (1: Candidato 1, 2: Candidato 2, 3: Candidato 3)")
        voto = int(input("Ingrese el número correspondiente al candidato: "))

        if voto >= 1 and voto <= 3:
            votos_candidatos[candidatos[voto - 1]] += 1
        else:
            print("Voto inválido, por favor intente de nuevo.")

    ganador = obtener_ganador(votos_candidatos)

    print("\nResultado del escrutinio:")
    for candidato, votos in votos_candidatos.items():
        print(f"{candidato}: {votos} votos")

    print("\nEl ganador de las elecciones es:", ganador)


if __name__ == "__main__":
    main()
