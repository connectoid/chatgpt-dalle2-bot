import json

def compare_and_update_dict(new_dict, file_path="events_dict.json"):
    try:
        with open(file_path, "r") as file:
            saved_dict = json.load(file)
        
        if new_dict != saved_dict:
            with open(file_path, "w") as file:
                json.dump(new_dict, file, indent=4)
            return True
    
    except FileNotFoundError:
        with open(file_path, "w") as file:
            json.dump(new_dict, file, indent=4)
        return True
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False
    
    return False




def create_message_text(events):
    lst = []
    try:
        for event in events:
            event_string = '\n'.join(str(value) for value in event.values())
            lst.append(event_string)
        message_text = '\n\n'.join(lst)
        return message_text
    except Exception as e:
        print(f'Exception in create_message_text: {e}')
        return False


def add_userid_to_file(number, file_path='userid_list.txt'):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        
        if number not in numbers:
            numbers.append(number)
            
            numbers.sort()
            
            with open(file_path, 'w') as file:
                for num in numbers:
                    file.write(f"{num}\n")
            print(f"UserID {number} добавлено в файл.")
        else:
            print(f"UserID {number} уже присутствует в файле.")
    
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            file.write(f"{number}\n")
        print(f"Файл {file_path} не найден. Создан новый файл с UserID {number}.")


def read_ids_from_file(file_path='userid_list.txt'):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers.append(int(line.strip()))
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    return numbers
