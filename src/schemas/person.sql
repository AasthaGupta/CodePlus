CREATE TABLE IF NOT EXISTS person (
  username TEXT PRIMARY KEY NOT NULL,
  password varchar(25) NOT NULL,
  p_fname varchar(25) NOT NULL,
  p_lname varchar(25) NOT NULL,
  country varchar(25) NOT NULL,
  dob date NOT NULL,
 );
