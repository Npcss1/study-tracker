import json
from datetime import date

def load_log():
    try:
        with open("log.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_log(data):
    with open("log.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_entry(minutes, note):
    log = load_log()
    today = str(date.today())
    if today in log:
        log[today]["minutes"] = log[today]["minutes"] + minutes
        log[today]["note"] = log[today]["note"] + "; " + note
    else:
        log[today] = {"minutes": minutes, "note": note}
    save_log(log)

def total_minutes():
    log = load_log()
    total = 0
    for m in log.values():
        total = total + m["minutes"]
    return total

def add_minutes():
    answer = input("Сколько минут? ")
    try:
        minutes = int(answer)
    except ValueError:
        print("Нужно ввести число")
        return
    note = input("Что было? ")
    add_entry(minutes, note)
    print(total_minutes())

def show_log():
    log = load_log()
    for day, data in log.items():
        print(day, data["minutes"], "мин,", data["note"])

def menu():
    while True:
        answer = input("1: История |  2: Добавить запись |  3: Exit: ")
        if  answer == "1":
            show_log()
        elif  answer == "2": 
            add_minutes()
        elif answer == "3":
            break
        else:
            print("нет такого")
menu()