import reflex as rx
from PassMan_Web.components import *
#from database.pipelines import CoursePipeline



def login() -> rx.Component:
    return rx.cond(
        SignInState.sign_in_state2,
        rx.vstack(
            login_form()
        ),
        rx.vstack(
            navbar_login(),
            login_form()
        )
    ) 
    
        