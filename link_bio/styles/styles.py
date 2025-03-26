import reflex as rx
import enum as Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FontWeight

#Constants
MAX_WIDTH = "600px"

#Fuentes de Google Fonts
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wgth@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Tektur:wgth@400&display=swap"
]




# Al tener páginas web dinamicas no se estila usar px
# en vez de px, se usa em 
# Donde 1em va a tomar el tamaño de fuente de la apliación

#Sizes
class Size():
    ZERO  = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    
    
#Styles, Propiedad de Reflex para definir estilos Globales

BASE_STYLE = {
    
    "font-family": Font.DEFAULT,
    "font-weight": FontWeight.LIGHT,
    "background-color": Color.BACKGROUND,
    
    rx.heading: {
        "color" : TextColor.HEADER,
        "font-family" : Font.TITLE,  
        "font-weight": FontWeight.MEDIUM
    },
    
    rx.button: {
        "width": "100%",
        "height": "100%",
        #"display": "block",
        
        "padding": Size.SMALL,
        "border-radius": Size.DEFAULT, #"30px"
        
        "color": TextColor.HEADER,
        "background-color": Color.CONTENT,
        
        "white_space": "normal", # No Truncado de textos
        "text_align": "start",
        
        "_hover":{
            "background-color": Color.SECONDARY,
        }
    },
    
    # rx.link: {
    #     "text-decoration":"none",
    #     "_hover": {} 
    # }
}



navbar_title_style = dict(
    font_family = Font.LOGO,
    font_weight= FontWeight.MEDIUM,
    font_size = Size.LARGE
)  

title_style = dict(
    width = "100%",
    padding = Size.DEFAULT,
)    


# DIC <- Diccionario de Propiedades
button_title_style = dict(
    font_family = Font.TITLE,
    font_weight= FontWeight.MEDIUM,
    font_size = Size.BIG,
    color = TextColor.HEADER
)

button_body_style = dict(
    font_family = Font.DEFAULT,
    font_weight= FontWeight.LIGHT,
    font_size = Size.MEDIUM,
    color = TextColor.BODY
)

# EJEMPLO DE MERGE entre Diccionario de Propiedades de Python
# Actualizamos el diccionario `button_title_style` con las propiedades de `title_style`
#button_title_style.update(title_style)    