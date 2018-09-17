import folium
import pandas
import webbrowser

#  getting data from the csv filr using pandas
data = pandas.read_csv("Volcanoes_USA.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# print(data)

def color_roducer(elevation):
    if elevation <= 1000:
        return "blue"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[39.209353, -85.892224], zoom_start=5, tiles="Mapbox Bright")

# It is usefull to add multiple child in the map like multiple markers on the map
fgv = folium.FeatureGroup(name="Volcanoes")

# To get the markers on my all previous homes in USA
# for coordinates in [[39.209353, -85.892224], [40.748137, -74.060691], [40.733909, -74.061057]]:

# iterate though all latitudes and longitudes in dat which we are getting from csv files
for lt,ln,el in zip(lat, lon, elev):
    # fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color=color_roducer(el)), tooltip="This is your Home"))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+" m", fill_color=color_roducer(el), color= "grey", fill_opacity=1.0, tooltip="This is your Home"))

fgp = folium.FeatureGroup(name="Population")
# read json file for population and use to create polygon layer
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
# to put the controller for selecting population or volcano view in the map
map.add_child(folium.LayerControl())

map.save("Map1.html")

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open("Map1.html")
