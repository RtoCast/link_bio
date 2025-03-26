import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.styles.styles import Size as Size

class State(rx.State):
    pass
    

def index() -> rx.Component :
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(            
                header(),
                links(),
                #CSS
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y=Size.BIG,
                margin_X=Size.BIG
                
                #justify = "between"
            ),            
        ),
        footer()
    )
    


# Personalizamos los componente en reflex


app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets = styles.STYLESHEETS
)

app.add_page(
    index,
    title= "Pagina de Reto",
    description= "Descripcion",
    image= "avatar.png"
)

app._compile()

