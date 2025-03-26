import reflex as rx
from link_bio.styles.styles import Size as Size        
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def info_text(title:str, body:str) -> rx.Component: 
    return rx.center(
        rx.box(
            rx.text(
                title ,
                as_="span",
                #CSS 
                font_weight = "bold",
                color = Color.PRIMARY
            ),
            f" {body}",
            #CSS 
            font_size = Size.MEDIUM,
            color = TextColor.BODY                
        ),
    )    