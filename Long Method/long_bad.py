"""
Weather Station Daily Report
-----------------------------
Processes raw temperature/humidity readings from a weather station and
prints a daily summary report with alerts for extreme conditions.

YOUR TASK: This script works correctly, but one function is doing way too
much — validation, calculations, alert logic, AND formatting/output are all
mixed together. Refactor it into smaller, well-named functions, each with a
single responsibility. Do NOT change the printed output — only the structure.
"""

readings = [
    {"time": "06:00", "temp_c": 14.2, "humidity": 78},
    {"time": "09:00", "temp_c": 19.5, "humidity": 65},
    {"time": "12:00", "temp_c": 27.8, "humidity": 40},
    {"time": "15:00", "temp_c": 31.4, "humidity": 32},
    {"time": "18:00", "temp_c": 24.1, "humidity": 55},
    {"time": "21:00", "temp_c": 18.6, "humidity": 70},
    {"time": "00:00", "temp_c": -1.0, "humidity": 90},
]


def process_weather_report(readings, station_name):
    # --- validate readings ---
    if not readings:
        print("Error: no readings provided")
        return None

    for r in readings:
        if r["humidity"] < 0 or r["humidity"] > 100:
            print(f"Error: invalid humidity at {r['time']}")
            return None
        if r["temp_c"] < -50 or r["temp_c"] > 60:
            print(f"Error: invalid temperature at {r['time']}")
            return None

    # --- compute statistics ---
    temps = [r["temp_c"] for r in readings]
    humidities = [r["humidity"] for r in readings]

    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    avg_humidity = sum(humidities) / len(humidities)

    max_reading = None
    min_reading = None
    for r in readings:
        if r["temp_c"] == max_temp:
            max_reading = r
        if r["temp_c"] == min_temp:
            min_reading = r

    # --- determine alerts ---
    alerts = []
    if max_temp > 30:
        alerts.append(f"HEAT WARNING: {max_temp}C recorded at {max_reading['time']}")
    if min_temp < 0:
        alerts.append(f"FROST WARNING: {min_temp}C recorded at {min_reading['time']}")
    if avg_humidity > 85:
        alerts.append("HIGH HUMIDITY WARNING: average humidity above 85%")
    if avg_humidity < 20:
        alerts.append("LOW HUMIDITY WARNING: average humidity below 20%")

    # --- classify overall day type ---
    if avg_temp < 10:
        day_type = "Cold"
    elif avg_temp < 22:
        day_type = "Mild"
    elif avg_temp < 30:
        day_type = "Warm"
    else:
        day_type = "Hot"

    # --- format and print report ---
    print(f"=== Daily Weather Report: {station_name} ===")
    print(f"Readings recorded: {len(readings)}")
    print(f"Average temperature: {avg_temp:.1f}C")
    print(f"Max temperature: {max_temp}C at {max_reading['time']}")
    print(f"Min temperature: {min_temp}C at {min_reading['time']}")
    print(f"Average humidity: {avg_humidity:.1f}%")
    print(f"Day classification: {day_type}")

    if alerts:
        print("--- Alerts ---")
        for alert in alerts:
            print(f"  * {alert}")
    else:
        print("No alerts today.")

    return {
        "avg_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "avg_humidity": avg_humidity,
        "day_type": day_type,
        "alerts": alerts,
    }


if __name__ == "__main__":
    process_weather_report(readings, "Cairo Central Station")