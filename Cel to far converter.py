print("Celcius to faranhite")
def convert(a=0):
        final=(a*(9/5)+32)
        return(print(f"{a}°C × {(9/5)} + {32} = {final}°F"))
        convert(b)
while True:
    b=input("Enter the celcisus: ")
    b=float(b)
    convert(b)