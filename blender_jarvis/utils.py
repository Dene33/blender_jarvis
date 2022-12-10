import os
import subprocess
from typing import List
import sys

def get_python_path():
    python_dir = os.path.join(sys.prefix, 'bin')
    python_files = [i for i in os.listdir(python_dir) if i.startswith("python")]
    
    python_exe = os.path.join(sys.prefix, 'bin', python_files[0])

    return python_exe

def pip_install(packages_names: List[str]):
    python_exe = get_python_path()
    subprocess.run([python_exe, "-m", "ensurepip"])
    subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

    for package_name in packages_names:        
        # install required packages
        subprocess.run([python_exe, "-m", "pip", "install", package_name, '--upgrade'])