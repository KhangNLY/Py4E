score = input("Enter Score: ")
float(score)
if float(score) >= 1.0:
    print("INVALID")
elif float(score) >= 0.9:
    print("A")
elif float(score) >= 0.8:
    print("B")
elif float(score) >= 0.7:
    print("C")
elif float(score) >= 0.6:
    print("D")
else:
    print("F")
