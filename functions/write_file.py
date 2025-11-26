import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        dir_name = os.path.dirname(abs_file_path)
        os.makedirs(dir_name, exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to the file path provided. Overwritting the file if it already exists. Files can only be written in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The STDout and STDErr of resulting from the script running will be returned. If the script exits with a non-zero value that will be appended to the output",),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file specified by file_path",
            ),
        },
    ),
)