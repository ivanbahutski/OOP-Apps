import os
import webbrowser
from filestack import Client
from fpdf import FPDF


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
        pdf.image(name='pictures/house.jpg', w=30, h=30)

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
        pdf.cell(w=70, h=25, txt=flatmate1.pays(bill, flatmate2), border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=70, h=25, txt=flatmate2.pays(bill, flatmate1), border=0, ln=1)

        os.chdir('files')

        pdf.output(self.filename)

        webbrowser.open('file://' + os.path.realpath(self.filename))


class FileSharer:
    def __init__(self, filepath, api_key='ANdcaMgMStGjk6qt3UAbWz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url

# For developer
# https://replit.com/@IvanBahutski/Flatmates#main.py

# For users
# https://replit.com/@IvanBahutski/Flatmates?embed=1
