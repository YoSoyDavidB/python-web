import reflex as rx
from link_bio.views.links.links import links

def header() -> rx.Component:
    return rx.vstack(
       rx.avatar(name="David B", size="xl"),
       rx.text("@David-Dev"),
       links()
    )