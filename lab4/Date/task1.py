from datetime import date,timedelta

for i in range(1,6):
    d1 = date.today() + timedelta(i - 1)
    print(f"Day {i};", d1)