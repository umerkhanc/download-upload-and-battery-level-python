import psutil
import speedtest

# Get system battery information
battery = psutil.sensors_battery()

# Get system network information
speed_test = speedtest.Speedtest()
download_speed = speed_test.download() / 10**6
upload_speed = speed_test.upload() / 10**6

# Print system information
print(f"Battery Level: {battery.percent}%")
print(f"Download Speed: {download_speed:.2f} Mbps")
print(f"Upload Speed: {upload_speed:.2f} Mbps")