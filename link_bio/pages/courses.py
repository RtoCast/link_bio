import reflex as rx
import link_bio.styles.styles as styles
import link_bio.utils as utils
from link_bio.routes import Route
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.styles.styles import Size as Size

@rx.page(
    route = Route.COURSES,
    title = utils.courses_title,
    description = utils.courses_description,
    image= utils.preview,
    meta = utils.courses_meta
)
def courses() -> rx.Component:    
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(            
                header(),
                index_links(),
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