from getpass import getpass
from logging import Logger
import os

from wrapper.Session import Session
from wrapper.Beautifulsoup import BeautifulSoup
from log.logging_config import setup_logging

def login(s: Session, username: str, password: str):
    login_url = "https://moodle.itismajo.it/login/index.php"
    resp = s.get("https://moodle.itismajo.it/")
    resp = s.get(login_url)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    token = soup.select_one("[name=logintoken]").get("value")
    
    body = {
        "anchor": "",
        "logintoken": token,
        "username": username,
        "password": password
    }
    
    resp = s.post(login_url, data=body)
    resp = s.get("https://moodle.itismajo.it/my/", allow_redirects=True)
    
    if resp.history:
        return { "username": username, "password": password, "status": 400 }
    
    return { "username": username, "password": password, "status": resp.status_code }

def main(logger: Logger):
    logger.info("")
    with Session() as s:
        logger.info("Type your username: ")
        username = input()
        logger.info("Type your password: ")
        passwd = getpass("")
        credentials = login(s, username, passwd)
        
        if credentials['status'] != 200:
            logger.error(f"Login failed with username: {credentials['username']} and password: {len(credentials['password']) * '*'}")
            return
        
        logger.debug(f"Logged Succesfully")
        
        logger.info("Type the name of the project (ex. Bike): ")
        project_name = input()
        
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\DB')
        
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)
        
        file = s.get("https://moodle.itismajo.it/pluginfile.php/184684/mod_folder/content/0/attach%20database.txt?forcedownload=1")
        open(os.path.join(desktop_path, 'attach_db.txt'), 'wb').write(file.content)
        
        file = s.get("https://moodle.itismajo.it/pluginfile.php/184684/mod_folder/content/0/dbBikeStores.ldf?forcedownload=1")
        open(os.path.join(desktop_path, f'db{project_name}Stores.ldf'), 'wb').write(file.content)
        
        file = s.get("https://moodle.itismajo.it/pluginfile.php/184684/mod_folder/content/0/dbBikeStores.mdf?forcedownload=1")
        open(os.path.join(desktop_path, f'db{project_name}Stores.mdf'), 'wb').write(file.content)
            
        
if __name__ == '__main__':
    
    logger = setup_logging()
    
    main(logger)