import json
import time

FILE_PATH = "/simulated_env/env.json"
# Lettura dal file
try:

    i=0
    while(i<10):
        i=i+1
        time.sleep(1)
        with open(FILE_PATH, "r") as file:
            data = json.load(file)  # Carica il JSON

            # Estrai il valore di "value_x"
            value_x = data.get("data1", {}).get("value_x", None)

            if value_x is not None:
                print(f"valore  : {value_x}")
            else:
                print("Errore: valore 'value_x' non trovato nel JSON.")
except FileNotFoundError:
    print(f"Errore: il file {FILE_PATH} non esiste.")
except json.JSONDecodeError:
    print(f"Errore: il file {FILE_PATH} non è un JSON valido.")
