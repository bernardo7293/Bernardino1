from serial import Serial

def start_communication():
    comport = Serial('COM25', 9600, timeout=5)

    return comport
