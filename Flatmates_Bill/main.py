import datetime
from calendar import monthrange
from fpdf import FPDF


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
        self.day_in_house = days_in_house

    def pays(self, bill):
        qty_days = monthrange(bill.period[0], bill.period[1])[1]
        one_day = bill.amount / qty_days
        pays = self.day_in_house * one_day
        return str(round(pays, 2))


class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names,
    their due amounts and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name='house.jpg', w=30, h=30)

        # Insert Title
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=70, h=40, txt=bill.name_month(), border=0)
        pdf.cell(w=70, h=40, txt=bill.year(), border=0, ln=1)
        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=70, h=25, txt=flatmate1.pays(bill), border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=70, h=25, txt=flatmate2.pays(bill), border=0, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=120, period=(2019, 2))

fl1 = Flatmates(name="Ivan", days_in_house=20)
fl2 = Flatmates(name='Vlad', days_in_house=25)

pdf_report = PdfReport('bill.pdf')
pdf_report.generate(flatmate1=fl1, flatmate2=fl2, bill=the_bill)

