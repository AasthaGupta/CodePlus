CREATE TABLE IF NOT EXISTS `writes` (
  `q_code` varchar(35) NOT NULL,
  `username` varchar(35) NOT NULL,
  PRIMARY KEY (`q_code`),
  KEY `fk9` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



INSERT INTO `writes` (`q_code`, `username`) VALUES
('Q4', 'amanj94'),
('Q1', 'ayushj94'),
('Q6', 'ayushj94'),
('Q7', 'gosaindhruv94'),
('Q8', 'jgarvit94'),
('Q2', 'mrinal94'),
('Q3', 'mrinal94'),
('Q5', 'sadul05');

ALTER TABLE `writes`
  ADD CONSTRAINT `fk8` FOREIGN KEY (`q_code`) REFERENCES `question` (`q_code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk9` FOREIGN KEY (`username`) REFERENCES `person` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;
