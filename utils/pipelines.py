from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from utils.dbconfig import *


class PassManUserPipeline(object):
    def __init__(self):
        self.engine = db_connect()
        create_table(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_item(self):
        session = self.Session()
        passman_user = select(PassManUser)
        result = session.execute(passman_user).all()
        session.close()
        return result
    
    def get_pass_by_username(self, username):
        get_sel = select(PassManUser).where(PassManUser.username==username)
        with self.engine.connect() as conn:
            result = conn.execute(get_sel)
            for i in result:
                return i[3]
            
    def get_id_by_username(self, username):
        get_sel = select(PassManUser).where(PassManUser.username==username)
        with self.engine.connect() as conn:
            result = conn.execute(get_sel)
            for i in result:
                return i[0]
            
    def get_mp_by_id(self, userid):
        get_sel = select(PassManUser).where(PassManUser.id==userid)
        with self.engine.connect() as conn:
            result = conn.execute(get_sel)
            for i in result:
                return i[3]
            
    def get_ds_by_id(self, userid):
        get_sel = select(PassManUser).where(PassManUser.id==userid)
        with self.engine.connect() as conn:
            result = conn.execute(get_sel)
            for i in result:
                return i[4]
            
    def get_phone_by_username(self, username):
        get_sel = select(PassManUser).where(PassManUser.username==username)
        with self.engine.connect() as conn:
            result = conn.execute(get_sel)
            for i in result:
                return i[2]

    def process_item(self,username,phone,master_password,device_secret):
        session = self.Session()
        passman_user = PassManUser()
        passman_user.username= username
        passman_user.phone= phone
        passman_user.masterkey_hash = master_password
        passman_user.device_secret = device_secret

        try:
            session.add(passman_user)
            session.commit()

        except: 
            session.rollback()
            raise

        finally:
            session.close()

class SeleniumPipeline(object):
    def __init__(self):
        self.engine = db_connect()
        create_table(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_item(self):
        session = self.Session()
        selenium = select(Selenium)
        result = session.execute(selenium).all()
        session.close()
        return result
    
    def get_id_by_name(self, sitename):
        get_sel = select(Selenium).where(Selenium.sitename==sitename.lower())
        with self.engine.connect() as conn:
            result = conn.execute(get_sel)
            for i in result:
                return i[0]
        
    def get_item_by_own_id(self, selenium_id):
        get_sel = select(Selenium).where(Selenium.id==selenium_id)
        with self.engine.connect() as conn:
            result = conn.execute(get_sel)
            for i in result:
                print(i)
                return i

    def process_item(self,sitename, url, username_id, password_id, button_id):
        session = self.Session()
        selenium = Selenium()
        selenium.sitename= sitename
        selenium.url = url
        selenium.username_id = username_id
        selenium.password_id = password_id
        selenium.button_id = button_id

        try:
            session.add(selenium)
            session.commit()

        except: 
            session.rollback()
            raise

        finally:
            session.close()

class WebsitePipeline(object):
    def __init__(self):
        self.engine = db_connect()
        create_table(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_item(self, search):
        session = self.Session()
        website = select(Website).where(Website.siteurl == search)
        result = session.execute(website).all()
        session.close()
        return result
    
    def get_item_by_id(self, id_user):
        get_webs = select(Website).where(Website.user_id==id_user)
        with self.engine.connect() as conn:
            result = conn.execute(get_webs)
            return result

    def process_item(self, sitename, username, password, user_id, selenium_id):
        session = self.Session()
        website = Website()
        act_user = session.query(PassManUser).get(user_id)
        act_selenium = session.query(Selenium).get(selenium_id)
        website.sitename = sitename
        website.username = username
        website.passwd = password
        act_user.websites.append(website)
        act_selenium.websites.append(website)

        try:
            session.add(website)
            session.commit()

        except: 
            session.rollback()
            raise

        finally:
            session.close()