import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(title:str, body:str, image:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,
                    #CSS
                    width = styles.Size.BIG,
                    height = styles.Size.BIG,
                    margin = Size.MEDIUM
                ),
                rx.vstack(
                    rx.text(title, style = styles.button_title_style),
                    rx.text(body, style = styles.button_body_style),
                    spacing = "1",
                    #CSS
                    align_items = "start"
                ),
                width = "100%"
            )
        ), 
        href=url,
        is_external=True,
        #CSS
        width="100%"    
    
    
    )



