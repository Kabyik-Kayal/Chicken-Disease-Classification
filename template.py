import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Chicken_disease_classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "params.yaml",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    
    path = Path(filepath)
    filedir, filename = os.path.split(path)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created file: {path}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"{filepath} already exists")

    