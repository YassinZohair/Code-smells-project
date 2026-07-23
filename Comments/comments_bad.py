"""
Shipping Cost Calculator
-------------------------
Calculates shipping cost and delivery estimates for packages.

YOUR TASK: This script works correctly, but it leans on comments to explain
things the CODE should be saying instead (unclear names, magic numbers,
tangled logic) — plus some comments that are just noise. Refactor by:
  1. Renaming variables/functions so they're self-explanatory
  2. Replacing magic numbers with named constants
  3. Deleting comments that become unnecessary once the code is clear
  4. KEEPING any comment that explains a "why" no renaming could replace

Do NOT change the printed output — only the structure/clarity of the code.
"""

# list of packages, w=weight in kg, d=distance in km, e=is express
pkgs = [
    {"w": 2.5, "d": 120, "e": False},
    {"w": 8.0, "d": 450, "e": True},
    {"w": 1.2, "d": 30, "e": False},
    {"w": 15.0, "d": 900, "e": True},
]


def calc(p):
    # base rate is 2 dollars
    b = 2.0
    # cost per kg is 1.5
    c = p["w"] * 1.5
    # cost per km, very small per-unit rate
    dcost = p["d"] * 0.02

    total = b + c + dcost

    # if express, multiply by 1.5 (express surcharge)
    if p["e"]:
        total = total * 1.5

    # apply a cap - shipping can never cost more than 200
    if total > 200:
        total = 200

    return round(total, 2)


def est_days(p):
    # d is distance
    d = p["d"]
    # e is express flag
    e = p["e"]

    # base calculation: 1 day per 200km, minimum 1 day
    days = d / 200
    if days < 1:
        days = 1

    # express cuts time in half
    if e:
        days = days / 2

    # round up because you can't have partial days
    import math
    days = math.ceil(days)

    return days


def process_all(pkgs):
    # loop through all packages
    for p in pkgs:
        # calculate cost
        cost = calc(p)
        # calculate days
        days = est_days(p)
        # print the result
        print(f"Package ({p['w']}kg, {p['d']}km, express={p['e']}): "
              f"${cost}, {days} day(s)")


if __name__ == "__main__":
    # run the processing
    process_all(pkgs)