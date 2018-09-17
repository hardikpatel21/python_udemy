import folium
import pandas

#  getting data from the csv filr using pandas
data = pandas.read_csv("Volcanoes_USA.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# print(data)

map = folium.Map(location=[39.209353, -85.892224], zoom_start=6, tiles="Mapbox Bright")

# It is usefull to add multiple child in the map like multiple markers on the map
fg = folium.FeatureGroup(name="My Map")

# To get the markers on my all previous homes in USA
# for coordinates in [[39.209353, -85.892224], [40.748137, -74.060691], [40.733909, -74.061057]]:

# iterate though all latitudes and longitudes in dat which we are getting from csv files
for lt,ln,el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color='blue'), tooltip="This is your Home"))


map.add_child(fg)

map.save("Map1.html")
