import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Github", "http://github.com"),
        link_button("LinkedIn", "http://linkedin.com"),
        link_button("Twitter", "http://twitter.com"),
        link_button("twitch", "http://twitch.tv")
    )