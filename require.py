import os

packages = [
    "flet",
]

for package in packages:
    os.system(f"pip install {package}")