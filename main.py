from numbers import Number


def calculate_something(number):
    number += 5
    return number

def main():
    try:
        number = int(input("Enter your number: "))
        if number is not None:
            result = calculate_something(number)
            print(result)
        else:
            print(f"{number} - invalid number!")
    except Exception as e:
        print(f"Something went wrong - {e}")


if __name__ == '__main__':
    main()