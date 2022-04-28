def encode(year):
    sol = ""
    decimalRomanMap = {'M': 1000, "CM": 900, 'D': 500, 'CD': 400, 'C': 100,
                       'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    i = 0
    number = year

    while number:
        currentDecimal = list(decimalRomanMap.values())[i]
        div = number // currentDecimal
        number %= currentDecimal

        while div:
            sol += list(decimalRomanMap.keys())[i]
            div -= 1

        i += 1

    return sol


if __name__ == "__main__":
    year = 2020
    print(f"Current Year {year} in Roman literals: {encode(year)}\n")
