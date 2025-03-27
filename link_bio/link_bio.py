import reflex as rx
import link_bio.constants as constants
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.pages.certifications import certifications

# class State(rx.State):
#     pass
    
app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLE
    # head_components= [
    #     rx.script(src=f"https://www.googletagmanager.com/gtag/js?id=G-QVRYTWM0N7"),
    #     rx.script(
    #         """        
    #         "window.dataLayer = window.dataLayer || [];
    #         function gtag(){dataLayer.push(arguments);}
    #         gtag('js', new Date());
    #         gtag('config', 'G-QVRYTWM0N7');
    #         """
    #     )            
    # ]
)



