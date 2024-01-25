import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"2014 - {datetime.date.today().year} David Buitrago",
            href="http://davidb.dev",
            is_external=True),
        rx.text("BUILDING SOFTWARE FROM MADRID TO THE WORLD"),
    )