from __future__ import annotations

total_until_100000 = 0

DIR_PREFIX = 'dir'
COMMAND_SYMBOL = '$'
PREVIOUS_DIRECTORY_SYMBOL = '..'
ROOT_DIR = '/'
MAX_DIR_SIZE = 100000

file_system = {}

class FileSystemItem:
    def __init__(self, prefix: str, name: str):
        self.is_dir = prefix == DIR_PREFIX
        self.name = name
        self.size = 0 if self.is_dir else int(prefix)
        self.children: list[FileSystemItem] = []

    def add_child(self, childItem: FileSystemItem):
        self.children.append(childItem)

    def calculate_size(self) -> int:
        if not self.is_dir:
            return self.size
        global total_until_100000
        for c in self.children:
            self.size += c.calculate_size()
        if self.size <= MAX_DIR_SIZE:
            total_until_100000 += self.size
        return self.size

def get_item_key(path_list: list[str], filename = None) -> str:
    if len(current_path) == 1 and filename is None:
        return ROOT_DIR
    path = ROOT_DIR
    for p in path_list[1:]:
      path += f'{p}/'
    if filename is not None:
        return f'{path}{filename}'
    return path[:-1]


with open("input.txt", "r") as input_file:
    commands_record = input_file.readlines()
    root_item = FileSystemItem(DIR_PREFIX, ROOT_DIR)
    file_system[ROOT_DIR] = root_item
    current_path = [ROOT_DIR]
    for output_record in commands_record[2:]:
        if output_record[0] == COMMAND_SYMBOL:
            command = output_record[2:].split(' ')
            # cd command
            if len(command) == 2:
                destination = command[1].rstrip()
                if destination == PREVIOUS_DIRECTORY_SYMBOL:
                    del current_path[-1]
                else:
                    current_path.append(destination)
        else:
            ls_output_item = output_record.split(' ')
            item_name = ls_output_item[1].rstrip()
            file_item = FileSystemItem(ls_output_item[0], item_name)
            file_system[get_item_key(current_path, item_name)] = file_item
            file_system[get_item_key(current_path)].add_child(file_item)
    root_item.calculate_size()
        
print(f"The total size is: {total_until_100000}")
