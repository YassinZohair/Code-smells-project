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

def member_summary(members_list,limit,label):
    total_visits=0
    for member in members_list:
        visits = member["visits"]
        avg = sum(visits) / len(visits)
        highest = max(visits)
        lowest = min(visits)
        total_visits+=sum(visits)
        print(f'{member['name']}: avg={avg:.1f}, max={highest}, min={lowest}')
        if avg<limit:
            print(f"  -> {member['name']} is at risk of cancelling membership")
    print(f"Total visits:{label} {total_visits}")
    return total_visits


def print_basic_report():
    print("=== BASIC TIER REPORT ===")
    total=member_summary(basic_members,10,'Basic')
    print()
    return total


def print_premium_report():
    print("=== PREMIUM TIER REPORT ===")
    total=member_summary(premium_members,15,'Premium')
    print()
    return total 


def print_vip_report():
    print("=== VIP TIER REPORT ===")
    total=member_summary(vip_members,20,'VIP')
    print()
    return total


def print_summary(all_totals):
   
    print("=== GYM-WIDE SUMMARY ===")
    print(f"Total visits across all tiers: {sum(all_totals)}")


if __name__ == "__main__":
    basic_total=print_basic_report()
    premium_total=print_premium_report()
    vip_total=print_vip_report()
    print_summary([basic_total,vip_total,premium_total])