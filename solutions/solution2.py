"""
Exercise 2: Draw coordinates

Draw the coordinates from data/exercise2.txt
using bare Python
"""
import folium

f = open('../data/exercise2.txt')  # <- if this doesnt work try full path

coord = []  # prepare an empty list in which we collect entries
for line in f:  # go through file line by line
    columns = line.split(',')  # separate columns
    district = columns[0]
    lat = float(columns[1])  # convert to float number
    lon = float(columns[2])
    coord .append((lat, lon)) # append coordinate tuple

print(coord)  # see what we got
print(len(coord))

# create a map
berlin = folium.Map(location=[52.50, 13.35],
                    zoom_start=10, tiles='stamenterrain')

for c in coord:  # go through all coordinates
    mark = folium.Marker(c)  # icon + popup are optional
    mark.add_to(berlin)

berlin.save('map.html')

