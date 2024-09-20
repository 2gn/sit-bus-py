from requests import get as req_get
from pdb import set_trace


def get_next_bus() -> object:
    raise NotImplementedError
    return {"time": None, "from": None}


def get_last_bus() -> object:
    raise NotImplementedError


def _get_data(real_index, items, key):
    return [
        str(real_index) + ":" + str(_item) for _item in items[key].split(".") if _item
    ]


def get_datas() -> object:
    data = get_all_data()

    # _list = data["timesheet"][0]["list"]

    keys = [
        "saturday",
        "suspended",
        "vacation",
        "weekday",
        "holiday",
        "saturday-next-month",
    ]
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

    return dict(zip(keys, final_data))


def get_all_data() -> object:
    return req_get("http://bus.shibaura-it.ac.jp/db/bus_data.json").json()
