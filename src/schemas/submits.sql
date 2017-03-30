CREATE TABLE IF NOT EXISTS `submits` (
  `s_id` int(35) NOT NULL,
  `username` varchar(35) NOT NULL,
  PRIMARY KEY (`s_id`),
  KEY `fk4` (`username`)
)

INSERT INTO `submits` (`s_id`, `username`) VALUES
(3, 'amanj94'),
(10, 'amanj94'),
(6, 'ayushj94'),
(7, 'ayushj94'),
(8, 'ayushj94'),
(1, 'gosaindhruv94'),
(9, 'gosaindhruv94'),
(11, 'jgarvit94'),
(5, 'mrinal94'),
(4, 'sadul05');

ALTER TABLE `submits`
  ADD CONSTRAINT `fk3` FOREIGN KEY (`s_id`) REFERENCES `solution` (`s_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk4` FOREIGN KEY (`username`) REFERENCES `person` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;


