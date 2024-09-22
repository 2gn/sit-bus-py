from requests import get as req_get
from pdb import set_trace

from datetime import *

day_types = [
    "saturday",
    "suspended",
    "vacation",
    "weekday",
    "holiday",
    "saturday-next-month",
]

def get_day_type(date: datetime) -> str:
    match date.strftime("%A"):
        case "Saturday":
            return day_types[0]
        case "Sunday":
            return day_types[4]
        case _:
            return day_types[3]

def get_current_time() -> datetime:
    return datetime.now()

def _get_data(real_index, items, key):
    return [
        str(real_index) + ":" + str(_item) for _item in items[key].split(".") if _item
    ]

def get_table() -> object:
    data = get_all_data()

    # _list = data["timesheet"][0]["list"]

    final_data = []

    for _item in data["timesheet"]:
        station_bus_times = []
        school_bus_times = []

        for index, item in enumerate(_item["list"]):
            real_index = index + 7
            for key in ["num1", "num2"]:
                station_bus_times += _get_data(real_index, item["bus_left"], key)
                school_bus_times += _get_data(real_index, item["bus_right"], key)
        final_data.append({"station": station_bus_times, "school": school_bus_times})

    return dict(zip(day_types, final_data))


def get_all_data() -> object:
    return req_get("http://bus.shibaura-it.ac.jp/db/bus_data.json").json()
