import ctypes
import os
import sys

# Request elevated permission
ctypes.windll.shell32.IsUserAnAdmin() or (
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    ) > 32, exit())

if os.path.isfile("./cmd.exe"):
    os.system("echo ✔️ cmd.exe exists")
else:
    os.system("echo ✖️ cmd.exe does not exist")
    print()

    os.system("pause")
    sys.exit()

if os.path.isfile("./register.reg"):
    os.system("echo ✔️ register.reg exists")
else:
    os.system("echo ✖️ register.reg does not exist")
    print()

    os.system("pause")
    sys.exit()

print()

# Add registry values
os.system("echo ➕ Adding required values to registry...")
os.system("regedit.exe /S register.reg >nul")
os.system("echo ✔️ Added required values to the registry.")

print()

# Create C:\Protocols directory
if os.path.isdir("C:\Protocols"):
    os.system("echo ✔️ \"C:\Protocols\" exists")
else:
    os.system("echo ✖️ \"C:\Protocols\" does not exist")
    print()

    os.system("echo ➕ Creating directory \"C:\Protocols\"...")
    os.mkdir("C:\Protocols")
    os.system("echo ✔️ Created directory \"C:\Protocols\".")

print()

# Copy cmd.exe
os.system("echo ➕ Copying \"cmd.exe\" to \"C:\Protocols\cmd.exe\"...")
os.system("xcopy \"cmd.exe\" \"C:\Protocols\" /E /C /H /R /K /O /Y >nul")
os.system("echo ✔️ Copied \"cmd.exe\" to \"C:\Protocols\cmd.exe\".")

print()

os.system("echo ✔️ The \"cmd://\" protocol has been registered.")

print()

os.system("pause")
sys.exit()
