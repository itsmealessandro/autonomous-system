import json,random
from time import sleep

FILE_PATH = "/simulated_env/env.json"
# Lettura dal file
try:
    i=0
    while(i<10):
        sleep(1)
        i=i+1
        # Leggi il contenuto del file
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

        # Modifica il valore di data1.value_x
        if "data1" in data and "value_x" in data["data1"]:
            val= random.randint(0,5)
            data["data1"]["value_x"] = val  # Imposta "b" come nuovo valore
        else:
            print("Chiave data1.value_x non trovata!")

        # Scrivi il nuovo contenuto nel file
        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

        print("File aggiornato con successo!")
except Exception as e:
    print(f"Errore nella lettura/scrittura del file: {e}")
