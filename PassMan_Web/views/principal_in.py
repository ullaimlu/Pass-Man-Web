import reflex as rx
from PassMan_Web.components import *
#from database.pipelines import CoursePipeline

content=[["Facebook","ullaimlu","ullaimlu@gmail.com","*******","/websites/facebook.png","https://facebook.com"],["Instagram","ullaimlu","ullaimlu@gmail.com","******","/websites/instagram.png","https://instagram.com"]]
class WebsState(rx.State):
    websites: list[list[str]]= content



def principal_in(tab: str,content=WebsState.websites) -> rx.Component:
    #content= courses(content)
    content=websites(content)
    return rx.hstack(
        sidebar(),
        rx.vstack(
            my_space_tittle(tab),
            my_space(tab, content),
            width="100%"
        )
    )
    
    
        