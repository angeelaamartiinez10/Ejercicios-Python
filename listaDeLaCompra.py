import flet as ft


def main(page: ft.Page):
    page.title="***Lista de la compra***"
   
    def mostraNombre(e):
        t.value=textField_Nombre.value
        page.update()
    
    t =ft.Text(value="Tu lista de la compra, facil y sencilla", color="purple",size=20)
    page.add(t) 
        
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=mostraNombre)   
    page.add(bt)

    textField_Nombre=ft.TextField(label="Escriba su nombre", hint_text="Nombre y apellidos")
    page.add(textField_Nombre)
 
    
    slider_coste=ft.Slider (min=0, max=1000, divisions=1000, label="Coste máximo:{value}€")
    page.add(slider_coste)




####AÑADIR TEXT BUTTON---> PORQUE CADA VE QEU SE PULSA SE SUME UN PRODUCTO


    
    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Mujer"),ft.dropdown.Option("Hombre"),])
    page.add(dropdown_menu)
    dropdown_menu.options.append(ft.dropdown.Option("Mejor ni te lo digo"))
    page.update()







ft.app(target=main)
