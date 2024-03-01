import time

seconds = int(input("set timer for how many seconds?: "))
for seconds in range(seconds,0,-1):
    print(seconds)
    time.sleep(1)
print("timer is done!")