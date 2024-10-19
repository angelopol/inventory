import flet as ft
from items import items
from add import AddModal, add
from search import dropdown, text

def main(page: ft.Page):
    page.title = "Inventory"
    page.theme = ft.Theme(font_family="Nunito")

    modal = AddModal(page)
    page.add(ft.ResponsiveRow([dropdown(), text(), add(lambda _: modal.open())]))

    items(page)

ft.app(main)