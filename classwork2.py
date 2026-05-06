import re


def no(number: str) -> bool:

    pattern = r"(98)-\d{4}-\d{4}"

    return bool(re.fullmatch(pattern, number))


def main():

    while True:

        number: str = input("Enter number: ").strip()

        if not number:
            print("Number cannot be empty")
            continue

        if no(number):
            print("Valid Number")
            break

        else:
            print("Invalid Number")
            print("Please type the number in this format: 98-1234-5678")


main()