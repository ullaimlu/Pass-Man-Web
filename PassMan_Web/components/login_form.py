import reflex as rx
from PassMan_Web.styles.colors import *
from .my_space import *
from .sidebar import *
from .websites import *
from utils.pipelines import *
from utils.config_user import *
from security_code.send_security_code import send_security_code
import hashlib

u= PassManUserPipeline()
w= WebsitePipeline()

class SignInState(rx.State):
    form_data: dict = {}
    security_code:  str = '0'
    sign_in_state: bool = False
    sign_in_state2: bool = False
    user_path: str= ""

    def handle_submit(self, form_data: dict):
        try:
            self.form_data = form_data
            hashed_mp = hashlib.sha256(self.form_data["pass"].encode()).hexdigest()       
            passwd=u.get_pass_by_username(self.form_data["email"])
            phone=u.get_phone_by_username(self.form_data["email"])
            self.user_path= f"websites/{u.get_id_by_username(self.form_data["email"])}"
            if passwd == hashed_mp:
                self.sign_in_state= True
                #self.security_code= send_security_code(phone)
            else: self.sign_in_state= False
        except: pass

    def security_code_handle(self, form_data: dict):
        if self.security_code == form_data["security_code"]:
            self.sign_in_state2= True
        else: self.sign_in_state2= False

    def log_out(self):
        self.sign_in_state1= False
        self.sign_in_state2= False
        return rx.redirect("../../")

class PasswordInputLogin(rx.State):
    state: str = "password"
    icon: str = "eye"
    
    def change_state(self):
        if self.state=="password":
            self.state= "text"
            self.icon= "eye_off"
        else: 
            self.state="password"
            self.icon="eye"

def login_form() -> rx.Component:

    return rx.cond(
        SignInState.sign_in_state2,
        rx.center(
            rx.vstack(
                rx.text("You are verified!",
                    color= Color.WHITET.value,
                    font_size="3em",
                    font_weight="bold"),
                rx.button(rx.icon("log_in", size=15),
                    "Go to my space",
                    margin_left= "5em",
                    _hover={"background_color": Color.GRAY.value},
                    background_color=Color.LILAC.value,
                    color=Color.BLACK.value,
                    on_click=rx.redirect(SignInState.user_path),
                    padding_x= "3em",
                    padding_y= "2em",
                    border_radius="3em",
                    margin_top= "1em",
                    text_align="left", 
                ),
                margin_top="20em"
            ),
            width="100%",
            height="100%"
        ),
        rx.center(
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
                    rx.flex(
                        rx.input(
                            name="pass",
                            border= "none",
                            type=PasswordInputLogin.state,
                            border_top= "1px",
                            background= Color.LILAC2.value,
                            height="3em",
                            width="25em"),


                        rx.button(rx.icon("eye", size=15),
                            radius="full",
                            color=Color.BLACK.value,
                            background_color=Color.LILAC.value,
                            type="button",
                            on_click=PasswordInputLogin.change_state),
                        spacing="2",
                    ),
                    
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
                        rx.alert_dialog.root(
                            rx.alert_dialog.trigger(
                                rx.button(
                                    "Sign In",
                                    _hover={"background_color": Color.GRAY.value},
                                    background_color=Color.LILAC.value,
                                    color=Color.BLACK.value,
                                    type="submit",
                                    form="form1",
                                    padding_x= "3em",
                                    padding_y= "2em",
                                    margin_left="2.5em",
                                    border_radius="3em",
                                    margin_top= "1em",
                                    text_align="left", 
                                ),
                            ),
                            
                            rx.cond(
                                SignInState.sign_in_state,
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Enter the security code"),
                                    rx.alert_dialog.description(
                                        "A Security code was sent to your Whatsapp ...",   
                                    ),
                                    rx.form(
                                        rx.input(placeholder="Enter the code",
                                            name="security_code",
                                            height="2.8em",
                                            bg=Color.WHITE.value,
                                            radius="full",
                                            width="100%",
                                            
                                        ),
                                        rx.flex(
                                            rx.alert_dialog.action(
                                                rx.button("Submit",
                                                    radius="full",
                                                    background_color=Color.PURPLE.value,
                                                    type="submit",
                                                    form="form2"
                                                    ),
                                            ),
                                            rx.alert_dialog.cancel(
                                                rx.button("Cancel",
                                                    radius="full",
                                                    background_color=Color.PURPLE.value),
                                            ),
                                            spacing="3",
                                            margin_top="1em",
                                        ),
                                        id= "form2",
                                        width="70%",
                                        on_submit=SignInState.security_code_handle,
                                        reset_on_submit=True,
                                    ),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Your Credentials are wrong"),
                                    rx.alert_dialog.description(
                                        "Try login again ...",   
                                    ),
                                    rx.alert_dialog.cancel(
                                        rx.button("Ok",
                                            radius="full",
                                            background_color=Color.PURPLE.value,
                                            margin_top="1em"),
                                    ),
                                    
                                ),
                            ),
                            background_color=Color.LILAC2.value,
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
                    id="form1",
                    width= "100%",
                    margin_top= "9em",
                    on_submit=  SignInState.handle_submit,
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
        
    )





"""def principal_in(tab: str, content: list) -> rx.Component:
    
    content=websites(content)
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.button(rx.icon("log_out", size=15),
                "Log Out",
                on_click=SignInState.log_out,
                _hover={"background_color": Color.GRAY.value},
                background_color=Color.LILAC.value,
                color=Color.BLACK.value,
                padding_y= "0.5em",
                border_radius="3em",
                margin_top="1em",
                margin_left="84em",
                width="8em"),
            my_space_tittle(tab),
            my_space(tab, content),
            width="100%"
        )
    )"""