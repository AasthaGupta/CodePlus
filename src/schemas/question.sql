CREATE TABLE IF NOT EXISTS `question` (
  `q_code` varchar(35) NOT NULL,
  `difficulty` varchar(35) NOT NULL,
  PRIMARY KEY (`q_code`)
) 



INSERT INTO `question` (`q_code`, `difficulty`) VALUES
('Q1', 'EASY'),
('Q2', 'EXPERT'),
('Q3', 'HARD'),
('Q4', 'MEDIUM'),
('Q5', 'EXPERT'),
('Q6', 'HARD'),
('Q7', 'EXPERT'),
('Q8', 'EXPERT');