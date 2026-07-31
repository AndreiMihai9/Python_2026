import requests

URL = "https://api.open-meteo.com/v1/forecast"

p = {
    "latitude": 46.77,
    "longitude": 23.60,
    "current": "temperature_2m,wind_speed_10m",
}

r = requests.get(URL, params=p)

print("URL final:", r.url)
print("Cod de stare:", r.status_code)

if r.status_code == 200:
    d = r.json()
    print("\nCheile din raspuns:")
    for k in d:
        print(" -", k)

    print("\nContinutul cheii 'current':")
    for k, v in d["current"].items():
        print(f"  {k}: {v}")
else:
    print("Cererea a esuat.")