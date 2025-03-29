import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as constants
from link_bio.routes import Route
# from link_bio.components.ant_components import float_button
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(        
        rx.link(            
            rx.box(
                rx.text(
                    "Rto",
                    as_= "span",
                    #CSS
                    color =Color.PRIMARY
                ),
                rx.text(
                    "Cast",
                    as_= "span",
                    #CSS
                    color =Color.SECONDARY
                ),
                style = styles.navbar_title_style
            ),
            href= Route.INDEX
        ),
        # float_button(
        #     # icon = rx.image(src="/icons/strava.svg"),
        #     # href = constants.STRAVA_URL
        # ),
        #CSS
        position = "sticky",
        bg = Color.CONTENT,
        padding_x = Size.DEFAULT,
        padding_y = Size.SMALL,
        z_index = "999",
        top = "0"            
    )