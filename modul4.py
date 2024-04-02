# Завдання 1
def total_salary(path):
    try:
        with open (path, 'r' , encoding="utf-8") as file:
            totaly_salary = 0
            num_developers = 0
            for lines in file:
                name, salary = lines.strip().split(",")
                totaly_salary += int(salary)
                num_developers += 1
            average_salary = totaly_salary/num_developers
            return totaly_salary, average_salary
    except FileNotFoundError:
          print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}") 

total, average = total_salary("/Applications/homework4/develop.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Завдання 2
def get_cats_info(path):
    cats_info = []
    try:
        with open (path, "r",encoding="utf-8") as file:
            for lines in file:
                cat_id, name, age = lines.strip().split(",")
                cat_info = {"id": cat_id, "Name": name, "age": age}
                cats_info.append(cat_info)
            return cats_info
    except FileNotFoundError:
          print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}") 
   
cats_info = get_cats_info("/Applications/homework4/cats.txt")
print(cats_info)


