import pyperclip, pyautogui, random
from time import sleep


def get_ready():
    print("Ready ...")
    print("Move your cursor to the textbox.")

    for i in range(5,-1,-1):
        print(i)
        sleep(1)

# Spam with count
def spam_count():
    start = int(input("Start from: "))
    end = int(input("To: "))
    time = float(input("Enter spam speed (sec): "))
    get_ready()
    if start < end:
        start = start-1
        limit = end - start
        for i in range(limit):
            pyperclip.copy(i+2)
            pyautogui.hotkey("ctrl","v")
            pyautogui.press("enter")
            sleep(time)
    
    elif start > end:
        end = end-1
        limit = start - end
        for i in range(limit):
            pyperclip.copy(start-i)
            pyautogui.hotkey("ctrl","v")
            pyautogui.press("enter")
            sleep(time)

# Spam on random
def spam_random():
    msg = input("Enter spam message (Multiple messages separate by '/'): ")
    limit = int(input("Enter spam limit: "))
    time = float(input("Enter spam speed (sec): "))
    get_ready()
    for i in range(limit):
        pyperclip.copy(random.choice(msg.split("/")).strip())
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        sleep(time)

# Spam in ordered
def spam_ordered():
    msg = input("Enter spam message (Multiple messages separate by '/'): ")
    limit = int(input("Enter spam limit: "))
    time = float(input("Enter spam speed (sec): "))
    get_ready()
    for i in range(limit):
        for i in msg.split("/"):
            pyperclip.copy(i.strip())
            pyautogui.hotkey("ctrl","v")
            pyautogui.press("enter")
            sleep(time)

# Spam from clipboard
def spam_clipboard():
    limit = int(input("Enter spam limit: "))
    time = float(input("Enter spam speed (sec): "))
    get_ready()
    for i in range(limit):
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        sleep(time)

# Click spam
def spam_click():
    limit = int(input("Enter click limit: "))
    time = float(input("Enter click speed (sec): "))
    get_ready()
    for i in range(limit):
        pyautogui.click()
        sleep(time)

print("\nChoose spam mode:")
print("1. Spam on count")
print("2. Spam message (random)")
print("3. Spam message (ordered)")
print("4. Spam clipboard")
print("5. Spam click\n")

option = int(input("Choice: "))

if option == 1: spam_count()
elif option == 2: spam_random()
elif option == 3: spam_ordered()
elif option == 4: spam_clipboard()
elif option == 4: spam_clipboard()
elif option == 5: spam_click()

