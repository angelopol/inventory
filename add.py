import flet as ft
from variables import GetVariables

variables = GetVariables()

class AddModal:
    def __init__(self, page):
        self.page = page
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Add item to inventory."),
            actions=[
                ft.ElevatedButton(
                    content=ft.Text("Add", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
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
                height=variables['height']
            ),
            ft.TextField(
                label="Ubication.",
                filled=True,
                border_radius=variables['radius'],
                border_width=variables['border_width'],
                height=variables['height']
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