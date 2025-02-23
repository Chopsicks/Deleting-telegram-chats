import pyautogui
import time
import keyboard
from colorama import init, Fore, Style
init()
ascii_art = r"""                    
 _____ _____         _      _      _ _              _____  _____  _____  _____ 
|_   _|  __ \       | |    | |    (_) |            |____ ||  _  ||  _  ||  _  |
  | | | |  \/     __| | ___| | ___ _| |_ ___ _ __      / /| |/' || |/' || |/' |
  | | | | __     / _` |/ _ \ |/ _ \ | __/ _ \ '__|     \ \|  /| ||  /| ||  /| |
  | | | |_\ \   | (_| |  __/ |  __/ | ||  __/ |    .___/ /\ |_/ /\ |_/ /\ |_/ /
  \_/  \____/    \__,_|\___|_|\___|_|\__\___|_|    \____/  \___/  \___/  \___/                                                                              
  By Frizzy Low
"""
colors = [
    Fore.MAGENTA,
    Fore.LIGHTMAGENTA_EX,
]
lines = ascii_art.splitlines()
for i, line in enumerate(lines):
    color = colors[i % len(colors)]
    print(color + line)
print(Style.RESET_ALL)
pyautogui.PAUSE = 0.01
LOOP_COUNT = 50000
def perform_actions():
    for i in range(LOOP_COUNT):
        if keyboard.is_pressed('q'):
            print("Стоп.")
            break
        pyautogui.click(button='right')
        pyautogui.press('up')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('enter')
        pyautogui.press('enter')
        print(f"Удален{i + 1} чат")
def configure_settings():
    global LOOP_COUNT
    try:
        print('Введите значение для скорости (скорость выполнение каждого действия) и количество удаленных чатов.')
        print("По умолчанию Скорость = 00.1 Количество = 50000")
        new_pause = float(input("Скорость: "))
        new_loop_count = int(input("Количество: "))
        pyautogui.PAUSE = new_pause
        LOOP_COUNT = new_loop_count
        print(f"Настройки обновлены: PAUSE = {pyautogui.PAUSE}, LOOP_COUNT = {LOOP_COUNT}")
    except ValueError:
        print("Ошибка.")
def reset_settings():
    global LOOP_COUNT
    pyautogui.PAUSE = 0.01
    LOOP_COUNT = 50000
    print(f"Сброс: PAUSE = {pyautogui.PAUSE}, LOOP_COUNT = {LOOP_COUNT}")
def main_menu():
    while True:
        print("\n--- Меню ---")
        print("1. Запустить выполнение")
        print("2. Настроить параметры")
        print("3. Сбросить настройки по умолчанию")
        print("4. Выйти")
        choice = input("Выберите: ")
        if choice == '1':
            print('Вам нужно навестись на самый в тг первый чат и нажать s, Не шевелить не чем!')
            print("Чтобы начать нажмите s для остановки нажмите q.")
            keyboard.wait('s')
            perform_actions()
            print("Готово.")
        elif choice == '2':
            configure_settings()
        elif choice == '3':
            reset_settings()
        elif choice == '4':
            print("Выход.")
            break
        else:
            print("Ошибка")
if __name__ == "__main__":
    main_menu()
