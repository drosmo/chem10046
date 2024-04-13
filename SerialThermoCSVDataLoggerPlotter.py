import serial
import csv
import time
import tkinter as tk
from threading import Thread

# Open serial port (COM port may vary)
ser = serial.Serial('COM6', 9600)

# Create a new Tkinter window
window = tk.Tk()
window.title("Arduino Data")

# Create a StringVar to hold the temperature data
temp_data = tk.StringVar()
temp_data.set("Temperature: ")

# Create a label that displays the temperature data
temp_label = tk.Label(window, textvariable=temp_data)
temp_label.pack()

# Function to read and write data
def read_and_write_data():
    # Open or create a CSV file
    with open('arduino_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature"])

        # Read serial data
        while True:
            # Read a line from the serial port
            data = ser.readline().decode('utf-8').rstrip()

            # Write timestamp and data to CSV
            writer.writerow([time.ctime(), data])

            # Update the temperature data
            temp_data.set("Temperature: " + data)

# Run the function in a new thread
Thread(target=read_and_write_data).start()

# Start the Tkinter event loop
window.mainloop()
