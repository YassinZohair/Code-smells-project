import math

class coordinate:
    def __init__(self,lat,long):
        self.lat=lat
        self.long=long

    def distance_to(self, other):
        R = 6371.0
        phi1, phi2 = math.radians(self.lat), math.radians(other.lat)
        dphi = math.radians(other.lat - self.lat)
        dlambda = math.radians(other.long - self.long)
        a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(R * c, 2)

    def __str__(self):
        return f"({self.lat:.4f}, {self.long:.4f})"

stops = [
    {"name": "Warehouse", "coord": coordinate(30.0444, 31.2357)},
    {"name": "Stop A", "coord": coordinate(30.0626, 31.2497)},
    {"name": "Stop B", "coord": coordinate(30.0330, 31.2180)},
    {"name": "Stop C", "coord": coordinate(30.0561, 31.2394)},
]
    

def is_within_city_bounds(coord, city_center, radius_km):
    return coord.distance_to(city_center) <= radius_km


def print_route_summary(stops):
    print("=== Delivery Route Summary ===")
    total_distance = 0.0
    for i in range(len(stops) - 1):
        current = stops[i]
        nxt = stops[i + 1]
        d = current["coord"].distance_to(nxt["coord"])
        total_distance += d
        print(f"{current['name']} {current['coord']} -> {nxt['name']} {nxt['coord']}: {d} km")

    print(f"Total route distance: {round(total_distance, 2)} km")

    city_center = coordinate(30.0444, 31.2357)
    for s in stops:
        within = is_within_city_bounds(s["coord"], city_center, 10)
        status = "within" if within else "outside"
        print(f"{s['name']} is {status} 10km of city center")


if __name__ == "__main__":
    print_route_summary(stops)