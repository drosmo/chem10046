import serial
import csv
import time

# Open serial port (COM port may vary)
ser = serial.Serial('COM6', 9600)

# Open or create a CSV file
with open('arduino_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature"])

    # Read serial data
    while True:
        try:
            # Read a line from the serial port
            data = ser.readline().decode('utf-8').rstrip()

            # Write timestamp and data to CSV
            writer.writerow([time.ctime(), data])

        except KeyboardInterrupt:
            # Exit the loop when Ctrl+C is pressed
            break
