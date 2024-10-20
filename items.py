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
        photo = self.item[5]
        if self.photo.result != None:
            photo = self.photo.result.files[0].path
        validate = ValidateInputs(self.name.value, self.ubication.value, self.page, self.code.value, self.supplier.value, photo)
        if validate: return validate

        UpdateItem(self.item[0], self.name.value, self.ubication.value, self.code.value, self.supplier.value, photo)
        self.inventory.update()
        alert(self.page, "Item updated.")

    def delete(self):
        DeleteItem(self.item[0])
        self.inventory.update()
        alert(self.page, "Item deleted.")

    def content(self):
        content, self.name, self.ubication, self.code, self.supplier, self.photo = ItemForm(self.item[1], self.item[2], self.item[3], self.item[4], self.page, self.item[5])
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

    def MakeContent(self, function):
        elements = []
        InventoryItems = function()
        if len(InventoryItems) == 0:
            self.content.content = ft.Text("Items not found.", style=ft.TextStyle(size=20))
            return

        for item in InventoryItems:
            modal = ItemModal(self.page, item, self)
            RowContent = [
                ft.Container(
                    ft.Image(src=item[5], height=(variables['height']*2)-20, border_radius=ft.border_radius.all(30), fit=ft.ImageFit.FIT_HEIGHT),
                    padding=ft.Padding(20, 10, 20, 10)
                ),
                ft.Text(item[3] + ': ' + item[1] + ', ' + item[2] + ', ' + item[4], style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20))
            ]
            height = variables['height']*2
            if item[5] == "":
                RowContent.pop(0)
                height = variables['height']
            elements.append(ft.ResponsiveRow([
                ft.TextButton(
                    content=ft.Row(RowContent),
                    on_click=lambda _, modal=modal: modal.open(), expand=True, height=height, col=12
                )
            ]))

        self.content.content = ft.Column(elements, alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS)

    def update(self, function=GetItems):
        self.MakeContent(function)
        self.page.update()