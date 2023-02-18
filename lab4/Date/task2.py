from datetime import date , timedelta


d = date.today() - timedelta(1)
print("Yesterday:" , d)

d = date.today()
print("Today:" , d)

d = date.today() + timedelta(1)
print("Tomorrow:" , d)