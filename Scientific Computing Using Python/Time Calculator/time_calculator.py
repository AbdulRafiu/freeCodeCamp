def add_time(start, duration, day=False):
    time, am_pm = start.split()
    hours, minutes = time.split(':')
    hours_to_add, minutes_to_add = duration.split(':')
    new_hours = int(hours) + int(hours_to_add)
    new_minutes = int(minutes) + int(minutes_to_add)
    if new_minutes >= 60:
        new_hours += 1
    day_count = new_hours // 24
    new_hours = new_hours % 24
    if 12 <= new_hours <= 24:
        if am_pm == 'AM':
            am_pm = 'PM'
        elif am_pm == 'PM':
            am_pm = 'AM'
            day_count += 1
    new_hours = new_hours % 12
    if new_hours == 0:
        new_hours = 12
    new_minutes = new_minutes % 60
    if day:
        day_table = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
        day = day_table[day.capitalize()]
        if not (day + day_count == 7):
            day = (day + day_count) % 7
        else:
            day = 7
        day = list(day_table.keys())[list(day_table.values()).index(day)]
        if day_count > 0:
            if day_count == 1:
                new_time = str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + \
                           am_pm + ", " + day + " (next day)"
            else:
                new_time = str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + am_pm + \
                           ", " + day + " (" + str(day_count) + " days later)"
        else:
            new_time = str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + am_pm + ", " + day

    elif day_count > 0:
        if day_count == 1:
            new_time = str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + am_pm + " (next day)"
        else:
            new_time = str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + am_pm + \
                       " (" + str(day_count) + " days later)"
    else:
        new_time = str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + am_pm
    return new_time
