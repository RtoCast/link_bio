import reflex as rx
import link_bio.styles.styles as styles
import link_bio.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.styles.styles import Size as Size
from link_bio.api.api import hello

class IndexState(rx.State):
    
    @rx.var
    def say_hello(self)->str:
        return hello()    

@rx.page(
    title = utils.index_title,
    description = utils.index_description,
    image= utils.preview,
    meta = utils.index_meta
)
def index() -> rx.Component:    
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(            
                rx.text(IndexState.say_hello),      
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