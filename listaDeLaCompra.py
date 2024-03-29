import flet as ft



def main(page: ft.Page):

    page.title="***Superamarket***"

    img = ft.Image(
        src=f"/imagenes/supermercado.png",
        width=170,
        height=170,
    )
    page.add(img)

    def boton_seleccionarC(e):
        textoc.value = (f"Carne seleccionada  {c1c.value}, {c2c.value}, {c3c.value}")
        page.update()

    def seleccionar_Carne(e):
        try:
            page.remove(c1c, c2c, c3c, bc, textoc)
        except:
            print("fallado pero pasamos")
        try:
            page.remove(c1, c2, c3, b, texto)
        except:
            print("fallado pero pasamos")
        try:
            page.remove(c1v, c2v, c3v, bv, textov)
        except:
            print("fallado pero pasamos")

        if dropdown_menu.value == "Carne":
            page.add(c1c, c2c, c3c, bc, textoc)
        elif dropdown_menu.value == "Pescado":
            page.add(c1, c2, c3, b, texto)
        elif dropdown_menu.value == "Verduras":
            page.add(c1v, c2v, c3v, bv, textov)
        

        
    def boton_seleccionarP(e):
        texto.value = (f"Pescado seleccionada  {c1.value}, {c2.value}, {c3.value}")
        page.update()

    def seleccionar_Pescado(e):
        if dropdown_menu == "Pescado":
            page.add(c1, c2, c3, b, texto)
        else:
            page.remove(c1, c2, c3, b, texto)


    def boton_seleccionarV(e):
        textov.value = (f"Verdura seleccionada  {c1v.value}, {c2v.value}, {c3v.value},")
        page.update()


    textoc = ft.Text(value="Carnes seleccionadas")
    c1c = ft.Checkbox(label="Pollo--> 4.49€/kg", value=False)
    c2c= ft.Checkbox(label="Ternera--> 5.19€/kg", value=False)
    c3c = ft.Checkbox(label="Cerdo--> 2.59€/kg", value=False)
    bc = ft.ElevatedButton(text="guardar", on_click=boton_seleccionarC)
    #page.add(c1c, c2c, c3c, bc, textoc)

    

    texto = ft.Text(value="Pescados seleccionados")
    c1 = ft.Checkbox(label="Sardinas", value=False)
    c2 = ft.Checkbox(label="Merluza", value=False)
    c3 = ft.Checkbox(label="Bacalao", value=False)
    b = ft.ElevatedButton(text="guardar", on_click=boton_seleccionarP)
    #page.add(c1, c2, c3, b, texto)


    textov = ft.Text(value="Verduras seleccionadas")
    c1v = ft.Checkbox(label="Tomates", value=False)
    c2v = ft.Checkbox(label="Lechuga", value=False)
    c3v = ft.Checkbox(label="Zanahorias", value=False)
    bv = ft.ElevatedButton(text="guardar", on_click=boton_seleccionarV)
    #page.add(c1v, c2v, c3v, bv, textov)

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

    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Carne") ,ft.dropdown.Option("Pescado"),ft.dropdown.Option("Verduras")], on_change=seleccionar_Carne)
    page.add(dropdown_menu)
    
    page.update()




ft.app(target=main, assets_dir="recursos")
