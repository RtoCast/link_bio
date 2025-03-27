import reflex as rx

#Común

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "/logo.svg"

_meta = [
    {"name":"og.type","content":"website"},
    {"name":"og.image","content":preview}        
]


#Index
index_title = "Pagina de Reto"
index_description = "Descripcion Indice"
index_meta = [
    {"name":"og.title","content":index_title},
    {"name":"og.description","content":index_description},
] 

index_meta.extend(_meta)

#Cursos
certification_title = "Titulo de la Página de Certificaciones"
certification_description = "Descripcion Certificaciones"
certification_meta = [
    {"name":"og.title","content":certification_title},
    {"name":"og.description","content":certification_description},
]

certification_meta.extend(_meta)


#Cursos
courses_title = "Titulo de la Página de cursos"
courses_description = "Descripcion cursos"
courses_meta = [
    {"name":"og.title","content":courses_title},
    {"name":"og.description","content":courses_description},
]

courses_meta.extend(_meta)