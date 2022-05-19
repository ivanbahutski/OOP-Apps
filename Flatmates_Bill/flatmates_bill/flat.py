import datetime


class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    def name_month(self):
        month_num = self.period[1]
        month_object = datetime.datetime.strptime(str(month_num), "%m")
        full_month_name = month_object.strftime("%B")
        return full_month_name

    def year(self):
        year_str = str(self.period[0])
        return year_str


class Flatmates:
    """
    Creates a flatmate person who lives in the
    flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return str(round(to_pay, 2))
