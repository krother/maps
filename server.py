"""
1. install flask
2. FLASK_APP=server.py flask run
"""
from flask import Flask
import folium
from folium.features import CustomIcon

app = Flask(__name__)

@app.route("/")
def show_map():
    berlin = folium.Map(location=[52.50, 13.35], 
        zoom_start=10, tiles='stamen watercolor')

    html_map = berlin.get_root().render()

    return f"""
<html>
  <body>
    { html_map }
  </body>
</html>"""
