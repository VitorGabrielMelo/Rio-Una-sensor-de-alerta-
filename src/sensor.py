import random
import time
from datetime import datetime

# Nível do rio em metros (valores simulados)
NIVEL_MINIMO = 0.5
NIVEL_MAXIMO = 8.0
INTERVALO_SEGUNDOS = 5


def ler_nivel():
    """Simula a leitura do sensor e devolve o nível do rio em metros."""
    return round(random.uniform(NIVEL_MINIMO, NIVEL_MAXIMO), 2)


def main():
    print("Sensor simulado do Rio Una (Ctrl+C para parar)")
    while True:
        nivel = ler_nivel()
        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{hora}] Nível do rio: {nivel} m")
        time.sleep(INTERVALO_SEGUNDOS)


if __name__ == "__main__":
    main()
