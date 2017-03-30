CREATE TABLE IF NOT EXISTS `solution_of` (
  `s_id` int(35) NOT NULL,
  `q_code` varchar(35) NOT NULL,
  PRIMARY KEY (`s_id`),
  KEY `fk6` (`q_code`)
) 



INSERT INTO `solution_of` (`s_id`, `q_code`) VALUES
(1, 'Q1'),
(3, 'Q1'),
(4, 'Q1'),
(5, 'Q1'),
(6, 'Q1'),
(8, 'Q3'),
(7, 'Q4'),
(10, 'Q4'),
(9, 'Q6'),
(11, 'Q7');

ALTER TABLE `solution_of`
  ADD CONSTRAINT `fk5` FOREIGN KEY (`s_id`) REFERENCES `solution` (`s_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk6` FOREIGN KEY (`q_code`) REFERENCES `question` (`q_code`) ON DELETE CASCADE ON UPDATE CASCADE;


