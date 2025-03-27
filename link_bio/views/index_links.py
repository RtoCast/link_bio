import reflex as rx
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.constants as constants

 
def index_links() -> rx.Component: 
    return rx.vstack(        
        title("Comunidad"),
        link_button(
            "Certificaciones",
            "Certificaciones Adquiridas",
            "/icons/folder.svg",
            Route.CERTIFICATIONS,
            is_external = False
        ),
        link_button(
            "Linkedin",
            "En lo profesional",
            "/icons/linkedin.svg",
            constants.LINKEDIN_URL
        ),
        link_button(
            "Instagram",
            "En lo Social",
            "/icons/instagram.svg",
            constants.INSTAGRAM_URL
        ),
        link_button(
            "Strava",
            "En lo Deportista",
            "/icons/strava.svg",
            constants.STRAVA_URL
        ),
        
        #CSS
        width = "100%"
    )
