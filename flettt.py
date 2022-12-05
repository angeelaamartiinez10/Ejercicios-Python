import flet as ft



def main(page: ft.Page):
    page.title="Tkinter no mola nada-->> Flet:))))"

    def mostraNombre(e):
        t.value=textField_Nombre.value
        page.update()

    #componente texto
    t =ft.Text(value="Introducción a flet", color="Cyan",size=25)
    page.add(t) #add hace dos cosas. 1-AÑADIR 2-ACTUALIZAR

    #componentes boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=mostraNombre)   
    page.add(bt)

    textField_Nombre=ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre.focus()
    page.add(textField_Nombre)


ft.app(target=main)