import smbus2
import bme280
import time
import matplotlib.pyplot as plt
from datetime import datetime
timestamps_values = []
temperature_celsius_values = []
humidity_values = []
pressure_values = []


bus = smbus2.SMBus(1)

address = 0x76
calibration_params = bme280.load_calibration_params(bus, address)


running = True
while running:
    try:
        data = bme280.sample(bus, address, calibration_params)
        
        timestamp_value = data.timestamp
        temperature_celsius_value = data.temperature
        humidity_value = data.humidity
        pressure_value = data.pressure
        
        timestamps_values.append(timestamp_value)
        temperature_celsius_values.append(temperature_celsius_value)
        humidity_values.append(humidity_value)
        pressure_values.append(pressure_value)
        
        
        for i, (ax, values, label) in enumerate(
            zip(axs, [temperature_celsius_values, humidity_values, pressure_values], ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)'])):
            ax.clear()
            ax.plot(timestamps, values, label=label)
            ax.legend()
            ax.set_ylabel(label)
        axs[-1].set_xlabel('Time')
        fig.autofmt_xdata(rotation=45)
        plt.pause(1)
            
        
    
        
        time.sleep(1)
    except KeyboardInterrupt:
        print('Program stopped')
        running = False
    except Exception as e:
        print("Une erreur c'est produite", str(e))
        running = False
        
    

    