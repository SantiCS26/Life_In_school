import flet as ft
from Player import Player
from Combat import Combat
from enemy import Enemy
from Settings import Settings

def main(page: ft.Page):
    page.title = "Life In School"

    player = Player()
    enemy = Enemy()
    combat = Combat(player, enemy)
    settings = Settings()

    # **** Player Values to Display ****
    health = ft.Text(value=f"HEALTH: {player.getHP()}")
    money = ft.Text(value=f"MONEY: {player.getMoneyAmount()}")

    # Function to update displayed health and money
    def update_display():
        health.value = f"HEALTH: {player.getHP()}"
        money.value = f"MONEY: {player.getMoneyAmount()}"
        page.update()

    #def button_is_clicked():


    def navigate_to(page_name):
        if page_name == "page1":
            page.views.append(ft.View(
                controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[health],
                            alignment="start"
                        ),
                        ft.Column(
                            controls=[],
                            width=500
                        ),
                        ft.Column(
                            controls=[money],
                            alignment="end"
                        )
                    ],
                    alignment="center"
                ),
                ft.Row(
                    controls=[ft.ElevatedButton(text="Go back to Main Menu", on_click=lambda _: go_back())],
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.OutlinedButton(text="Add Health", on_click=lambda e: [player.add_health(1), update_display()], width=200),
                                ft.OutlinedButton(text="Remove Health", on_click=lambda e: [player.remove_health(1), update_display()], width=200)
                            ],
                            alignment="start",
                            width=200
                        ),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.OutlinedButton(text="Attack Button", on_click=lambda e: [combat.player_attack(), combat.enemy_attack(), update_display()], width=200),
                                    ]
                                )
                            ],
                            alignment="center"
                        ),
                        ft.Column(
                            controls=[
                                ft.OutlinedButton(text="Add Money", on_click=lambda e: [player.add_money(1), update_display()], width=200),
                                ft.OutlinedButton(text="Remove Money", on_click=lambda e: [player.remove_money(1), update_display()], width=200),
                            ],
                            alignment="end",
                            width=200
                        )
                    ],
                    alignment="center"
                ),
            ]
            ))
        page.update()

    # Function to go back to the main menu
    def go_back():
        page.views.pop()
        page.update()

    # Main Menu buttons
    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls = [
                        ft.Text(
                            "Welcome to Life in School\n",
                            size=40,
                            text_align="CENTER",
                            ),
                    ],
                    alignment="CENTER",
                ),
                ft.Row(
                    controls = [
                        ft.TextField(label="Enter Your Name", on_submit= lambda e: [settings.set_name(e.control.value), settings.test_name()]),
                    ],
                    alignment="CENTER"
                ),
                ft.Row(
                    controls = [
                        ft.Text(
                            "\n\nPlease Select Your Difficulty:\n",
                            size=20,
                            text_align="CENTER"
                        ),
                    ],
                    alignment="CENTER"
                ),
                ft.Row(
                    controls = [
                        ft.Column(
                            controls=[
                                ft.OutlinedButton(text="Easy", on_click=lambda e: [settings.set_Difficulty("Easy"), settings.test_Selection()], width=200)
                            ],
                            alignment="CENTER"
                        ),
                        ft.Column(
                            controls=[
                                ft.OutlinedButton(text="Medium", on_click=lambda e: [settings.set_Difficulty("Medium"), settings.test_Selection()], width=200)
                            ],
                            alignment="CENTER"
                        ),
                        ft.Column(
                            controls=[
                                ft.OutlinedButton(text="Hard", on_click=lambda e: [settings.set_Difficulty("Hard"), settings.test_Selection()], width=200)
                            ],
                            alignment="CENTER"
                        ),
                    ],
                    alignment="CENTER"
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Go to Page 1", on_click=lambda _: navigate_to("page1")),
                    ],
                    alignment="CENTER"
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)

