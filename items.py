import flet as ft
from variables import GetVariables

variables = GetVariables()

class ItemModal:
    def __init__(self, page, item):
        self.page = page
        self.item = item
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Item "+item[0]+"."),
            actions=[
                ft.ElevatedButton(
                    content=ft.Text("Update", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color=ft.colors.BLUE)),
                    on_click=None
                ),
                ft.ElevatedButton(
                    content=ft.Text("Delete", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color=ft.colors.RED)),
                    on_click=None
                ),
                ft.ElevatedButton(
                    content=ft.Text("Close", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
                    on_click=lambda _: self.close()
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )

    def content(self):
        return ft.Column(
            [ft.TextField(
                label="Name.",
                filled=True,
                border_radius=variables['radius'],
                border_width=variables['border_width'],
                height=variables['height'],
                value=self.item[1]
            ),
            ft.TextField(
                label="Ubication.",
                filled=True,
                border_radius=variables['radius'],
                border_width=variables['border_width'],
                height=variables['height'],
                value=self.item[2]
            )],
            alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS
        )

    def open(self):
        self.modal.content = self.content()
        self.page.dialog = self.modal
        self.modal.open = True
        self.page.update()
    
    def close(self):
        self.modal.open = False
        self.page.update()

class items:
    def __init__(self, page):
        self.page = page
        self.content = self.MakeContent()
        self.page.add(self.content)

    def MakeContent(self):
        elements = []
        InventoryItems = [['1', "Item 1", "Ubication 1"], ['2', "Item 2", "Ubication 2"], ['3', "Item 3", "Ubication 3"]]
        if len(InventoryItems) == 0:
            return ft.Text("Aún no ha agregado ningún item al inventario.", style=ft.TextStyle(size=20))
        for item in InventoryItems:
            modal = ItemModal(self.page, item)
            elements.append(ft.ResponsiveRow([
                    ft.TextButton(
                        content=ft.Text(item[0]+': '+item[1]+', '+item[2], style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20)),
                        on_click=lambda _: modal.open(), expand=True, height=variables['height'], col=12
                    )
                ])
            )
        return ft.Column(elements, alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS)
    
    def update(self):
        self.content = self.MakeContent()
        self.page.update()