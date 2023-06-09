import ctypes
import os
import sys

# Request elevated permission
ctypes.windll.shell32.IsUserAnAdmin() or (
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    ) > 32, exit())

if os.path.isfile("./cmd.exe"):
    print("✔️ cmd.exe exists")
else:
    print("✖️ cmd.exe does not exist\n")

    os.system("pause")
    sys.exit()

if os.path.isfile("./register.reg"):
    print("✔️ register.reg exists\n")
else:
    print("✖️ register.reg does not exist\n")

    os.system("pause")
    sys.exit()

# Add registry values
print("➕ Adding required values to registry...")
os.system("regedit.exe /S register.reg >nul")
print("✔️ Added required values to the registry\n")

# Create C:\Protocols directory
if os.path.isdir("C:\Protocols"):
    print("✔️ \"C:\Protocols\" exists\n")
else:
    print("✖️ \"C:\Protocols\" does not exist")

    print("➕ Creating directory \"C:\Protocols\"...")
    os.mkdir("C:\Protocols")
    print("✔️ Created directory \"C:\Protocols\"\n")

# Copy cmd.exe
print("➕ Copying \"cmd.exe\" to \"C:\Protocols\cmd.exe\"...")
os.system("xcopy \"cmd.exe\" \"C:\Protocols\" /E /C /H /R /K /O /Y >nul")
print("✔️ Copied \"cmd.exe\" to \"C:\Protocols\cmd.exe\"\n")

print("✔️ The \"cmd://\" protocol has been registered.\n")

os.system("pause")
sys.exit()
