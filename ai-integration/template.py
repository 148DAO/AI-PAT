"""Python Script to Create Folder Structure"""
# Update the structure as per your need

import os
from pathlib import Path



"""Add or Modify the file/folder list below to create new files/folders in the same directory"""
files = [
    f"Makefile", # A text file that contain instruction to build software
    f"README.md", # Readme file for Ai part
    
    # Requirements (dependencies)
    f"requirements.txt", 
    f"setup.py",

    # Docker 
    f"Dockerfile",
    f".dockerignore",
    
    # More
    f"app.py", 

    # Data
    f"data/external/.gitkeep",
    f"data/interim/.gitkeep",
    f"data/processed/.gitkeep",
    f"data/raw/.gitkeep",

    # Data 
    f"docs/.gitkeep", # sphinx project 

    # Jupyter notebooks
    f"notebooks/.gitkeep", 

    # Resources and Reports
    f"references/ref.txt",
    f"reports/figures/.gitkeep",
    f"reports/logs/.gitkeep",
    f"reports/papers/.gitkeep",

    # Source files
    f"src/__init__.py",
    # Data
    f"src/data/__init__.py",
    f"src/data/make_dataset.py",
    # Features
    f"src/features/__init__.py",
    f"src/features/build_features.py",
    
    # Models
    f"models/model.py",
    f"src/models/__init__.py",
    f"src/models/predict_model.py",
    f"src/models/train_model.py",
    f"model-weights/.gitkeep", 

    # Visualize
    f"src/visualization/__init__.py",
    f"src/visualization/visualize.py",

    # Evaluation 
    f"src/evaluation/__init__.py", 
    f"src/evaluation/evaluate.py",

    # Data Pipeline (if req)
    f"src/pipeline/__init__.py",
    f"src/pipeline/data_pipeline.py",

    # Misc 
    f"api/.gitkeep",
    f"tests/.gitkeep",
    f"training/.gitkeep",
    f"fine-tune/.gitkeep",
    f"tasks/.gitkeep"     
]


# Function to create the files
def create_files(file_list):
    """
    Creates a list of files if they don't exist.
    
    Args:
        file_list: A list of strings representing file paths.
    """

    try:
        for f in file_list: 
            filepath = Path(f)
            file_dir, filename = os.path.split(filepath)

            if file_dir != "":
                os.makedirs(f"{file_dir}", exist_ok=True)
            if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
                with open(filepath, "w") as f:
                    pass 
            else:
                print(f"File is already present at: {filepath}")
    except:
        print("[ERROR] Failed to create files")



# Function to create the folder structure 
def create_folders(items):
    """
    Creates a folder structure based on a list of files and folders.

    Args:
        items: A list of strings representing files or folders. Files should have extensions, while folders should be simple names.
    """
    
    try:
        for item in items:
            if "." in item:  # It's a file
                file_path = Path(item)
                file_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories
            else:  # It's a folder
                folder_path = Path(item)
                folder_path.mkdir(parents=True, exist_ok=True)
    except: 
        print("[ERROR] Failed to create folders")




# Main
if __name__=="__main__":
    create_files(files)
    # create_folders(folders)
    print("[INFO] Folder structure created")
