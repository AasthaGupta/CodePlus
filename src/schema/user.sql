CREATE TABLE IF NOT EXISTS user
(
	email TEXT NOT NULL,
	username TEXT NOT NULL,
	password varchar(25) NOT NULL,
	fname varchar(25) NOT NULL,
	lname varchar(25) NOT NULL,
	country varchar(25) NOT NULL,
	dob date NOT NULL,
	PRIMARY KEY (email,username)
);
