from rxconfig import config
import PassMan_Web.styles.styles as styles
from PassMan_Web.views.principal_in import *
from PassMan_Web.views.login import *
from PassMan_Web.views.sign_up import *
from utils.pipelines import *
from utils.retrieve import *
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"



class State(rx.State):
    principal_content: list[list[str]]=[]
    @rx.var
    def post_id(self)->list[list[str]]:       
        content=[]
        w= WebsitePipeline()
        tab=self.router.page.params.get("pid", "...")
        
        try:
            mp=u.get_mp_by_id(int(tab))
            ds=u.get_ds_by_id(int(tab))
            for i in w.get_item_by_id(int(tab)):
                pswd= retrieve(mp,ds, i[3])
                content.append([i[1],i[2],pswd,i[5],f"/websites/{i[1].lower()}.png"])
        except:pass
        return content 

#def index() -> rx.Component:
    # return principal_in("My Websites")

def index() -> rx.Component:
    return login()

@rx.page(route="websites/[pid]")
def post():
    return principal_in("My Websites", State.post_id)

@rx.page(route="sign-up")
def post():
    """A page that updates based on the route."""
    return sign_up()

app = rx.App(
    stylesheets= styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(index)
app.compile()

