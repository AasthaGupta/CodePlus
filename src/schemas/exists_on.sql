CREATE TABLE IF NOT EXISTS `exists_on` (
  `q_code` varchar(35) NOT NULL,
  `domain` varchar(35) NOT NULL,
  PRIMARY KEY (`q_code`,`domain`),
  KEY `fk11` (`domain`)
) 


INSERT INTO `exists_on` (`q_code`, `domain`) VALUES
('Q1', 'CODECHEF'),
('Q2', 'CODECHEF'),
('Q7', 'CODECHEF'),
('Q1', 'CODEFORCES'),
('Q2', 'CODEFORCES'),
('Q4', 'CODEFORCES'),
('Q7', 'CODEFORCES'),
('Q2', 'SPOJ'),
('Q3', 'SPOJ'),
('Q6', 'SPOJ'),
('Q7', 'SPOJ'),
('Q2', 'TOPCODER'),
('Q5', 'TOPCODER'),
('Q6', 'TOPCODER'),
('Q7', 'TOPCODER'),
('Q8', 'TOPCODER');

ALTER TABLE `exists_on`
  ADD CONSTRAINT `fk10` FOREIGN KEY (`q_code`) REFERENCES `question` (`q_code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk11` FOREIGN KEY (`domain`) REFERENCES `online_judge` (`domain`) ON DELETE CASCADE ON UPDATE CASCADE;