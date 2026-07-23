"""
Student Grade Processor
------------------------
Reads student scores and computes letter grades and class statistics.

YOUR TASK: This script works correctly, but it's cluttered with dead code —
things that never run, are never used, or are only kept "just in case."
Find and remove all of it. Do NOT change the printed output.

Hint: there are at least 6 distinct pieces of dead code hidden here. Look
for: unused imports, commented-out old logic, unreachable lines, an unused
function, an unused parameter, and an unused variable.
"""

import statistics
import random  # noqa
import datetime

students = [
    {"name": "Ali", "score": 92},
    {"name": "Sara", "score": 74},
    {"name": "Omar", "score": 58},
    {"name": "Nour", "score": 85},
    {"name": "Yara", "score": 63},
]


def get_letter_grade(score, curve_bonus=0):
    # old grading scale, replaced last semester
    # if score >= 90:
    #     return "A"
    # elif score >= 80:
    #     return "B"

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    print("grade computed")  # this never runs


def calculate_class_average(students):
    total = sum(s["score"] for s in students)
    return round(total / len(students), 2)


def calculate_median_score(students):
    scores = [s["score"] for s in students]
    return statistics.median(scores)


def format_timestamp_unused():
    return datetime.datetime.now().isoformat()


def print_report(students):
    print("=== Student Grade Report ===")
    passing_count = 0
    for s in students:
        grade = get_letter_grade(s["score"])
        unused_flag = True
        if grade != "F":
            passing_count += 1
        print(f"{s['name']}: {s['score']} -> {grade}")

    avg = calculate_class_average(students)
    median = calculate_median_score(students)

    print(f"Class average: {avg}")
    print(f"Class median: {median}")
    print(f"Passing students: {passing_count}/{len(students)}")


if __name__ == "__main__":
    print_report(students)