from datetime import datetime, date

while True:
    day = input('Please input the date to calculate the age from (dd/mm/yy):\n')

    try:
        birthday = datetime.strptime(day, '%d/%m/%y')
        break
    except ValueError as err:
        print(
            f"[ERROR: {err}] Please input a valid date following the given format.")


age = date.today().year - birthday.year
if date.today().month < birthday.month:
    print(f"This person is {age-1} years old.")
else:
    print(f"This person is {age} years old.")
