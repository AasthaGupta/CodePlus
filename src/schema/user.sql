CREATE TABLE IF NOT EXISTS user
(
	email TEXT NOT NULL,
	username TEXT NOT NULL,
	password VARCHAR(32) NOT NULL,
	fname VARCHAR(25) NOT NULL,
	lname VARCHAR(25) NOT NULL,
	country VARCHAR(25) NOT NULL,
	dob DATE NOT NULL,
	PRIMARY KEY (email,username)
);
