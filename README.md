# MDWebsite
## Description

MDWebsite is a personal website for Max Debin (DrMaxD) created to advertise myself


## Summary

MDWebsite is a website designed to advertise myself (Max Debin) and demonstrate by web development abilities. This project was inspired by multiple friends who have all created and recomended creating a personal website. This project was created with HTML, CSS, and Python to run a website using FLASK. The website is connected to a postgres database which will allow a user to enter their contact information as well as a message within a contact me page. The information would be stored within a database where I would look at the information and respond as soon as possible. Additionally, users will be able to see my resume which has been created using TEX, other projects I have worked on, and an about me section where I will talk about myself more.


## Project Setup
### Virtual Environment
1. install virtualenv virtual environment
    ```bash
    pip install virtualenv
    # or
    python3 -m pip install virtualenv
    ```
2. create a virtual environment
    ```bash
    # create venv
    virtualenv .venv
    # or 
    python3 -m virtualenv .venv
   ```

2. activate the virtual environment
    ```bash
    pip install virtualenv
    # or
    python3 -m pip install virtualenv
    ```
4. install the project dependencies
     ```bash
    pip install -r requirements.txt
    # or
    python3 -m pip install -r requirements.txt
    ```

### Postgresql Database
1. install postgres version 16.4: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

2. create a database

3. create a .env file in the project root

4. add the following values to the .env file
    ```bash
    db_name = <db name>
    db_owner = postgres
    db_pass = <db pass>
    ```
    
## Sources

Project Template - CMPT221L Software Development 2 https://github.com/profphip/cmpt221


Website Background - freepik.com
https://shorturl.at/7qz0Q


TEX Resume Template - Overleaf.com
https://www.overleaf.com/




