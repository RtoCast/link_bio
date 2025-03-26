import reflex as rx
import link_bio.constants as constants
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color


def header() -> rx.Component: 
    return rx.vstack(   
        rx.hstack(
            rx.avatar(
                fallback="AR", 
                radius="full", 
                size = "6",
                src = "avatar.png",
                #CSS
                padding = "2px",
                border = "5px",
                border_color = Color.PRIMARY
            ),
            rx.vstack(
                rx.box(
                    rx.heading(
                        "Angel Reto", 
                        size = "6"
                    ),
                    rx.text(
                        "@Rtocast",
                        #CSS
                        margin_top = Size.ZERO,
                        color = TextColor.BODY
                    ),                         
                ),
                rx.hstack(
                    link_icon(
                        "icons/linkedin.svg",
                        constants.LINKEDIN_URL
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        constants.INSTAGRAM_URL                        
                    ),
                    link_icon(
                        "icons/strava.svg",
                        constants.STRAVA_URL
                    )
                ),
                spacing = "2",
                
                #CSS
                align_items = "start"                
            ),                    
            spacing = "1"
        ),

        rx.flex(
            info_text("+4","años de experiencia"),
            rx.spacer(),
            info_text("+4","Certificaciones SAP"),
            rx.spacer(),
            info_text("+4","Clientes en SAP"),
            #CSS
            width="100%",
        ),
        rx.text(
            """ Describe myself as an only word: Commitment. Day by day, I learn how to be more innovative and chameleonic in
                the majority of the contexts; Also, I am an automation lover and goals focused in order to accelerate key functional
                process. With my expertise, I acquired experience about how to deal with complex problem and solve it.
                Furthermore, work as team spirit builder in order to go through team’s problem. As a remote worker, I understand
                the key points of effective communication and how it can make the difference.""",
            #CSS
            color = TextColor.BODY,
            font_size = Size.MEDIUM
        ),
        spacing = "1"
    )
