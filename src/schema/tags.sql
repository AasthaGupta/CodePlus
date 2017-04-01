CREATE TABLE IF NOT EXISTS tags
(
	q_code TEXT NOT NULL,
	tag TEXT NOT NULL,
	PRIMARY KEY (q_code,tag),
	FOREIGN KEY (q_code) REFERENCES question (q_code) ON DELETE CASCADE ON UPDATE CASCADE
);

