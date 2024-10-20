import flet as ft
from variables import GetVariables

variables = GetVariables()

class alert:
    def __init__(self, page, text):
        self.page = page
        self.text = text
        self.open()

    def open(self):
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(self.text),
            actions=[
                ft.ElevatedButton(
                    content=ft.Text("Close", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
                    on_click=lambda _: self.close()
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )

        self.page.dialog = self.modal
        self.modal.open = True
        self.page.update()
    
    def close(self):
        self.modal.open = False
        self.modal = None
        self.page.update()

def ValidateInputs(name, ubication, page, code, supplier):
    if name == "" or ubication == "" or code == "" or supplier == "":
        return alert(page, "Please fill all fields.")

def ItemForm(NameValue="", UbicationValue="", CodeValue="", SupplierValue=""):
    code = ft.TextField(
        label="Code.",
        filled=True,
        border_radius=variables['radius'],
        border_width=variables['border_width'],
        height=variables['height'],
        max_length=1000,
        value=CodeValue
    )
    name = ft.TextField(
        label="Name.",
        filled=True,
        border_radius=variables['radius'],
        border_width=variables['border_width'],
        height=variables['height'],
        max_length=1000,
        value=NameValue
    )
    supplier = ft.TextField(
        label="Supplier.",
        filled=True,
        border_radius=variables['radius'],
        border_width=variables['border_width'],
        height=variables['height'],
        max_length=1000,
        value=SupplierValue
    )
    ubication = ft.TextField(
        label="Ubication.",
        filled=True,
        border_radius=variables['radius'],
        border_width=variables['border_width'],
        height=variables['height'],
        max_length=1000,
        value=UbicationValue
    )
    return ft.Column([code, name, supplier, ubication],alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS), name, ubication, code, supplier