import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size        

def title(text:str) -> rx.Component: 
    return rx.heading(
        text,
        size = "6",
        #CSS
        style = styles.title_style,
        padding_y = Size.SMALL
    )    