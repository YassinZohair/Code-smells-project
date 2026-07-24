readings = [
    {"time": "06:00", "temp_c": 14.2, "humidity": 78},
    {"time": "09:00", "temp_c": 19.5, "humidity": 65},
    {"time": "12:00", "temp_c": 27.8, "humidity": 40},
    {"time": "15:00", "temp_c": 31.4, "humidity": 32},
    {"time": "18:00", "temp_c": 24.1, "humidity": 55},
    {"time": "21:00", "temp_c": 18.6, "humidity": 70},
    {"time": "00:00", "temp_c": -1.0, "humidity": 90},
]

def validate_temp(readings):
    if not readings:
        print("Error: no readings provided")
        return False
    
    for r in readings:
        if r["humidity"] < 0 or r["humidity"] > 100:
            print(f"Error: invalid humidity at {r['time']}")
            return False
        if r["temp_c"] < -50 or r["temp_c"] > 60:
            print(f"Error: invalid temperature at {r['time']}")
            return False
    return True

def compute_stat(readings):
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
    return {'avg_temp':avg_temp,'avg_humidity':avg_humidity,'max_temp':max_temp,
            'min_temp':min_temp,'max_reading':max_reading,'min_reading':min_reading}

def find_alerts(stats):
    alerts = []
    if stats['max_temp'] > 30:
        alerts.append(f"HEAT WARNING: {stats['max_temp']}C recorded at {stats['max_reading']['time']}")
    if stats['min_temp'] < 0:
        alerts.append(f"FROST WARNING: {stats['min_temp']}C recorded at {stats['min_reading']['time']}")
    if stats['avg_humidity'] > 85:
        alerts.append("HIGH HUMIDITY WARNING: average humidity above 85%")
    if stats['avg_humidity'] < 20:
        alerts.append("LOW HUMIDITY WARNING: average humidity below 20%")
    return alerts

def classification(stats):
    avg_temp=stats['avg_temp']
    day_type=''
    if avg_temp < 10:
        day_type = "Cold"
    elif avg_temp < 22:
        day_type = "Mild"
    elif avg_temp < 30:
        day_type = "Warm"
    else:
        day_type = "Hot"
    return day_type

def print_report(readings,station_name,stats,day_type,alerts):
        print(f"=== Daily Weather Report: {station_name} ===")
        print(f"Readings recorded: {len(readings)}")
        print(f"Average temperature: {stats['avg_temp']:.1f}C")
        print(f"Max temperature: {stats['max_temp']}C at {stats['max_reading']['time']}")
        print(f"Min temperature: {stats['min_temp']}C at {stats['min_reading']['time']}")
        print(f"Average humidity: {stats['avg_humidity']:.1f}%")
        print(f"Day classification: {day_type}")
        if alerts:
            print("--- Alerts ---")
            for alert in alerts:
                print(f"  * {alert}")
        else:
            print("No alerts today.")
        return stats
    
if __name__ == "__main__":
    if validate_temp(readings)==True:
        stats=compute_stat(readings)
        alerts=find_alerts(stats)
        day_type=classification(stats)
        print_report(readings,'cairo central station',stats,day_type,alerts)
    else:
        print('validation error')
    

# TODO: make the functions calls in the pipeline and the print report fucntion to only print 