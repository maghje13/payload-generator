import os
import sys


program_list = ["msf-payload-generator", "nmap-helper", "arp-discover", "RED_HAWK", "sqlmap", "setoolkit", "socialphish"
                "subfinder", "wireshark", "brutal", "venom", "slowloris", "xsscon"]


def clear():
    os.system("clear")


def install(program):
    if program == "msf-payload-generator":
        os.system("cd programs/msf-payload-generator && bash install.sh")
    elif program == "nmap-helper":
        os.system("cd programs/nmap-helper && bash install.sh")
    elif program == "RED_HAWK":
        os.system("sudo apt install php")
        os.system("cd programs && git clone git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
    elif program == "sqlmap":
        os.system("sudo apt install sqlmap")
    elif program == "setoolkit":
        setoolkit_option = str(input("Install via apt or github (a/g/e, e=exit): "))
        if setoolkit_option == "a" or setoolkit_option == "A":
            os.system("sudo apt install set")
        elif setoolkit_option == "g" or setoolkit_option == "G":
            os.system("cd programs && git clone https://github.com/trustedsec/social-engineer-toolkit/")
            os.system("cd programs && mv social-engineer-toolkit setoolkit")
            os.system("cd programs/setoolkit && sudo python3 setup.py")
    elif program == "socialphish":
        os.system("cd programs && git clone https://github.com/rizzy01/SocialPhish.git")
    elif program == "subfinder":
        os.system("sudo apt install subfinder")
    elif program == "wireshark":
        os.system("sudo apt install wireshark")
    elif program == "brutal":
        os.system("cd programs && sudo git clone https://github.com/Screetsec/Brutal.git")
        os.system("cd programs/Brutal && sudo chmod +x Brutal.sh")
    elif program == "venom":
        os.system("cd programs && git clone https://github.com/r00t-3xp10it/venom.git")
        os.system("cd programs/venom/aux && sudo ./setup.sh && cd .. && bash venom.sh -u")
    elif program == "slowloris":
        os.system("sudo pip install slowloris")
    elif program == "xsscon":
        os.system("pip install bs4 requests")
        os.system("cd programs && git clone https://github.com/menkrep1337/XSSCon && chmod 755 -R XSSCon")


def run(program):
    if program == "msf-payload-generator":
        os.system("cd programs/msf-payload-generator && python3 main.py")
    elif program == "nmap-helper":
        os.system("cd programs/nmap-helper && python3 main.py")
    elif program == "arp-discover":
        os.system("arp -a")
    elif program == "RED_HAWK":
        os.system("cd programs/red_hawk && php rhawk.php")
    elif program == "sqlmap":
        sqlmap_option = str(input("Site to scan (with http/https): "))
        os.system(f"sudo sqlmap -u {sqlmap_option}")
    elif program == "setoolkit":
        os.system("cd programs/setoolkit && sudo setoolkit")
    elif program == "socialphish":
        os.system("cd programs/socialphish && sudo bash socialphish.sh")
    elif program == "subfinder":
        sublist3r_option = str(input("Site to scan (e.g. example.com):"))
        os.system(f"sudo subfinder -d {sublist3r_option}")
    elif program == "brutal":
        os.system("cd programs/Brutal && sudo bash Brutal.sh")
    elif program == "venom":
        os.system("cd programs/venom && sudo bash venom.sh")
    elif program == "slowloris":
        slowloris_option = str(input("Site to DDoS (e.g. example.com): "))
        slowloris_option2 = str(input("Is the site using https? (y/n): "))
        if slowloris_option2 == "Y" or slowloris_option2 == "Y":
            os.system(f"slowloris {slowloris_option} --https")
        else:
            os.system(f"slowloris {slowloris_option}")
    elif program == "xsscon":
        xsscon_option = str(input("Domain: "))
        os.system(f"cd programs/XSSCon && python3 xsscon.py -u {xsscon_option}")


# main program
while True:
    clear()
    for line in open("ascii-art.txt", "r"):
        print(line)
    menu_choice_0 = str(input("""Choose one of these options:
    [1] msf payload generator
    [2] nmap helper
    [3] arp discover tool
    [4] red hawk
    [5] sqlmap
    [6] setoolkit
    [7] socialphish
    [8] subfinder
    [9] wireshark
    [10] Brutal
    [11] venom
    [12] slowloris
    [13] xsscon
    [14] Exit
    
    > """))
    if menu_choice_0 == "":
        pass
    elif manu_choice_0 == "14":
        sys.exit()
    elif menu_choice_0 == "1":
        while True:
            clear()
            print("msf payload generator is a program created by me (maghje13)!\nit uses metasploit-framework's "
                  "msfvenom command to create a backdoor payload, and can create a listener\n "
                  "source: https://github.com/maghje13/payload-generator\n")
            menu_choice_1 = str(input("""Options:
[1] Install
[2] Run
[3] Exit

> """))
            if menu_choice_1 == "1":
                install("msf-payload-generator")
            elif menu_choice_1 == "2":
                run("msf-payload-generator")
            elif menu_choice_1 == "3":
                break
            else:
                pass
    elif menu_choice_0 == "3":
        while True:
            clear()
            print("arp discover tool is a tool created by me (maghje13)!\n"
                  "it uses the \"arp -a\" command to show all devices it can find on your network\n")
            menu_choice_3 = str(input("""Options:
[1] Run
[2] Exit"""))
            if menu_choice_3 == "1":
                run("arp-discover")
            elif menu_choice_3 == "2":
                break
            else:
                pass
    elif menu_choice_0 == "4":
        while True:
            clear()
            print("Redhawk is a very good recon tool for scanning websites and finding vulnerabilities")
            menu_choice_4 = str(input("""Options:
        [1] Install
        [2] Run
        [3] Exit"""))
            if manu_choice == "1":
                install("RED_HAWK")
            elif menu_choice_4 == "2":
                run("RED_HAWK")
            elif menu_choice_4 == "3":
                break
            else:
                pass
