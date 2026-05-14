import requests
import json
import pandas as pd
import plotly.express as px

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

data = pd.DataFrame({
    "population": population,
    "planet_list": planet_list,
    "diameter": diameter,
    "surface_water": surface_water
})

fig1 = px.scatter(
    data, 
    x="surface_water", 
    y="diameter", 
    size="population",
    hover_name="planet_list",
    title="Star Wars Pandas Bubble Plot",
    labels={'surface_water': 'Surface Water (%)', 'diameter': 'Diameter (km)', 'population': 'Population'}
)
fig1.show()

#Extra credit!
filtered_data = data[data['population'] < 27000000000]

fig2 = px.scatter(
    filtered_data,
    x="surface_water", 
    y="diameter", 
    size="population",
    hover_name="planet_list",
    title="Star Wars Pandas Bubble Plot",
    labels={'surface_water': 'Surface Water (%)', 'diameter': 'Diameter (km)', 'population': 'Population'}
)

fig2.show()