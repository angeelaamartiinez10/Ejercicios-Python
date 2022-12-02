import flet as ft



def main(page: ft.Page):
    page.title="Tkinter no mola nada-->> Flet:))))"

    def cambiarColor(e):
        t.color="pink"
        for i in range(10):
            text=ft.Text(value=f"texto numero {i}",size=30)
            page.add(text)


    #componente texto
    t =ft.Text(value="Introducción a flet", color="Cyan",size=25)
    page.add(t) #add hace dos cosas. 1-AÑADIR 2-ACTUALIZAR

    #componentes boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiarColor)   
    page.add(bt)



ft.app(target=main)