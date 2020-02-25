sec_input = int(input("Введите количество секунд:"))
hours = sec_input // 3600
minutes = sec_input // 60 - hours * 60
sec = sec_input % 60
if sec <= 9:
    sec = str(f"0{sec}")
if minutes <= 9:
    minutes = str(f"0{minutes}")
if hours <= 9:
    hours = str(f"0{hours}")
print(f"{hours}:{minutes}:{sec}")
