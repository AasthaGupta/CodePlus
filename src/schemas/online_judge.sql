CREATE TABLE IF NOT EXISTS `online_judge` (
  `domain` varchar(35) NOT NULL,
  PRIMARY KEY (`domain`)
) 

INSERT INTO `online_judge` (`domain`) VALUES
('CODECHEF'),
('CODEFORCES'),
('SPOJ'),
('TOPCODER');