from utils.pipelines import *
from selenium_folder.selenium_login import *
from utils.retrieve import *

s = SeleniumPipeline()
s.process_item("instagram", "https://instagram.com", '["NAME","username"]', '["NAME","password"]', '["CLASS_NAME","_acan _acap _acas _aj1- _ap30]')
#for i in s.get_item_by_own_id(1):
    #item=i
#print(i)

#try:
    #selenium_login("mariana","lulita",1)
    #selenium_login("mariana","lulita",1)
#except:pass

u = PassManUserPipeline()
w= WebsitePipeline()
#u.process_item("marianac1707m@gmail.com", "573168718747", "1Heladodechocolate*", "82372")

