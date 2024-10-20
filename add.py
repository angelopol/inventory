import flet as ft
from variables import GetVariables
from ItemForm import alert, ItemForm, ValidateInputs
from db import StoreItem

variables = GetVariables()
    
class AddModal:
    def __init__(self, page, inventory):
        self.page = page
        self.inventory = inventory

    def AddItem(self):
        photo = ""
        if self.photo.result != None:
            photo = self.photo.result.files[0].path
        validate = ValidateInputs(self.name.value, self.ubication.value, self.page, self.code.value, self.supplier.value, photo)
        if validate: return validate
        
        StoreItem(self.name.value, self.ubication.value, self.code.value, self.supplier.value, photo)
        self.inventory.update()
        alert(self.page, "Item added.")

    def content(self):
        content, self.name, self.ubication, self.code, self.supplier, self.photo = ItemForm(page=self.page)
        return content

    def open(self):
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Add item to inventory."),
            actions=[
                ft.ElevatedButton(
                    content=ft.Text("Add", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
                    on_click=lambda _: self.AddItem()
                ),
                ft.ElevatedButton(
                    content=ft.Text("Close", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
                    on_click=lambda _: self.close()
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            content=self.content()
        )
        self.page.dialog = self.modal
        self.modal.open = True
        self.page.update()
    
    def close(self):
        self.modal.open = False
        self.modal = None
        self.page.update()

def add(function):
    return ft.Container(
        ft.ElevatedButton(
            content=ft.Text(
                "Add",
                style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD,
                    size=30,
                    color=ft.colors.GREEN
                )
            ),
            on_click=function,
            height=variables['height']
        ),
    col= 3
    )