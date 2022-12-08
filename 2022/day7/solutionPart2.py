from __future__ import annotations

DIR_PREFIX = 'dir'
COMMAND_SYMBOL = '$'
PREVIOUS_DIRECTORY_SYMBOL = '..'
ROOT_DIR = '/'
DISK_SIZE = 70000000
NEEDED_SPACE = 30000000

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
        for c in self.children:
            self.size += c.calculate_size()
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
    space_available = DISK_SIZE - root_item.size
    space_to_get = NEEDED_SPACE - space_available

    current_size_dir_to_delete = root_item.size
    for item in file_system.values():
        if item.is_dir and item.size >= space_to_get and item.size < current_size_dir_to_delete:
            current_size_dir_to_delete = item.size
    print(f"The dir size is: {current_size_dir_to_delete}")