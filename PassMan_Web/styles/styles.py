import reflex as rx
from .fonts import Font
from .colors import Color


STYLESHEETS = [
    "https://fonts.cdnfonts.com/css/glacial-indifference-2"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": Color.BLACK.value,
    "background-image": "linear-gradient(to right, #030849 0%, #a9a7c3 100%)"
}
