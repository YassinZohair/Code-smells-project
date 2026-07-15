"""
Gym Membership Report Generator
--------------------------------
Generates usage reports for three membership tiers: Basic, Premium, and VIP.

YOUR TASK: This script works correctly, but it's riddled with duplicate code.
Refactor it so the repeated logic lives in ONE place per concept.
Do not change the printed output — only the structure of the code.
"""

basic_members = [
    {"name": "Ali", "visits": [12, 15, 9, 20]},
    {"name": "Sara", "visits": [5, 8, 6, 7]},
]

premium_members = [
    {"name": "Omar", "visits": [22, 25, 19, 30]},
    {"name": "Nour", "visits": [18, 20, 17, 21]},
]

vip_members = [
    {"name": "Yara", "visits": [28, 30, 29, 31]},
    {"name": "Karim", "visits": [26, 27, 25, 28]},
]


def print_basic_report():
    print("=== BASIC TIER REPORT ===")
    total_visits = 0
    for member in basic_members:
        visits = member["visits"]
        avg = sum(visits) / len(visits)
        highest = max(visits)
        lowest = min(visits)
        total_visits += sum(visits)
        print(f"{member['name']}: avg={avg:.1f}, max={highest}, min={lowest}")
        if avg < 10:
            print(f"  -> {member['name']} is at risk of cancelling membership")
    print(f"Total visits (Basic): {total_visits}")
    print()


def print_premium_report():
    print("=== PREMIUM TIER REPORT ===")
    total_visits = 0
    for member in premium_members:
        visits = member["visits"]
        avg = sum(visits) / len(visits)
        highest = max(visits)
        lowest = min(visits)
        total_visits += sum(visits)
        print(f"{member['name']}: avg={avg:.1f}, max={highest}, min={lowest}")
        if avg < 15:
            print(f"  -> {member['name']} is at risk of cancelling membership")
    print(f"Total visits (Premium): {total_visits}")
    print()


def print_vip_report():
    print("=== VIP TIER REPORT ===")
    total_visits = 0
    for member in vip_members:
        visits = member["visits"]
        avg = sum(visits) / len(visits)
        highest = max(visits)
        lowest = min(visits)
        total_visits += sum(visits)
        print(f"{member['name']}: avg={avg:.1f}, max={highest}, min={lowest}")
        if avg < 20:
            print(f"  -> {member['name']} is at risk of cancelling membership")
    print(f"Total visits (VIP): {total_visits}")
    print()


def print_summary():
    all_totals = 0
    for member in basic_members:
        all_totals += sum(member["visits"])
    for member in premium_members:
        all_totals += sum(member["visits"])
    for member in vip_members:
        all_totals += sum(member["visits"])
    print("=== GYM-WIDE SUMMARY ===")
    print(f"Total visits across all tiers: {all_totals}")


if __name__ == "__main__":
    print_basic_report()
    print_premium_report()
    print_vip_report()
    print_summary()