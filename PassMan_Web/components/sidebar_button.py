import reflex as rx
from PassMan_Web.styles.styles import Color
from utils.generate import *


class FormInputState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        print(self.form_data)
        #create_course_guide(self.form_data["course_name"])

class TextfieldControlled(rx.State):
    password: str = ""
    
    def generate_password(self):
        self.password= generatePassword(16)

class PasswordInput(rx.State):
    state: str = "password"
    icon: str = "eye"
    
    def change_state(self):
        if self.state=="password":
            self.state= "text"
            self.icon= "eye_off"
        else: 
            self.state="password"
            self.icon="eye"

def sidebar_button1(text: str, icon: str) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon(icon, size=15),
                text,
                _hover={"background_color": Color.GRAY.value},
                background_color=Color.LILAC.value,
                color=Color.BLACK.value,
                padding_x= "2em",
                padding_y= "2em",
                border_radius="3em",
                text_align="left", 
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Add a new website"),
            #rx.alert_dialog.description(
                #"* Gaps are mandatory",
                
            #),
            rx.form(
                rx.text("Website *"),
                rx.input(placeholder=" ex: Facebook",
                    name="website_name",
                    height="2.8em",
                    bg=Color.WHITE.value,
                    radius="full",
                    required=True,
                    width="100%",
                    
                ),
                rx.text("Username *"),
                rx.input(placeholder=" ex: jd_imllu",
                    name="username",
                    height="2.8em",
                    bg=Color.WHITE.value,
                    radius="full",
                    required=True,
                    width="100%",
                ),

                rx.text("Gmail"),
                rx.input(placeholder=" ex: jane.doe@domain.com.",
                    name="gmail",
                    height="2.8em",
                    bg=Color.WHITE.value,
                    radius="full",
                    width="100%",
                ),
                rx.flex(
                    rx.vstack(
                        rx.text("Password *"),
                        rx.input(placeholder=" ex: 7Rq;lwwj@CV2_sy",
                            name="password",
                            value=TextfieldControlled.password,
                            height="2.8em",
                            type=PasswordInput.state,
                            required=True,
                            bg=Color.WHITE.value,
                            radius="full",
                            width="20em",
                            on_change=TextfieldControlled.set_password
                        ),

                        rx.text("Confirm Password *"),
                        rx.input(placeholder=" ex: 7Rq;lwwj@CV2_sy",
                            #name="password",
                            value=TextfieldControlled.password,
                            height="2.8em",
                            type=PasswordInput.state,
                            required=True,
                            bg=Color.WHITE.value,
                            radius="full",
                            width="20em",
                            on_change=TextfieldControlled.set_password
                        ),
                    ),
                    rx.flex(
                        rx.button(rx.icon("eye", size=15),
                                radius="full",
                                margin_top="3em",
                                background_color=Color.PURPLE.value,
                                on_click=PasswordInput.change_state),
                        
                        rx.button("Generate",
                                radius="full",
                                margin_top="3em",
                                background_color=Color.PURPLE.value,
                                on_click=TextfieldControlled.generate_password),
                        spacing="1",
                    ),
                    spacing="2"
                ),

                rx.flex(
                    rx.alert_dialog.action(
                        rx.button("Add",
                            radius="full",
                            background_color=Color.PURPLE.value,
                            type="submit",
                            #=rx.redirect("../../user/courses/1")
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
                on_submit=FormInputState.handle_submit,
                reset_on_submit=True,
                #margin_left="4.5em",
                width="100%"
            ),

            background_color=Color.LILAC2.value,
            width="30em"
        ),
        
    )


def sidebar_button2(tab: str, icon: str, url: str) -> rx.Component:
    return rx.button(
        rx.icon(icon, size=15),
        tab,
        on_click=rx.redirect(url),
        _hover={"background_color": Color.GRAY.value},
        background_color=Color.LILAC.value,
        color=Color.BLACK.value,
        padding_y= "0.5em",
        border_radius="3em",
        width="15em"
    )