"""TODO app."""

import reflex as rx
from typing import List


class State(rx.State):
    """The app state."""

    items: List[str] = []
    search_term: str = ""

    def add_item(self, form_data: dict[str, str]):
        """Add a new item to the todo list."""
        new_item = form_data.get("new_item")
        if new_item:
            self.items.append(new_item)

    def finish_item(self, item: str):
        """Finish an item in the todo list.

        Args:
            item: The item to finish.
        """
        self.items.pop(self.items.index(item))

    def set_search_term(self, term: str):
        self.search_term = term

    @rx.var
    def filtered_items(self) -> list[str]:
        """Return a list of items filtered by the search term.

        If the search term is empty, return all items. Otherwise, return
        a list of items that contain the search term, case-insensitively.
        """
        return [item for item in self.items if self.search_term.lower() in item.lower()]


def todo_block(item: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                item,
                class_name="text-2xl text-white font-semibold",
            ),
            rx.icon(
                "trash",
                class_name="hover:text-purple-500",
                size=30,
                color="white",
                on_click=lambda: State.finish_item(item),
            ),
            class_name="flex items-center justify-between p-4",
        ),
        class_name="mt-2 p-4 w-3/4 h-24 rounded-2xl text-lg md:text-2xl bg-indigo-600 hover:scale-105 hover:shadow-lg",
    )


@rx.page(route="/", title="Home")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            # rx.box("Daisy UI", class_name="btn btn-primary btn-outline"),
            rx.heading("Search Todo", class_name="mt-20"),
            rx.form(
                rx.input(
                    placeholder="Enter your search term...",
                    on_change=State.set_search_term,
                    value=State.search_term,
                    class_name="p-4 w-3/4 h-16 md:h-20 rounded-2xl text-md md:text-2xl mx-auto",
                ),
            ),
            rx.heading("Add Todo", class_name="mt-20"),
            rx.form(
                rx.input(
                    name="new_item",
                    placeholder="Add a new to-do...",
                    class_name="mb-10 p-4 w-3/4 h-16 md:h-20 rounded-2xl text-md md:text-2xl mx-auto",
                ),
                enter_key_submit=True,
                reset_on_submit=True,
                on_submit=State.add_item,
            ),
            rx.foreach(State.filtered_items, todo_block),
            rx.logo(
                class_name="absolute bottom-0 left-1/2 transform -translate-x-1/2 mb-4"
            ),
            align="center",
        ),
        class_name="mx-auto",
    )


style = {
    "font_family": "MonaspaceArgon",
    "font_size": "16px",
}

app = rx.App(
    style=style,
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "/fonts/myfont.css",
    ],
)
