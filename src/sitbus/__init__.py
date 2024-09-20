from pdb import set_trace


def hello() -> str:
    return "Hello from sit-bus-py!"


if __name__ == "__main__":
    from sitbus import get_datas

    # data = get_all_data()

    # _list = data["timesheet"][0]["list"]

    # print(get_datas())

    print(get_datas())

sample = {
    "station": {
        "8:01",
        "8:10",
        "8:18",
        "8:34",
        "8:50",
    },
    "school": {
        "8:01",
        "8:10",
        "8:18",
        "8:34",
        "8:50",
    },
}


# sample["school"]["bus"][0]
