"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


class State(rx.State):
    """The app state."""


# def action_bar() -> rx.Component:
#     return rx.form(
#         rx.hstack(
#             rx.input(
#                 placeholder="Summarize this video...",
#                 value=State.question,
#                 on_change=State.set_question,
#                 style=style.input_style,
#                 radius="large",
#                 variant="surface",
#                 size="3",
#             ),
#             rx.button(
#                 "Ask AI",
#                 type="submit",
#                 style=style.button_style,
#                 size="3",
#             ),
#         ),
#         on_submit=State.answer,
#         enter_key_submit=True,
#         reset_on_submit=False,
#     )


@rx.page(route="/", title="Home")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            # rx.box("Daisy UI", class_name="btn btn-primary btn-outline"),
            rx.heading("Add Todo", class_name="mt-20"),
            rx.input(
                placeholder="Add a new to-do...",
                class_name="p-4 w-3/4 h-20 rounded-2xl text-2xl",
            ),
            rx.heading("Search Todo", class_name="mt-20"),
            rx.input(
                placeholder="Enter your search term...",
                class_name="p-4 w-3/4 h-20 rounded-2xl text-2xl",
            ),
            rx.logo(
                class_name="absolute bottom-0 left-1/2 transform -translate-x-1/2 mb-4"
            ),
            align="center",
        ),
        class_name="mx-auto",
    )


style = {
    "font_family": "Monaspace Argon",
    "font_size": "16px",
}

app = rx.App(style=style)
