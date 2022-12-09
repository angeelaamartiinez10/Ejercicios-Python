import flet as ft



def main(page: ft.Page):
    page.title="Tkinter no mola nada-->> Flet:))))"

    def mostraNombre(e):
        t.value=textField_Nombre.value
        page.update()

    #componente texto
    t =ft.Text(value="Introducción a flet", color="blue",size=25)
    page.add(t) #add hace dos cosas. 1-AÑADIR 2-ACTUALIZAR

    #componentes boton
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=mostraNombre)   
    page.add(bt)

    textField_Nombre=ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    
    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Mujer"),ft.dropdown.Option("Hombre"),])
    page.add(dropdown_menu)
    dropdown_menu.options.append(ft.dropdown.Option("Mejor ni te lo digo"))
    page.update()

    value=int
    slider_edad=ft.Slider (min=0, max=120, divisions=120, label="Edad:{value}")
    page.add(slider_edad)

ft.app(target=main)