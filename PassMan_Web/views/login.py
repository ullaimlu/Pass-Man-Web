import reflex as rx
from PassMan_Web.components import *
#from database.pipelines import CoursePipeline



def login() -> rx.Component:
    return rx.vstack(
        navbar_login(),
        login_form()
    )    
    
        