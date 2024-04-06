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

# Task 4 
def parse_input(user_input):

  cmd, *args = user_input.split()
  cmd = cmd.strip().lower()
  return cmd, *args


def add_contact(args, contacts):
  name, phone = args
  contacts[name] = phone
  return "Contact added."


def change_contact(args, contacts):
  name, phone = args
  if name not in contacts:
    return f"Contact '{name}' not found."
  contacts[name] = phone
  return "Contact updated."


def show_phone(name, contacts):
  if name not in contacts:
    return f"Contact '{name}' not found."
  return contacts[name]


def show_all(contacts):
  if not contacts:
    return "No contacts found."
  return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
  
  contacts = {}

  print("Welcome to the assistant bot!")
  while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)

    if command in ["close", "exit"]:
      print("Good bye!")
      break

    elif command == "hello":
      print("How can I help you?")

    elif command == "add":
      print(add_contact(args, contacts))

    elif command == "change":
      print(change_contact(args, contacts))

    elif command == "phone":
      print(show_phone(*args, contacts))

    elif command == "all":
      print(show_all(contacts))

    else:
      print("Invalid command.")


if __name__ == "__main__":
  main()