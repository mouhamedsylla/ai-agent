import os
from functions.config import MAX_CHARS

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


def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    target_file_path = os.path.join(abs_working_directory, file_path)

    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    if not os.path.abspath(target_file_path).startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if os.path.getsize(target_file_path) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

            return file_content_string
    except PermissionError:
        print("Error: no permission for reading file")
    
    except Exception as e:
        print(f"Error: {e}")
    


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    target_file_path = os.path.join(abs_working_directory, file_path)

    if not os.path.abspath(target_file_path).startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(target_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        print("Error: can't write file")
