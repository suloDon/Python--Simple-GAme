import time


def timer():
    while True:
        time_ = int(input("Enter time in second which you want to set"))
        for i in range(time_, 0, -1):
            second = i % 60
            minute = int((i / 60) % 60)
            hour = int(i / 3600)
            print(f"{hour:02}:{minute:02}:{second:02}")
            time.sleep(1)
            if second == 0 and minute == 0 and hour == 0:
                break
        ask = input("Do you want to use timer again ? Press Y for yes or any others for exit").upper()
        if ask == "Y":
            continue
        else:
            print("Thank you ")
            break


