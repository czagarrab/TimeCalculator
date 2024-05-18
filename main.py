import flet as ft
from flet import (
    Page
)
import time_calculator

def main(page: Page):
    page.title = "Calculadora de tiempo"
    page.window_resizable = False
    page.window_width = 390
    page.window_height = 435
    page.padding = 0
    # create application instance
    calc = time_calculator.TimeCalculatorApp()
    # add application's root control to the page
    page.on_keyboard_event = calc.on_keyboard
    # AppBar
    # page.appbar = ft.AppBar(
    #     leading=ft.Icon(ft.icons.PALETTE),
    #     leading_width=40,
    #     title=ft.Text("AppBar Example"),
    #     center_title=False,
    #     bgcolor=ft.colors.SURFACE_VARIANT,
    #     actions=[
    #         ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
    #         ft.IconButton(ft.icons.FILTER_3),
    #         ft.PopupMenuButton(
    #             items=[
    #                 ft.PopupMenuItem(text="Item 1"),
    #                 ft.PopupMenuItem(),  # divider
    #                 ft.PopupMenuItem(
    #                     text="Checked item", checked=False, 
    #                 ),
    #             ]
    #         ),
    #     ],
    # )
    page.add(calc)

ft.app(target=main)

