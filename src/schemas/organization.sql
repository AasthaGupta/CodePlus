CREATE TABLE IF NOT EXISTS `organisation` (
  `o_id` int(35) NOT NULL AUTO_INCREMENT,
  `o_name` varchar(35) NOT NULL,
  `type` varchar(35) NOT NULL,
  `o_city` varchar(35) NOT NULL,
  `o_country` varchar(35) NOT NULL,
  PRIMARY KEY (`o_id`)
)



INSERT INTO `organisation` (`o_id`, `o_name`, `type`, `o_city`, `o_country`) VALUES
(13, 'SAMSUNG', 'COMPANY', 'BANGALORE', 'INDIA'),
(14, 'GOOGLE', 'COMPANY', 'SANFRANCISCO', 'USA'),
(15, 'NSIT', 'INSTITUITION', 'DELHI', 'INDIA');