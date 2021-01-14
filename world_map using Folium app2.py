import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")
map1 = folium.Map(location=[38,-99],zoom_start=4, tiles = "Stamen Terrain")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_indicator(elevation):
#    for i in elev:
        if elevation<1000:
            return "green"
        elif elevation>=1000 and elevation<2000:
            return "orange"
        else:
            return "red"

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
#    map1.add_child(folium.Marker(location=[lt,ln], popup = el , icon = folium.Icon(color=color_indicator(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup = el, fill_color = color_indicator(el), fill = True, color = "grey",fill_opacity = 0.6))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x["properties"]["POP2005"]<1000000 
else 'orange' if 1000000 <= x["properties"]["POP2005"] < 2000000
else 'red' }))

map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())

map1.save("WorldMap.html")