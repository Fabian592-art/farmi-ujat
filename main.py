import flet as ft

def main(page: ft.Page):
    page.title = "FARMI-UJAT"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT", size=40),
        center_title=True
    )

    # Definición de botones (igual que antes)...
    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication", size=40, color="black"),
                    ft.Text("Interacciones Medicamentosas", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor="orange100",
        color="black",
        width=200
    )

    btn_nuevo = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("add", size=40, color="black"),
                    ft.Text("Alta de \n Medicamentos", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor="orange200",
        color="black",
        width=200
    )

    btn_lista = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("list", size=40, color="black"),
                    ft.Text("Listar \n Medicamentos", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor="orange300",
        color="black",
        width=200
    )

    # Divider
    page.add(ft.Divider(color="black"))

    # Fila con los botones
    page.add(
        ft.Row(
            controls=[btn_interacciones, btn_nuevo, btn_lista],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20  # espacio entre botones
        )
    )

    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
