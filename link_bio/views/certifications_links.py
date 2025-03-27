import reflex as rx
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.constants as constants

 
def certifications_links() -> rx.Component: 
    return rx.vstack(        
        title("Certificaciones"),
        link_button(
            "Certificación 01",
            "Certificaciones Des",
            "/icons/file-pdf.svg",
            Route.COURSES,
            is_external = False
        ),
        link_button(
            "Certificación 02",
            "Certificaciones Des",
            "/icons/file-pdf.svg",
            Route.COURSES,
            is_external = False
        ),        
        #CSS
        width = "100%"
    )
