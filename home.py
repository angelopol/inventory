import flet as ft

radius = 40
height = 60
border_width = 0

class AddModal:
    def __init__(self, page):
        self.page = page
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Add item to inventory."),
            actions=[
                ft.ResponsiveRow([
                    ft.ElevatedButton(
                        content=ft.Text("Add", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
                        on_click=None, col=6
                    ),
                    ft.ElevatedButton(
                        content=ft.Text("Close", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
                        on_click=lambda _: self.close(), col=6
                    )
                ])
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )

    def content(self):
        return ft.Column(
            [ft.TextField(
                label="Name.",
                filled=True,
                border_radius=radius,
                border_width=border_width,
                height=height
            ),
            ft.TextField(
                label="Ubication.",
                filled=True,
                border_radius=radius,
                border_width=border_width,
                height=height
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

def dropdown():
    return ft.Dropdown(
        label_style=ft.TextStyle(size=10),
        options=[
            ft.dropdown.Option("Name"),
            ft.dropdown.Option("Ubication")
        ],
        filled=True,
        border_radius=radius,
        border_width=border_width,
        col=3,
        height=height
    )

def text():
    return ft.TextField(
        filled=True,
        border_radius=radius,
        border_width=border_width,
        col=6,
        height=height
    )

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
            height=height
        ),
    col= 3
    )

def main(page: ft.Page):
    page.title = "Inventory"
    page.theme = ft.Theme(font_family="Nunito")

    modal = AddModal(page)

    page.add(ft.ResponsiveRow([dropdown(), text(), add(lambda _: modal.open())]))

ft.app(main)