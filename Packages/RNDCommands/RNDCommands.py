import serial

def IDN(self):
    SP = serial.Serial()

    try:
        SP.write("*IDN?")
        SP.
    except serial.SerialException as e:
        print(e.errno)

    return