import reflex as rx

from link_bio.styles.colors import Color

class FloatButton(rx.Component):    
    #Librería Ant Design
    #Como se invoca el Componente como si usaramos su librería  Ej. import { FloatButton } from 'antd',
    library = "antd"
    tag = "FloatButton"
    #icon = rx.image(src="/icons/strava.svg")
     
    #print(icon)           
    #icon : rx.Var[rx.image]
    #href : rx.Var[str] 
    target = "_blank"
    badge = {"dot": True, "color": Color.SECONDARY}
    
float_button = FloatButton.create    