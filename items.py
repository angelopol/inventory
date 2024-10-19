import flet as ft
from variables import GetVariables
from db import GetItems, UpdateItem, DeleteItem
from ItemForm import alert, ItemForm, ValidateInputs

variables = GetVariables()

class ItemModal:
    def __init__(self, page, item, inventory):
        self.page = page
        self.item = item
        self.inventory = inventory

    def update(self):
        validate = ValidateInputs(self.name.value, self.ubication.value, self.page)
        if validate: return validate

        UpdateItem(self.item[0], self.name.value, self.ubication.value)
        self.inventory.update()
        alert(self.page, "Item updated.")

    def delete(self):
        DeleteItem(self.item[0])
        self.inventory.update()
        alert(self.page, "Item deleted.")

    def content(self):
        content, self.name, self.ubication = ItemForm(self.item[1], self.item[2])
        return content

    def open(self):
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Item details."),
            actions=[
                ft.ElevatedButton(
                    content=ft.Text("Update", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color=ft.colors.BLUE)),
                    on_click=lambda _: self.update()
                ),
                ft.ElevatedButton(
                    content=ft.Text("Delete", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color=ft.colors.RED)),
                    on_click=lambda _: self.delete()
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

class items:
    def __init__(self, page):
        self.page = page
        self.content = ft.Container()
        self.update()

    def MakeContent(self):
        elements = []
        InventoryItems = GetItems()
        if len(InventoryItems) == 0:
            self.content.content = ft.Text("Items not found.", style=ft.TextStyle(size=20))
            return

        for item in InventoryItems:
            modal = ItemModal(self.page, item, self)
            elements.append(ft.ResponsiveRow([
                ft.TextButton(
                    content=ft.Text(item[1] + ', ' + item[2], style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20)),
                    on_click=lambda _, modal=modal: modal.open(), expand=True, height=variables['height'], col=12
                )
            ]))

        self.content.content = ft.Column(elements, alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS)

    def update(self):
        self.MakeContent()
        self.page.update()