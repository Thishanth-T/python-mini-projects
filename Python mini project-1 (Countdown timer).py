import time
duration = int(input("Enter the time you want in seconds:"))
for i in range(duration,0,-1):
    seconds = i % 60
    minutes = (i//60) % 60
    hours = i//3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times UP!!!")