import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src = "/logo.svg",
            #CSS
            height = Size.BIG,
            background_color = "transparent"
        ),
        rx.text(
            rx.link(
                f"@2020 - {datetime.date.today().year} --> que lleva a Reflex", 
                href = "https://reflex.dev/docs/library", 
                is_external = True,
                underline= "none",
                #CSS 
                font_size = Size.MEDIUM
            ),
        ),
        rx.text(
            "¡Comprometido con la excelencia!",
            #CSS 
            font_size = Size.MEDIUM,
            margin_top = Size.ZERO
        ),
        #CSS
        #margin_bottom = Size.BIG,
        padding_bottom = Size.BIG,
        padding_X = Size.BIG,
        color = TextColor.FOOTER, 
        
        align= "center",
        spacing = "1"
    )