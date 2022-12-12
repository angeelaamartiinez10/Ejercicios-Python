import flet as ft


def main(page: ft.Page):
    page.title="***Lista de la compra***"
   
    def boton_seleccionar(e):
        t.value = (f"Comida seleccionada  {c1.value}, {c2.value}, {c3.value}, {c4.value}, {c5.value}.")
        page.update()

    texto = ft.Text(value="Selecciona")
    c1 = ft.Checkbox(label="Pollo", value=True)
    c2 = ft.Checkbox(label="Ternera", value=True)
    c3 = ft.Checkbox(label="Cerdo", value=True)
    c4 = ft.Checkbox(label="Chorizo", disabled=True)
    b = ft.ElevatedButton(text="guardar", on_click=boton_seleccionar)
    page.add(c1, c2, c3, c4, b, texto)


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

    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Carne"),ft.dropdown.Option("Pescado"),])
    page.add(dropdown_menu)
    dropdown_menu.options.append(ft.dropdown.Option("Verduras"))
    page.update()




ft.app(target=main)
