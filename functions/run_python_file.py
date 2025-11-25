import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not (os.path.exists(fabs_file_pathh) or os.path.isfile(abs_file_path)):
            return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py`"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python", abs_file_path] + args,
            capture_output=True,
            text=True,
            cwd=working_directory,
            check=True,
            timeout=30,
        )
        output = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            output = "No output produced."
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"