from calendar import monthrange


class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:
    """
    Creates a flatmate person who lives in the
    flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.day_in_house = days_in_house

    def pays(self, bill):
        if type(self.day_in_house) == int:
            num_days = monthrange(bill.period[0], bill.period[1])[1]
            one_day = bill.amount / num_days
            pays = self.day_in_house * one_day
            return pays

        else:
            kf1 = self.day_in_house[0] / (sum([d for d in self.day_in_house]))
            kf2 = self.day_in_house[1] / (sum([d for d in self.day_in_house]))
            return bill.amount * kf1, bill.amount * kf2


class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names,
    their due amounts and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period=(2019, 2))
# fl = Flatmates(name=["John", "Marry"], days_in_house=[20, 25])
fl = Flatmates(name="Ivan", days_in_house=20)

print(fl.pays(bill=the_bill))
# print(marry.pays(bill=the_bill))
