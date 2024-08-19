import reflex as rx

config = rx.Config(
    app_name="todo",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["daisyui"],
    },
    # Add this line to install Daisy UI via npm
    npm_dependencies={"daisyui": "latest"},
)
