from enum import Enum

class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

    @classmethod
    def get_name(cls, month_number: int) -> str:
        for month in cls:
            if month.value == month_number:
                return month.name
        raise ValueError(f"Invalid month number: {month_number}")