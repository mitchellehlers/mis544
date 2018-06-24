import datetime


def get_current_time_as_str():
    return str(datetime.datetime.now()).replace(" ", "_")


