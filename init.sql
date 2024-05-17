CREATE TABLE passman_user(
	id SERIAL primary key unique,
	username VARCHAR(64) NOT null,
    masterkey_hash VARCHAR(255) NOT NULL,
    device_secret VARCHAR(255) NOT NULL
)

CREATE TABLE selenium (
	id SERIAL primary key unique,
    sitename VARCHAR(64) NOT NULL,
    url VARCHAR(64) NOT null,
    username_id VARCHAR(64) NOT null,
    password_id VARCHAR(64) NOT null,
    button_id VARCHAR(64) NOT null
)

CREATE TABLE website (
	id SERIAL primary key unique,
    sitename VARCHAR(64) NOT NULL,
    username VARCHAR(64),
    email VARCHAR(64),   
    passwd VARCHAR(64) NOT null,
    user_id SERIAL REFERENCES passman_user (id),
    selenium_id SERIAL REFERENCES selenium (id)
)