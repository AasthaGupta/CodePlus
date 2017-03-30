CREATE TABLE IF NOT EXISTS `tags` (
  `q_code` varchar(35) NOT NULL,
  `tag` varchar(35) NOT NULL,
  PRIMARY KEY (`q_code`,`tag`)
)


INSERT INTO `tags` (`q_code`, `tag`) VALUES
('Q1', 'DP'),
('Q1', 'GREEDY'),
('Q2', 'DP'),
('Q2', 'MATHS'),
('Q3', 'IMPLEMENT'),
('Q4', 'DS'),
('Q4', 'GREEDY'),
('Q5', 'DS'),
('Q6', 'MATHS'),
('Q7', 'DP'),
('Q7', 'GREEDY'),
('Q7', 'IMPLEMENT'),
('Q8', 'DP'),
('Q8', 'GREEDY');


ALTER TABLE `tags`
  ADD CONSTRAINT `fk7` FOREIGN KEY (`q_code`) REFERENCES `question` (`q_code`) ON DELETE CASCADE ON UPDATE CASCADE;

