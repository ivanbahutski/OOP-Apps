from Flatmates_Bill.flat import Bill, Flatmates
from Flatmates_Bill.report import PdfReport, FileSharer

amount = float(input('Hey, enter the bill amount: '))
period = (int(input('Enter year of staying: ')), int(input('And also Enter number of month: ')))

name1 = input('What is  your name: ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house during the bill period: '))
name2 = input('What is the name of the other flatmate? : ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house during the bill period: '))

the_bill = Bill(amount=amount, period=period)
fl1 = Flatmates(name=name1, days_in_house=days_in_house1)
fl2 = Flatmates(name=name2, days_in_house=days_in_house2)

print(f'{fl1.name} pays: ', fl1.pays(the_bill, fl2))
print(f'{fl1.name} pays: ', fl2.pays(the_bill, fl1))

pdf_report = PdfReport(f'{the_bill.year()}, {the_bill.name_month()}.pdf')
pdf_report.generate(flatmate1=fl1, flatmate2=fl2, bill=the_bill)

file_sharer = FileSharer(f'{the_bill.year()}, {the_bill.name_month()}.pdf')
print(file_sharer.share())
