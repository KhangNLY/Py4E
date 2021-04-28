largest = None
smallest = None

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try:
        num = int(inp)
    except ValueError:
        print("You enter an invalid number, it must be an integer\nEnter again")
        continue
    if smallest is None and largest is None:
        smallest = num
        largest = num
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num


def done(largest, smallest):
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))


done(largest, smallest)
