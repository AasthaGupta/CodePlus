CREATE TABLE IF NOT EXISTS `member_of` (
  `username` varchar(35) NOT NULL,
  `o_id` int(35) NOT NULL,
  PRIMARY KEY (`username`),
  KEY `fk2` (`o_id`)
) 



INSERT INTO `member_of` (`username`, `o_id`) VALUES
('ayushj94', 13),
('gosaindhruv94', 13),
('mrinal94', 13),
('amanj94', 14),
('jgarvit94', 14),
('sadul05', 15);

ALTER TABLE `member_of`
  ADD CONSTRAINT `fk1` FOREIGN KEY (`username`) REFERENCES `person` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk2` FOREIGN KEY (`o_id`) REFERENCES `organisation` (`o_id`) ON DELETE CASCADE ON UPDATE CASCADE;