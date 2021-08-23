import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print("|=================================================================|")
print("| {:<63} |".format('             Windows WiFi Password Gethering Tool'))
print("|=================================================================|")
print("| {:<30} | {:<30} |".format('Design by', "Team Alchemists"))
print("|=================================================================|")
print("| {:<30} | {:<30} |".format('SSID', 'Password'))
print("|=================================================================|")
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("| {:<30} | {:<30} |".format(i, results[0]))
    except IndexError:
        print ("| {:<30} | {:<30} |".format(i, ""))
print("|=================================================================|")
input("\nEnter to Exit")

