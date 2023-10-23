import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Connection string for your IoT device
CONNECTION_STRING = "HostName=hung-csce438.azure-devices.net;DeviceId=parkey-camera;SharedAccessKey=UGp1CUljsmLm0vpd+8V49y2UPrpbOFfZwAIoTIkHNOU="

# Create an IoT Hub device client
device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Start the device client
device_client.connect()

try:
    while True:
        # Simulate sensor data
        temperature = random.randint(1, 20)
        humidity = random.randint(6, 10)
        time_stamp = time.time()
        # Create a JSON message

        message = Message('{"eventId": ' + str(temperature) + ', "humidity": ' + str(humidity) + ', "time": ' + str(time_stamp) + '}')

        # Send the message to the IoT Hub
        device_client.send_message(message)

        print(f"Message sent: {message}")

        time.sleep(30)

except KeyboardInterrupt:
    print("Data sending stopped.")
    device_client.disconnect()

