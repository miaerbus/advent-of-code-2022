file1 = open('day7/input', 'r')
lines = file1.readlines()


def disk_space():
    root = build_file_system(lines)
    dirs = find_all_directories(root)
    sum = 0
    can_be_deleted = root.size() - 40_000_000
    suitable = []
    for dir in dirs:
        size = dir.size()
        if size < 100_000:
            sum += size
        if size > can_be_deleted:
            suitable.append(size)

    print("Disk space, part 1:", sum)
    print("Disk space, part 2:", min(suitable))


def build_file_system(rows):
    root = ElfDirectory("/", None)
    current_dir = root
    for line in rows:
        if ElfFile.is_file(line):
            process_file_line(line, current_dir)
        elif ElfDirectory.is_directory(line):
            process_directory_line(line, current_dir)
        elif is_command(line):
            current_dir = process_change_directory(line, current_dir)
    return root


def find_all_directories(to_search):
    all_dirs = [to_search]
    for child in to_search.directories:
        all_dirs.extend(find_all_directories(child))
    return all_dirs


def process_file_line(line, current_directory):
    file = ElfFile.parse(line)
    current_directory.add_file(file)


def process_directory_line(line, current_directory):
    ElfDirectory.parse(line, current_directory)


def is_command(string):
    return string.startswith('$ cd')


def process_change_directory(line, current_directory):
    command_data = line.split()
    name = command_data[2]
    if name == '..':
        if current_directory.parent is not None:
            return current_directory.parent
    elif name == '/':
        return current_directory
    else:
        child_directories = current_directory.directories
        for directory in child_directories:
            if directory.name == name:
                return directory


class ElfFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @staticmethod
    def parse(line):
        file_data = line.split()
        return ElfFile(file_data[1], int(file_data[0]))

    @staticmethod
    def is_file(line):
        array = line.split()
        size = array[0]
        return len(array) == 2 and size.isnumeric()


class ElfDirectory:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = []
        if parent is not None:
            self.parent.directories.append(self)

    @staticmethod
    def parse(line, parent):
        file_data = line.split()
        directory = ElfDirectory(file_data[1], parent)
        return directory

    @staticmethod
    def is_directory(string):
        return string.startswith('dir ')

    def add_file(self, file):
        self.files.append(file)

    def size(self):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.directories:
            size += directory.size()
        return size


disk_space()
