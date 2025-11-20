import re
import random

print("=== INSERIMENTO STUDENTI ===")
studenti = []

# Inserimento nomi
while True:
    nome = input("Nome e cognome (invio per terminare): ").strip()
    if nome == "":
        break
    studenti.append(nome)

if not studenti:
    print("Nessuno studente inserito.")
    exit()

# Input testo ricerca
testo = input("\nStringa di ricerca: ").strip().lower()
print("\n=== FILTRAGGIO ===")

# ---------------------------------------
# PRIORITÀ 1 → atomo (sottostringa esatta)
# ---------------------------------------
regex1 = re.compile(re.escape(testo), re.IGNORECASE)
filtrati = [n for n in studenti if regex1.search(n)]

if filtrati:
    print("Usata PRIORITÀ 1 (atomo)")
else:
    # ---------------------------
    # PRIORITÀ 2 → gruppo chars
    # ---------------------------
    gruppo = "[" + "".join(sorted(set(testo))) + "]"
    regex2 = re.compile(gruppo, re.IGNORECASE)
    filtrati = [n for n in studenti if regex2.search(n)]

    if filtrati:
        print("Usata PRIORITÀ 2 (gruppo di caratteri)")
    else:
        # ----------------------------------
        # PRIORITÀ 3 → range min-max + spazio
        # ----------------------------------
        minimo = min(testo)
        massimo = max(testo)
        range_pattern = f"[{minimo}-{massimo} ]"
        regex3 = re.compile(range_pattern, re.IGNORECASE)
        filtrati = [n for n in studenti if regex3.search(n)]
        print("Usata PRIORITÀ 3 (range min-max + spazio)")

# Mostra filtrati
print("\nNominativi filtrati:", filtrati)

# ---------------------------------------
# Estrazione di massimo 3 nominativi
# ---------------------------------------
if len(filtrati) > 3:
    estratti = random.sample(filtrati, 3)
else:
    estratti = filtrati

print("\n=== SELEZIONE FINALE ===")
print("Nominativi estratti:", estratti)
