import flet as ft
from items import items
from add import AddModal, add
from search import dropdown, text

def main(page: ft.Page):
    page.title = "Inventory"
    page.theme = ft.Theme(font_family="Nunito")

    inventory = items(page)
    modal = AddModal(page, inventory)
    page.add(ft.ResponsiveRow([dropdown(), text(), add(lambda _: modal.open()), inventory.content]))

ft.app(main)