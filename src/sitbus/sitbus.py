from .utils import *

class TableFetcher():
    def __init__(self):
        self.table = get_table()

    def get_next_bus(
        self,
        where: str = "school",
        currentTime: datetime =get_current_time()
    ):
        print(self.table)
        day_type = get_day_type(currentTime)
        for index, date in enumerate(self.table[day_type][where]):
            if date > currentTime:
                return date[index - 1]
        raise "No next bus found"
