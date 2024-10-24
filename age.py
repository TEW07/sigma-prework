from datetime import datetime as dt


def main():
    date_input = input("Enter your birthdate in format: DD-MM-YYYY \n")
    birthdate = dt.strptime(date_input, "%d-%m-%Y")
    today = dt.today()

    print("Input Date:", birthdate.strftime("%d-%m-%Y"))
    print("Today's Date:", today.strftime("%d-%m-%Y"))

    age_years = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    # Here we subtract 1 if we have not reached the birthday or given date

    print("You are", age_years, "years old")


main()
