import json
import os
import requests

URL_GEO = "https://geocoding-api.open-meteo.com/v1/search"
URL_MET = "https://api.open-meteo.com/v1/forecast"
FIS = "favorite.json"

ZILE = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]


def descriere(cod):
    """Traduce codul WMO intr-un text lizibil."""
    if cod == 0:
        return "senin"
    elif cod <= 3:
        return "partial noros"
    elif cod <= 48:
        return "ceata"
    elif cod <= 57:
        return "burnita"
    elif cod <= 67:
        return "ploaie"
    elif cod <= 77:
        return "ninsoare"
    elif cod <= 82:
        return "averse"
    elif cod <= 86:
        return "averse de ninsoare"
    else:
        return "furtuna"


def incarca():
    if os.path.exists(FIS):
        with open(FIS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salveaza(ors):
    with open(FIS, "w", encoding="utf-8") as f:
        json.dump(ors, f, indent=4, ensure_ascii=False)


def cauta_oras(nume):
    p = {"name": nume, "count": 1, "language": "ro", "format": "json"}
    r = requests.get(URL_GEO, params=p)

    if r.status_code != 200:
        print("Serviciul de cautare nu raspunde.")
        return None
    d = r.json()

    if "results" not in d:
        print(f"Orasul '{nume}' nu a fost gasit.")
        return None

    g = d["results"][0]
    return {
        "nume": g["name"],
        "tara": g.get("country", "?"),
        "lat": g["latitude"],
        "lon": g["longitude"],
    }

def vremea_acum(c):
    p = {
        "latitude": c["lat"],
        "longitude": c["lon"],
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,"
                   "wind_speed_10m,weather_code",
        "timezone": "auto",
    }
    r = requests.get(URL_MET, params=p)

    if r.status_code != 200:
        print("Nu am putut prelua datele meteo.")
        return

    cur = r.json()["current"]
    print(f"\n--- {c['nume']}, {c['tara']} ---")
    print(f"Cer: {descriere(cur['weather_code'])}")
    print(f"Temperatura: {cur['temperature_2m']} C (resimtita {cur['apparent_temperature']} C)")
    print(f"Umiditate: {cur['relative_humidity_2m']}%")
    print(f"Vant: {cur['wind_speed_10m']} km/h")


def prognoza(c, nzile=3):
    p = {
        "latitude": c["lat"],
        "longitude": c["lon"],
        "daily": "temperature_2m_max,temperature_2m_min,weather_code,"
                 "precipitation_probability_max",
        "forecast_days": nzile,
        "timezone": "auto",
    }
    r = requests.get(URL_MET, params=p)

    if r.status_code != 200:
        print("Nu am putut prelua prognoza.")
        return

    zl = r.json()["daily"]
    print(f"\n--- Prognoza {nzile} zile: {c['nume']} ---")

    for i in range(len(zl["time"])):
        data = zl["time"][i]
        an, ln, zi = data.split("-")
        print(f"{zi}.{ln}  {zl['temperature_2m_min'][i]:5} / "
              f"{zl['temperature_2m_max'][i]:5} C  "
              f"{descriere(zl['weather_code'][i]):20} "
              f"ploaie {zl['precipitation_probability_max'][i]}%")

def listeaza(ors):
    if len(ors) == 0:
        print("Nu ai orase favorite.")
        return False
    print("\nOrase favorite:")
    for i, o in enumerate(ors, start=1):
        print(f"{i}. {o['nume']}, {o['tara']}")
    return True


def alege_favorit(ors):
    """Afiseaza favoritele si intoarce orasul ales, sau None."""
    if not listeaza(ors):
        return None
    n = input("Numarul orasului: ").strip()
    if not n.isdigit() or int(n) < 1 or int(n) > len(ors):
        print("Optiune invalida.")
        return None
    return ors[int(n) - 1]


ors = incarca()

while True:
    print("\n===== APLICATIE METEO =====")
    print("1. Vremea acum (oras nou)")
    print("2. Prognoza 3 zile (oras nou)")
    print("3. Adauga oras la favorite")
    print("4. Vremea pentru un favorit")
    print("5. Listeaza favoritele")
    print("6. Sterge un favorit")
    print("0. Iesire")

    op = input("Optiune: ").strip()

    if op == "1":
        c = cauta_oras(input("Oras: ").strip())
        if c is not None:
            vremea_acum(c)

    elif op == "2":
        c = cauta_oras(input("Oras: ").strip())
        if c is not None:
            prognoza(c)

    elif op == "3":
        c = cauta_oras(input("Oras: ").strip())
        if c is not None:
            ors.append(c)
            salveaza(ors)
            print(f"{c['nume']} a fost adaugat la favorite.")

    elif op == "4":
        o = alege_favorit(ors)
        if o is not None:
            vremea_acum(o)
            prognoza(o)

    elif op == "5":
        listeaza(ors)

    elif op == "6":
        o = alege_favorit(ors)
        if o is not None:
            ors.remove(o)
            salveaza(ors)
            print(f"{o['nume']} a fost sters.")

    elif op == "0":
        salveaza(ors)
        print("Datele au fost salvate. La revedere!")
        break

    else:
        print("Optiune invalida.")