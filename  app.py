# app.py
import streamlit as st
import folium
from streamlit_folium import st_folium
from src.pathfinder import FlightPathFinder
from src.exporter import export_to_mavlink

st.set_page_config(page_title="AeroRoute Flight Planner", layout="wide")

st.title("🛩️ AeroRoute: Autonomous Fixed-Wing Flight Planner")
st.markdown("Plan optimized drone waypoints, avoid no-fly zones, and export ArduPilot-ready missions.")

# Sidebar Controls
st.sidebar.header("Mission Parameters")
cruise_altitude = st.sidebar.slider("Cruise Altitude (m)", 50, 500, 100)
min_turning_radius = st.sidebar.number_format = st.sidebar.slider("Turning Radius (m)", 10, 100, 25)

# Main layout: Map view
st.subheader("Interactive Mission Map")
# Default center: Tokyo / Ueno area or a test zone
m = folium.Map(location=[35.7148, 139.7774], zoom_start=14)

# Render map in Streamlit
output = st_folium(m, width=700, height=500)

# Export Section
st.subheader("Export Mission")
if st.button("Generate MAVLink .waypoints File"):
    # Sample test waypoints
    sample_wps = [
        (35.7148, 139.7774, cruise_altitude),
        (35.7200, 139.7800, cruise_altitude),
        (35.7250, 139.7750, cruise_altitude)
    ]
    file_path = export_to_mavlink(sample_wps)
    with open(file_path, "r") as f:
        st.download_button("Download mission.waypoints", f, file_name="mission.waypoints")