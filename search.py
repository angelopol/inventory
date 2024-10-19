import flet as ft
from variables import GetVariables
from db import GetItems, GetItemsByName, GetItemsByUbication

variables = GetVariables()

SearchDropwdown = ft.Dropdown(
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

def search(input, inventory):
    if input.control.value == "":
        inventory.update()
    else:
        if SearchDropwdown.value == "Name":
            inventory.update(lambda: GetItemsByName(input.control.value))
        else:
            inventory.update(lambda: GetItemsByUbication(input.control.value))

def dropdown():
    return SearchDropwdown

def text(inventory):
    return ft.TextField(
        filled=True,
        border_radius=variables['radius'],
        border_width=variables['border_width'],
        col=6,
        height=variables['height'],
        hint_text="Search",
        on_change=lambda _: search(_, inventory)
    )