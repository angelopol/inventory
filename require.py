import os

packages = [
    "flet",
    "sqlite3"
]

for package in packages:
    os.system(f"pip install {package}")