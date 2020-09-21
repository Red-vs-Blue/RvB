CREATE DATABASE RVB;

USE RVB;

CREATE TABLE area( 
    name VARCHAR (100) PRIMARY KEY,
    text VARCHAR (200)
)

CREATE TABLE accounts(
	username VARCHAR (20) PRIMARY KEY NOT NULL,
	email VARCHAR(50) NOT NULL,
	party INT NOT NULL,
	password VARCHAR(25) NOT NULL,
	creation_date SMALLDATETIME NOT NULL,
	privileges INT NOT NULL,
  	FOREIGN KEY(party) REFERENCES affiliation (id),
  	FOREIGN KEY(privileges) REFERENCES privileges (id)
)

CREATE TABLE links(
    id INT IDENTITY PRIMARY KEY,
    link VARCHAR
);

CREATE TABLE affiliation(
    id INT IDENTITY,
    affiliation VARCHAR
)

CREATE TABLE privilege(
    id INT PRIMARY KEY IDENTITY,
    privilege VARCHAR 
)

CREATE TABLE pages(
    id INT PRIMARY KEY IDENTITY,
    title VARCHAR (15) NOT NULL,
    area_name VARCHAR(100) NOT NULL,
  	FOREIGN KEY(area_name) REFERENCES area (name)
)

CREATE TABLE posts(
    id INT PRIMARY KEY IDENTITY,
    username VARCHAR (20) NOT NULL,
    affiliation INT NOT NULL,
    post_text VARCHAR,
    time_and_date SMALLDATETIME,
    votes INT,
    area VARCHAR (100),
    page VARCHAR (15),
    post_title VARCHAR(500) NOT NULL,
    FOREIGN KEY (page) REFERENCES page (name),
    FOREIGN KEY (area) REFERENCES area (name),
    FOREIGN KEY (affiliation) REFERENCES affiliation (id),
    FOREIGN KEY (username) REFERENCES accounts (username)
)

CREATE TABLE thread_comments(
    id INT PRIMARY KEY IDENTITY,
    post_id INT NOT NULL,
    username VARCHAR (20),
    text VARCHAR(8000),
    date SMALLDATETIME,
    FOREIGN KEY(post_id) REFERENCES posts (id),
    FOREIGN KEY(username) REFERENCES accounts (username)
)

CREATE TABLE contact_us(
    id INT PRIMARY KEY IDENTITY,
    email VARCHAR (150) NOT NULL,
    post VARCHAR(1000),
    name VARCHAR(150),
    date SMALLDATETIME
);

INSERT INTO privilege (privilege)
VALUES  ('reg_user'),
        ('moderator'),
        ('archmoderator'),
        ('admin');


INSERT INTO affiliation (affiliation)
VALUES  ('republican'),
        ('democrat'),
        ('libertarian'),
        ('green'),
        ('constitution');

INSERT INTO area (name, description)
VALUES  ('National'),
        ('The page for all national politics.');

INSERT INTO area (name, description)
VALUES  ('Colorado'),
        ('The place for all Colorado issues or politicians.');

INSERT INTO pages (title, area)
VALUES  ('Abortion'),
        ('National');

INSERT INTO accounts (username, email, party, password, creation_date, privileges)
VALUES  ('dan_the_repub'),
        ('republican@gmail.com'),
        ('1'),
        ('password'),
        ('2020-09-14'),
        ('1');

INSERT INTO accounts (username, email, party, password, creation_date, privileges)
VALUES  ('kendra_the_demo'),
        ('democratsRus@gmail.com'),
        ('2'),
        ('password'),
        ('2020-09-13'),
        ('1');

INSERT INTO posts (username, affiliation, post_text, time_and_date, votes, post_title)
VALUES  ('dan_the_repub'),
        ('1'),
        ('Republicans rule!!'),
        ('2020-09-15 12:43:10'),
        ('20'),
        ('What I think about Republicans, a statement');

INSERT INTO posts (username, affiliation, post_text, time_and_date, votes, post_title)
VALUES  ('kendra_the_demo'),
        ('2'),
        ('Go go go go Democrats!!'),
        ('2020-09-13 11:42:05'),
        ('25'),
        ('Democrats are the best! Everyone else stinks!');