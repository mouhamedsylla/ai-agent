import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    target_path = os.path.join(abs_working_directory, directory)

    result = f'Result for {directory} directory'

    if directory == '.' :
        result = "Result for current directory:"

    if not os.path.isdir(target_path):
        return f'    Error: "{directory}" is not a directory'

    if not os.path.abspath(target_path).startswith(abs_working_directory):
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'

    
    
    files = os.listdir(target_path)


    return result + '\n' + formatting_output(listdir=files, target_path=target_path)


def formatting_output(listdir, target_path):
    lines = []
    for file in listdir:
        full_path = os.path.join(target_path, file)
        lines.append(f' - {file}: file_size={os.path.getsize(full_path)} is_dir={os.path.isdir(full_path)}')

    return "\n".join(lines)