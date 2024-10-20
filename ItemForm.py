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

def ValidateInputs(name, ubication, page, code, supplier, photo):
    if name == "" or ubication == "" or code == "" or supplier == "":
        return alert(page, "Please fill all fields.")

def ItemForm(NameValue="", UbicationValue="", CodeValue="", SupplierValue="", page=None, PhotoValue=""):
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
    def PickPhoto(page, PhotoName, picker):
        if picker.files != None:
            PhotoName.src = picker.files[0].path
            page.update()

    PhotoName = ft.Image(
        src="x",
        height=variables['height'],
        fit=ft.ImageFit.FIT_HEIGHT,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10),
        col=3
    )
    photo = ft.FilePicker(on_result=lambda _: PickPhoto(page, PhotoName, _))
    page.overlay.append(photo)
    
    PhotoButton = ft.ResponsiveRow([
        ft.ElevatedButton(on_click=lambda _: photo.pick_files(), height=variables['height'],
            content=ft.Text("Choose photo.", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=16)), col=9
        ), PhotoName
    ], expand=True)

    elements = [code, name, ubication, supplier, PhotoButton]
    if PhotoValue != "":
        ItemPhoto = ft.Image(
            src=PhotoValue,
            width=350,
            fit=ft.ImageFit.FIT_WIDTH,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(30)
        )
        elements.append(ItemPhoto)
    return ft.Column(elements, alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS), name, ubication, code, supplier, photo