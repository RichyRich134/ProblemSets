def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    val1 = d.lstrip("$")
    return float(val1)


def percent_to_float(p):
    val2 = p.rstrip("%")
    return float(val2) / 100

main()