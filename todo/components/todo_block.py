import reflex as rx


def todo_block(item: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                item,
                class_name="text-2xl text-white font-semibold",
            ),
            rx.icon(
                "trash", class_name="hover:text-purple-500", size=30, color="white"
            ),
            class_name="flex items-center justify-between p-4",
        ),
        class_name="mt-2 p-4 w-3/4 h-24 rounded-2xl text-lg md:text-2xl bg-indigo-600 hover:scale-105 hover:shadow-lg",
    )
