import reflex as rx
from PassMan_Web.components import *
#from database.pipelines import CoursePipeline



def sign_up() -> rx.Component:
    return rx.vstack(
        navbar_sign_up(),
        sign_up_form()
    )    