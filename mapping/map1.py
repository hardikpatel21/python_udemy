import folium
map = folium.Map(location=[39.209353, -85.892224], zoom_start=6, tiles="Mapbox Bright")

# It is usefull to add multiple child in the map like multiple markers on the map
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[39.209353, -85.892224], [40.748137, -74.060691], [40.733909, -74.061057]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Home", icon=folium.Icon(color='blue'), tooltip="This is your Home"))


map.add_child(fg)

map.save("Map1.html")
