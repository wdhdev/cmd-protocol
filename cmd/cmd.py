import os
import sys

URL = sys.argv[1]

if URL.startswith("cmd://") and URL.replace("cmd://", "") == "" or not URL.startswith("cmd://") or URL.startswith("cmd:///"):
    print("No command was specified.\n")
    os.system("pause")
    sys.exit()

commands = URL.split("//")
command_tmp = commands[1]
t22 = command_tmp[len(command_tmp) - 1]

if t22 == "/":
    command_tmp2 = command_tmp[:-1]
else:
    command_tmp2 = command_tmp

command = (
    command_tmp2
    .replace("%20", " ")
    .replace("%5C", "\\")
    .replace("%7C", "|")
    .replace("-/", "-")
    .replace("%25", "%")
)

print("""  ____                                          _   _____                     _
 / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| | | ____|_  _____  ___ _   _| |_ ___  _ __
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` | |  _| \ \/ / _ \/ __| | | | __/ _ \| '__|
| |__| (_) | | | | | | | | | | | (_| | | | | (_| | | |___ >  <  __/ (__| |_| | || (_) | |
 \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_| |_____/_/\_\___|\___|\__,_|\__\___/|_|
""")

print("Command:", command)

while True:
    confirm = input("\nExecute command? [y/N]\n>> ")
    start = confirm.lower()

    if start == "y" or start == "yes":
        print()
        os.system("cmd /c " + command)

        print("\nOperation completed.\n")
        os.system("pause")
        sys.exit()
    else:
        print("\nOperation cancelled.\n")
        os.system("pause")
        sys.exit()
