"""
Delivery Route Distance Tracker
---------------------------------
Tracks delivery stops using GPS coordinates and computes distances between
them along a route.

YOUR TASK: This script works correctly, but the same group of fields keeps
reappearing together across multiple functions — a classic Data Clump.
Find the repeating group, bundle it into a class, and refactor all
functions to use it. Do NOT change the printed output.

Hint: use the "delete one field, does the rest still make sense" test on
each parameter pair/group you find repeating.
"""

import math

stops = [
    {"name": "Warehouse", "lat": 30.0444, "lon": 31.2357},
    {"name": "Stop A", "lat": 30.0626, "lon": 31.2497},
    {"name": "Stop B", "lat": 30.0330, "lon": 31.2180},
    {"name": "Stop C", "lat": 30.0561, "lon": 31.2394},
]


def distance_km(lat1, lon1, lat2, lon2):
    # Haversine formula
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)


def format_coordinates(lat, lon):
    return f"({lat:.4f}, {lon:.4f})"


def is_within_city_bounds(lat, lon, city_lat, city_lon, radius_km):
    return distance_km(lat, lon, city_lat, city_lon) <= radius_km


def print_route_summary(stops):
    print("=== Delivery Route Summary ===")
    total_distance = 0.0
    for i in range(len(stops) - 1):
        current = stops[i]
        nxt = stops[i + 1]
        d = distance_km(current["lat"], current["lon"], nxt["lat"], nxt["lon"])
        total_distance += d
        print(f"{current['name']} {format_coordinates(current['lat'], current['lon'])} "
              f"-> {nxt['name']} {format_coordinates(nxt['lat'], nxt['lon'])}: {d} km")

    print(f"Total route distance: {round(total_distance, 2)} km")

    cairo_center_lat, cairo_center_lon = 30.0444, 31.2357
    for s in stops:
        within = is_within_city_bounds(s["lat"], s["lon"], cairo_center_lat, cairo_center_lon, 10)
        status = "within" if within else "outside"
        print(f"{s['name']} is {status} 10km of city center")


if __name__ == "__main__":
    print_route_summary(stops)