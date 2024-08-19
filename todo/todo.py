"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from todo.components.todo_block import todo_block


class State(rx.State):
    """The app state."""

    todo_list = ["apple", "orange"]
    new_todo = ""

    def set_new_todo(self, value: str):
        self.new_todo = value

    def add_todo(self, todo_item: str):
        self.todo_list.append(todo_item)

    def remove_todo(self, index: int):
        if 0 <= index < len(self.todo_list):
            self.todo_list.pop(index)


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
            rx.heading("Search Todo", class_name="mt-20"),
            rx.input(
                placeholder="Enter your search term...",
                class_name="p-4 w-3/4 h-20 rounded-2xl text-lg md:text-2xl",
            ),
            rx.heading("Add Todo", class_name="mt-20"),
            rx.form(
                rx.input(
                    placeholder="Add a new to-do...",
                    class_name="mb-10 p-4 w-3/4 h-20 rounded-2xl text-lg md:text-2xl mx-auto",
                    value=State.new_todo,
                    on_change=State.set_new_todo,
                ),
                enter_key_submit=True,
            ),
            rx.foreach(State.todo_list, todo_block),
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
