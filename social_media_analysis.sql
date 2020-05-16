-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2020 at 06:47 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `social_media_analysis`
--

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `id` int(11) NOT NULL,
  `date_posted` datetime NOT NULL,
  `content` text NOT NULL,
  `user_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`id`, `date_posted`, `content`, `user_id`, `post_id`) VALUES
(1, '2020-03-28 14:21:53', 'Ramping up new coworkers can be one of the more time-consuming tasks for everyone on the team. Give the newest members of your team access to everything they need to know by pointing them to your team’s private Stack Overflow community.', 1, 2),
(2, '2020-03-28 14:22:16', 'Shipping new features involves a lot of teamwork and coordination. Forget checklists and long docs no one ever reads. Store your team’s shipping best practices on Stack Overflow.', 1, 2),
(3, '2020-04-20 08:55:40', 'hi sgss', 3, 11),
(4, '2020-04-23 12:40:15', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3, 2),
(5, '2020-04-23 12:49:17', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3, 13),
(6, '2020-04-23 12:55:17', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3, 14),
(7, '2020-04-23 13:39:43', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3, 14);

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `date_posted` datetime NOT NULL,
  `content` text NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`id`, `title`, `date_posted`, `content`, `user_id`) VALUES
(1, 'Question 1', '2020-03-28 14:19:40', 'Unlike office workers, remote employees don’t have the ability to tap their colleagues when they need help. To do remote work well, knowledge should be easily accessible to anyone, wherever they are in the world.', 1),
(2, 'Question 2', '2020-03-28 14:20:15', 'Contractors bring outside expertise into your organization and free up your time, ideally. One of the challenges of working with contractors is making sure they know what they need to know to successfully complete a project without taking up too much of your team’s time.', 1),
(8, 'Question 4', '2020-03-29 10:49:30', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 1),
(9, 'New Question', '2020-03-30 08:49:02', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 1),
(10, 'New Post', '2020-03-30 09:09:02', 'Unlike office workers, remote employees don’t have the ability to tap their colleagues when they need help. To do remote work well, knowledge should be easily accessible to anyone, wherever they are in the world.', 3),
(11, 'Social Analysis', '2020-03-30 09:09:22', 'Unlike office workers, remote employees don’t have the ability to tap their colleagues when they need help. To do remote work well, knowledge should be easily accessible to anyone, wherever they are in the world.', 3),
(12, 'Question 4', '2020-04-23 12:39:12', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3),
(13, 'social', '2020-04-23 12:48:54', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3),
(14, 'Question 6', '2020-04-23 12:54:55', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3),
(15, 'Question 7', '2020-04-23 13:39:21', 'Stack Overflow’s powerful Q&A engine works so well for public and private knowledge-sharing that some of our customers are using it with their customers. Stack Overflow Enterprise allows multiple-team permissions, giving companies the ability to give their clients secure 24/7 access to a knowledge base of answers.', 3);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(120) NOT NULL,
  `image_file` varchar(20) NOT NULL,
  `password` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `image_file`, `password`) VALUES
(1, 'Ashan M Silva', 'ashan.silva.97.aj@gmail.com', 'default.jpg', '$2b$12$35dUgOqxV3y4BkUgH3TteOO4Mm16R/MhPGSV9n2hsIZgis84NbuMu'),
(3, 'Ashan Silva', 'ashansilva.17@cse.mrt.ac.lk', 'de3462525333ca07.jpg', '$2b$12$4Sv8VmqECcP.EGg4tj4p.uPQpHtb3Q/m1mq6t/Vr.y3PafJzj./Ji');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `post_id` (`post_id`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`);

--
-- Constraints for table `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
