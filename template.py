import os


dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

for directory in dirs:
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, ".gitkeep"), "w") as f:
        pass
 
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]

for file in files:
    with open(file, "w") as f:
        pass