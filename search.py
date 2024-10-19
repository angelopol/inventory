import flet as ft
from variables import GetVariables

variables = GetVariables()

def dropdown():
    return ft.Dropdown(
        label_style=ft.TextStyle(size=10),
        options=[
            ft.dropdown.Option("Name"),
            ft.dropdown.Option("Ubication")
        ],
        filled=True,
        border_radius=variables['radius'],
        border_width=variables['border_width'],
        col=3,
        height=variables['height'],
        value="Name"
    )

def text():
    return ft.TextField(
        filled=True,
        border_radius=variables['radius'],
        border_width=variables['border_width'],
        col=6,
        height=variables['height'],
        hint_text="Search"
    )