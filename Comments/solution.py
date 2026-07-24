# list of packages, w=weight in kg, d=distance in km, e=is express
pkgs = [
    {"weight": 2.5, "distance": 120, "express": False},
    {"weight": 8.0, "distance": 450, "express": True},
    {"weight": 1.2, "distance": 30, "express": False},
    {"weight": 15.0, "distance": 900, "express": True},
]


def calc(package):
    base_rate = 2.0
    cost_per_kg = package["weight"] * 1.5
    cost_per_km = package["distance"] * 0.02

    total = base_rate + cost_per_kg + cost_per_km

    # if express, multiply by 1.5 (express surcharge)
    if package["express"]:
        total = total * 1.5

    # apply a cap - shipping can never cost more than 200
    if total > 200:
        total = 200
    return round(total, 2)


def est_days(package):
    distance = package["distance"]
    express = package["express"]

    # base calculation: 1 day per 200km, minimum 1 day
    days = distance / 200
    if days < 1:
        days = 1
    if express:
        days = days / 2

    # round up because you can't have partial days
    import math
    days = math.ceil(days)

    return days


def process_all(packages):
    for p in packages:
        cost = calc(p)
        days = est_days(p)
        print(f"Package ({p['weight']}kg, {p['distance']}km, express={p['express']}): "
              f"${cost}, {days} day(s)")


if __name__ == "__main__":
    process_all(pkgs)