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
VALUES  ('National', 'The place for all National political issues.'),
	('Colorado','The place for all Colorado issues or politicians.');

INSERT INTO pages (title, area)
VALUES  ('Abortion','National');

INSERT INTO accounts (username, email, party, password, creation_date, privileges)
VALUES  ('dan_the_repub','republican@gmail.com','1','password','2020-09-14','1'),
('kendra_the_demo','democratsRus@gmail.com','2','password','2020-09-13','1');

INSERT INTO posts (username, affiliation, post_text, time_and_date, votes, page, post_title)
VALUES  ('dan_the_repub','1','Republicans rule!!','2020-09-15 12:43:10','20','1','What I think about Republicans, a statement');

INSERT INTO posts (username, affiliation, post_text, time_and_date, votes, page, post_title)
VALUES  ('kendra_the_demo','2','Go go go go Democrats!!','2020-09-13 11:42:05','25','1','Democrats are the best! Everyone else stinks!');