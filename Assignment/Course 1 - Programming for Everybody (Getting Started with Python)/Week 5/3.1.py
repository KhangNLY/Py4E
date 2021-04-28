hrs = input("Enter Hours:")
xx = input("Enter the Rate:")
try:
    h = float(hrs)
    x = float(xx)
except:
    print("Error, please enter numeric input")
    quit()
if h <= 40:
    print(h * x)
elif h > 40:
    print(40 * x + (h - 40) * 1.5 * x)
