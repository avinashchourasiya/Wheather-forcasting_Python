-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2019 at 09:10 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wheather_prediction`
--

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`username`, `passwd`, `email`, `contact`) VALUES
('avinash', 'avi9833', 'avinashchourasiya88@gmail.com', '7678091344'),
('avinashtes', '64467', 'avinashchourasiya88@gmail.com', '7678091333'),
('avinashcho', '88454', 'wdwedwd', 'wedwdwdwed'),
('efwfw', '28413', 'efwfwef', 'wfewfwef'),
('dsdfsdfs', '62976', 'fsdfsfs', 'fsdfsdfsf'),
('dsdfsdfs', '30889', 'avinashchourasiya88@gmail.com', 'fsdfsdfsf'),
('dsdfsdfs', '84523', 'avinashchourasiya88@gmail.com', 'fsdfsdfsf'),
('avinash', 'delta', 'avinashchourasiya88@gmail.com', '7367347832');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
