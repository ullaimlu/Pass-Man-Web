import reflex as rx
from PassMan_Web.styles.colors import *
from utils.pipelines import *
from utils.config_user import *

class SignUpState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        config_user(self.form_data["email"],self.form_data["pass"])

class PassStrength(rx.State):
    passwd: str = ""
    value: int = 20
    message: str ="Create a strong password"
    state: str = "Weak"
    color: str = "red"

    def check_strength(self, passwd):
        self.passwd=passwd
        has_lowercase = any(char.islower() for char in self.passwd)
        has_uppercase = any(char.isupper() for char in self.passwd)
        has_digit = any(char.isdigit() for char in self.passwd)
        has_punctuation = any(char in string.punctuation for char in self.passwd)

        if len(self.passwd) < 12:
            self.value= 20
            self.message= "Your password must be 12 long minimum"
            self.state= "Weak"
            self.color= "red"
        
        elif not has_lowercase:
            self.value=40
            self.message= "Your password must have lowercase"
            self.state= "Medium"
            self.color= "orange"

        elif not has_uppercase:
            self.value=40
            self.message= "Your password must have uppercase"
            self.state= "Medium"
            self.color= "orange"

        elif not has_digit:
            self.value=40
            self.message= "Your password must have at least a digit"
            self.state= "Medium"
            self.color= "orange"
        
        elif not has_punctuation:
            self.value=60
            self.message= "Your password must have at least an special character"
            self.state= "Good"
            self.color= "yellow"

        else: 
            self.value=100
            self.message= "Nice :)"
            self.state= "Strong"
            self.color= "green"

        


def login_form() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.form(
                rx.center(
                    rx.text("Sign in",
                        color= Color.WHITET.value,
                        font_size="3em",
                        font_weight="bold"), 
                    width="100%"),
                rx.text("Email",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="email",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.text("Password",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="pass",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.center(
                    rx.text("¿Forgot your password?",
                        margin_top="1em",
                        color= Color.WHITET.value,
                        margin_left="0.5em",
                        text_decoration="underline white",
                        font_size="1em",
                        font_weight="bold"), 
                ),
                
                rx.flex(
                    rx.button(
                        "Sign In",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        padding_x= "3em",
                        padding_y= "2em",
                        margin_left="2.5em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    rx.button(
                        "Sign In with Google",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        padding_x= "3em",
                        padding_y= "2em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    spacing="2"
                
                ),
                rx.center(
                    rx.text("¿You don't have an account yet?",
                        rx.chakra.span(" Sign Up",text_decoration="underline white"),
                        margin_top="1em",
                        color= Color.WHITET.value,
                        margin_left="0.5em",  
                        font_size="1em",
                        font_weight="bold"), 
                ),
                width= "100%",
                margin_top= "9em"
                
            ),
            rx.image(src="/logog.png", width="30%", margin_top="20%"),
            width="40em",
            margin="0",
            height="100%",
            align="center",
            spacing="8"
        ),
        width="100%"
    )

def sign_up_form() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.form(
                rx.center(
                    rx.text("Sign up",
                        color= Color.WHITET.value,
                        font_size="3em",
                        font_weight="bold"), 
                    width="100%"),
                rx.text("Email",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="email",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.text("Create Password",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="pass",
                    border= "none",
                    border_top= "1px",
                    on_change= PassStrength.check_strength,
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.text(PassStrength.state,
                    margin_top="1em",
                    color= PassStrength.color,
                    margin_left="1em",
                    font_size="0.8em",
                    font_weight="bold"),
                rx.progress(
                    value=PassStrength.value, 
                    color_scheme= PassStrength.color,
                ),
                rx.text(PassStrength.message,
                    margin_top="1em",
                    color= Color.LILAC2.value,
                    margin_left="0.5em",
                    font_size="0.8em",
                    font_weight="bold"),
                rx.text("Confirm Password",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="pass",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                
                rx.flex(
                    rx.button(
                        "Create Account",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        type="submit",
                        padding_x= "3em",
                        padding_y= "2em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    rx.button(
                        "Sign Up with Google",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        padding_x= "3em",
                        padding_y= "2em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    spacing="2"
                
                ),
                rx.center(
                    rx.text("¿You already have an account?",
                        rx.chakra.span(" Sign In",text_decoration="underline white"),
                        margin_top="1em",
                        color= Color.WHITET.value,
                        margin_left="0.5em",  
                        font_size="1em",
                        font_weight="bold"), 
                ),
                width= "100%",
                margin_top= "6em",
                on_submit=  SignUpState.handle_submit,
                reset_on_submit=True,
            ),
            rx.image(src="/logog.png", width="30%", margin_top="20%"),
            width="40em",
            margin="0",
            height="100%",
            align="center",
            spacing="8"
        ),
        width="100%"
    )