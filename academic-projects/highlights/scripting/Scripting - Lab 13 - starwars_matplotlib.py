import requests
import json
import matplotlib.pyplot as plt

def api_call(url):
    response = requests.get(url)
    json_response = json.loads(response.text)
    return json_response

planet_list = []
diameter = []
population = []
surface_water = []
endpoint_url = "https://swapi.dev/api/planets/"


while endpoint_url:
    results = api_call(endpoint_url)
    planet_info = results["results"]
    
    for planet in planet_info:
        pop = planet.get("population")
        dia = planet.get("diameter")
        wat = planet.get("surface_water")

        if pop == "unknown" or pop == "0":
            continue
        if dia == "unknown" or dia == "0":
            continue
        if wat == "unknown" or wat == "0":
            continue

        population.append(int(pop))
        diameter.append(int(dia))
        surface_water.append(float(wat))
        planet_list.append(planet.get("name"))
        
    endpoint_url = results.get("next")

fig, (ax0, ax1, ax2) = plt.subplots(3, 1, layout="constrained")

ax0.set_xlabel("Planet")
ax0.set_ylabel("Diameter")
ax1.set_xlabel("Planet")
ax1.set_ylabel("Population")
ax2.set_xlabel("Planet")
ax2.set_ylabel("Water Surface")

ax0.plot(planet_list, diameter, label = "Diameter") 
ax1.plot(planet_list, population, label = "Population") 
ax2.plot(planet_list, surface_water, label = "Water Surface") 
ax0.legend()
ax1.legend()
ax2.legend()
plt.show()