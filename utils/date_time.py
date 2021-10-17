import datetime as dt

def process_date_time(execution_date, times):
    # 19:58:57 -> 2021-10-13 19:58:57
    for time in times:
        ti = time["start_time"]
        time["start_time"] = execution_date + " " + ti

        tf = time["end_time"]
        time["end_time"] = execution_date + " " + tf

    return times

def diff_hours(start, end):
    format = "%H:%M:%S"

    diff = dt.datetime.strptime(end, format) - dt.datetime.strptime(start, format)

    return diff.total_seconds()
