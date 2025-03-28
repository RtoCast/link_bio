import reflex as rx
import link_bio.constants as constants
from link_bio.styles.colors import Color

class FloatButton(rx.Component):    
    #Librería Ant Design
    #Como se invoca el Componente como si usaramos su librería  Ej. import { FloatButton } from 'antd',
    library = "antd"
    tag = "FloatButton",
    #icon = rx.image(src="/icons/strava.svg")
     
    #print(icon)           

    href = "https:// " #constants.STRAVA_URL
    target = "_blank"
    badge = {"dot": True, "color": Color.SECONDARY}
    
float_button = FloatButton.create    