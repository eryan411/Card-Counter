def find_count(value):
    if value == "2" or value == "3" or value == "4" or value == "5" or value == "6":
        return 1
    elif value == "7" or value == "8" or value == "9":
        return 0
    elif value == "10" or value.lower() == "a" or value.lower() == "j" or value.lower() == "q" or value.lower() == "k":
        return -1
    else:
        return 0


if __name__ != '__main__':
    pass
else:
    total = 0
    runProgram = True
    while runProgram:
        count = 0
        card = input("Card:")
        if card.lower() == "reset":
            total = 0
        elif card.lower() == "stop":
            runProgram = False
        else:
            total += find_count(card)
        print(f"Count is {total}")
