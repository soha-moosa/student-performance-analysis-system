-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2017 at 11:22 PM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 7.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spas`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `a_pass` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `a_pass`) VALUES
(1, 'Rehan', 'perfect'),
(2, 'Soha', 'clay'),
(3, 'Sami', 'hannah');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` int(5) NOT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `credit_hours` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id`, `code`, `name`, `credit_hours`) VALUES
(1, 'CT-153', 'Programming Languages', 4),
(2, 'CT-174', 'Fundamentals of Information Technology', 4),
(3, 'MT-171', 'Differential and Integral Calculus', 3),
(4, 'EL-134', 'Basic Electronics', 4),
(5, 'HS-205', 'Islamic Studies', 3),
(6, 'HS-209', 'Ethical Behaviour(For Non-Muslims)', 3),
(7, 'CT-157', 'Data Structures Algorithms and Applications', 4),
(8, 'CT-162', 'Discrete Structures', 3),
(9, 'CT-251', 'Object Oriented Programming', 4),
(10, 'HS-104', 'Functional English', 3),
(11, 'HS-105', 'Pakistan Studies', 3),
(12, 'HS-127', 'Pakistan Studies(For Foriegners)', 3),
(13, 'CS-251', 'Login Design & Switching Theory', 4),
(14, 'CT-352', 'Computer Graphics', 4),
(15, 'CT-258', 'Financial & Cost Accounting', 3),
(16, 'CT-259', 'System Analysis and Design', 3),
(17, 'MT-273', 'Differential Equations and Linear Algebra', 3),
(18, 'CS-252', 'Computer Architecture and Organization', 4),
(19, 'CS-257', 'Data Base Management System', 3),
(20, 'CT-362', 'Web Engineering', 4),
(21, 'HS-208', 'Business Communications & Ethics', 3),
(22, 'MT-331', 'Probability & Statics', 3),
(23, 'CT-360', 'Visual Programming', 4),
(24, 'CS-353', 'Microprocessors and their Applications', 4),
(25, 'CT-363', 'Operating Systems', 4),
(26, 'CT-462', 'Distributed Computing', 4),
(27, 'CS-351', 'Computer Communication Networks', 4),
(28, 'CT-365', 'Software Engineering', 3),
(29, 'CT-364', 'Theory of Automated and Formated Languages', 3),
(30, 'CT-361', 'Artificial Intelligence & Expert systems', 4),
(31, 'CT-366', 'E-Commerce', 3),
(32, 'CT-460', 'Network and Information Security', 4),
(33, 'CT-464', 'Modeling and Simulations', 3),
(34, 'CT-463', 'Data Warehousing & Mining', 4),
(35, 'CT-442', 'Numerical Methods', 3),
(36, 'CT-499', 'Software Based Project', 3),
(37, 'HS-403', 'Enterpreneurships', 3),
(38, 'CT-451', 'Parallel Processing', 4),
(39, 'CT-465', 'Compiler Design', 3),
(40, 'CT-499', 'Software Based Project', 3),
(41, 'CT-481', 'Wireless Networks & Mobile Computing', 4),
(42, 'CT-482', 'Bio-Informatics', 4),
(43, 'CT-483', 'System Administration', 4);

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `id` int(5) NOT NULL,
  `teacher_id` int(5) NOT NULL,
  `course_id` int(5) NOT NULL,
  `student_id` int(5) NOT NULL,
  `class_per` int(5) DEFAULT NULL,
  `class_test` int(5) DEFAULT NULL,
  `mid_term` int(5) NOT NULL,
  `lab_test` int(5) DEFAULT NULL,
  `project` int(5) DEFAULT NULL,
  `attendance` int(5) NOT NULL,
  `ts_marks` int(5) NOT NULL,
  `tf_marks` int(5) NOT NULL,
  `ps_marks` int(5) DEFAULT NULL,
  `pf_marks` int(5) DEFAULT NULL,
  `t_marks` int(5) NOT NULL,
  `percentage` int(11) NOT NULL,
  `GPA` float NOT NULL,
  `semester` int(5) NOT NULL,
  `year` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`id`, `teacher_id`, `course_id`, `student_id`, `class_per`, `class_test`, `mid_term`, `lab_test`, `project`, `attendance`, `ts_marks`, `tf_marks`, `ps_marks`, `pf_marks`, `t_marks`, `percentage`, `GPA`, `semester`, `year`) VALUES
(1, 11, 1, 1, 3, 5, 18, 14, 6, 79, 35, 49, 2, 17, 129, 86, 4, 1, 1),
(2, 6, 2, 1, 3, 16, 17, 14, NULL, 78, 32, 39, 20, 19, 146, 97, 4, 1, 1),
(3, 16, 4, 1, 2, 7, 13, 15, 20, 80, 33, 37, 13, 15, 140, 93, 4, 1, 1),
(4, 10, 3, 1, 3, 7, 19, NULL, NULL, 89, 34, 49, NULL, NULL, 112, 112, 4, 1, 1),
(5, 18, 5, 1, 4, 7, 18, NULL, NULL, 90, 34, 32, NULL, NULL, 97, 97, 4, 1, 1),
(6, 1, 9, 1, 5, 7, 12, 17, 18, 89, 36, 40, 15, 17, 150, 100, 4, 2, 1),
(7, 2, 8, 1, 3, 7, 14, NULL, NULL, 90, 35, 42, NULL, NULL, 101, 101, 4, 2, 1),
(8, 8, 7, 1, 3, 6, 15, 16, NULL, 90, 38, 30, 19, 16, 110, 73, 3, 2, 1),
(9, 14, 11, 1, 2, 8, 15, NULL, NULL, 97, 32, 31, NULL, NULL, 88, 88, 4, 2, 1),
(10, 17, 10, 1, 5, 10, 15, NULL, NULL, 89, 40, 32, NULL, NULL, 92, 92, 4, 2, 1),
(11, 13, 18, 2, 2, 7, 12, 16, NULL, 89, 29, 37, 24, 10, 137, 91, 4, 1, 2),
(12, 6, 19, 2, 2, 8, 18, 7, NULL, 80, 35, 51, 25, 16, 155, 103, 4, 1, 2),
(13, 1, 20, 2, 3, 8, 16, 12, 18, 97, 32, 42, 11, 14, 153, 102, 4, 1, 2),
(14, 8, 21, 2, 2, 13, 14, NULL, NULL, 89, 29, 43, NULL, NULL, 101, 101, 4, 1, 2),
(15, 2, 22, 2, 2, 9, 13, NULL, NULL, 78, 24, 32, NULL, NULL, 80, 80, 3.4, 1, 2),
(16, 3, 13, 3, NULL, 7, 13, 12, NULL, 90, 32, 35, NULL, 12, 111, 74, 3, 2, 2),
(17, 2, 14, 3, 1, 8, 5, 12, NULL, 89, 31, 43, 18, 5, 123, 82, 3.7, 2, 2),
(18, 14, 15, 3, NULL, 7, 14, NULL, NULL, 78, 29, 39, NULL, NULL, 89, 89, 4, 2, 2),
(19, 7, 16, 3, 2, 12, 17, NULL, NULL, 98, 31, 48, NULL, NULL, 79, 79, 3.4, 2, 2),
(20, 2, 17, 3, 3, 12, 14, NULL, NULL, 89, 29, 41, NULL, NULL, 70, 70, 2.7, 2, 2),
(21, 11, 23, 4, 2, 10, 13, 5, 7, 79, 37, 45, 17, 5, 104, 69, 2.7, 1, 3),
(22, 9, 24, 4, 4, 12, 15, 7, NULL, 90, 38, 43, 5, 5, 101, 67, 2.4, 1, 3),
(23, 6, 25, 4, 3, 4, 12, 13, NULL, 93, 32, 43, 17, 8, 91, 61, 2, 1, 3),
(24, 4, 26, 4, 3, 7, 7, 16, NULL, 82, 33, 45, 13, 7, 98, 65, 2.4, 1, 3),
(25, 7, 27, 5, 2, 6, 7, 18, NULL, 91, 33, 47, 18, 5, 103, 69, 2.7, 2, 3),
(26, 13, 28, 5, 2, 8, 17, 9, NULL, 89, 37, 42, 18, 7, 104, 69, 2.7, 2, 3),
(27, 2, 29, 5, 5, 8, 18, NULL, NULL, 79, 31, 54, NULL, NULL, 85, 85, 3.7, 2, 3),
(28, 2, 30, 5, 2, 6, 13, 14, NULL, 79, 36, 45, 10, 10, 101, 67, 2.4, 2, 3),
(29, 4, 31, 5, 3, 12, 18, NULL, NULL, 89, 33, 54, NULL, NULL, 87, 87, 4, 2, 3),
(30, 7, 32, 15, 2, 6, 12, 18, NULL, 94, 38, 47, 8, 8, 101, 67, 2.4, 1, 4),
(31, 9, 33, 15, 5, 15, 19, NULL, NULL, 83, 39, 48, NULL, NULL, 87, 87, 4, 1, 4),
(32, 10, 34, 15, 1, 8, 14, 14, NULL, 78, 37, 51, 10, 10, 108, 72, 3, 1, 4),
(33, 8, 35, 15, 10, 10, 19, NULL, NULL, 91, 39, 49, NULL, 0, 89, 59, 1.7, 1, 4),
(34, 12, 40, 15, NULL, NULL, 0, NULL, 80, 0, 0, 0, NULL, NULL, 80, 80, 3.4, 1, 4),
(35, 13, 38, 13, 1, 7, 16, 14, NULL, 96, 38, 54, 15, 5, 112, 75, 3, 2, 4),
(36, 5, 39, 13, 5, 13, 18, NULL, NULL, 83, 36, 51, NULL, NULL, 87, 87, 4, 2, 4),
(37, 13, 40, 13, NULL, NULL, 0, NULL, 90, 0, 0, 0, NULL, NULL, 170, 170, 4, 2, 4),
(38, 4, 37, 13, 3, 12, 16, NULL, NULL, 89, 31, 45, NULL, NULL, 76, 76, 3.4, 2, 4),
(39, 16, 41, 13, 2, 8, 12, 7, NULL, 97, 29, 42, 15, 10, 96, 64, 2, 2, 4),
(40, 11, 1, 2, 3, 0, 17, 10, 5, 89, 37, 46, 24, 8, 115, 77, 3.4, 1, 1),
(42, 3, 2, 2, 5, 15, 12, 6, NULL, 87, 38, 52, 10, 10, 110, 73, 3, 1, 1),
(43, 3, 3, 2, 5, 16, 16, NULL, NULL, 89, 37, 54, 0, 0, 91, 61, 2, 1, 1),
(44, 5, 5, 2, 5, 10, 18, NULL, NULL, 98, 33, 43, NULL, NULL, 76, 76, 3.4, 1, 1),
(45, 6, 6, 2, 5, 14, 17, NULL, NULL, 87, 36, 50, NULL, NULL, 86, 86, 4, 2, 1),
(46, 10, 7, 2, 4, 8, 12, 7, NULL, 97, 34, 42, 10, NULL, 86, 86, 4, 2, 1),
(47, 2, 8, 2, 5, 14, 13, NULL, NULL, 79, 32, 45, NULL, NULL, 77, 77, 3.4, 2, 1),
(48, 1, 9, 2, 4, NULL, 15, 15, 5, 87, 39, 45, NULL, NULL, 84, 84, 3.7, 2, 1),
(49, 17, 10, 2, NULL, 16, 18, NULL, NULL, 91, 34, 45, NULL, NULL, 79, 79, 3.4, 2, 1),
(50, 18, 11, 2, 5, 15, 17, NULL, NULL, 84, 37, 36, 0, NULL, 76, 76, 3.4, 2, 1),
(51, 11, 1, 3, 4, 7, 15, 6, 7, 93, 39, 45, 0, NULL, 84, 84, 3.7, 1, 1),
(52, 6, 2, 3, 5, 10, 15, 4, NULL, 0, 39, 50, NULL, NULL, 89, 89, 4, 1, 1),
(53, 13, 3, 3, 5, 8, 18, NULL, NULL, 82, 31, 54, NULL, NULL, 85, 85, 3.7, 1, 1),
(54, 18, 4, 3, 5, 15, 10, 10, 10, 85, 40, 50, NULL, NULL, 100, 100, 4, 1, 1),
(55, 3, 5, 3, 6, 10, 15, NULL, NULL, 78, 30, 38, NULL, NULL, 68, 68, 2.7, 1, 1),
(56, 6, 7, 3, 5, 10, 10, 8, NULL, 87, 33, 54, NULL, NULL, 87, 87, 4, 2, 1),
(57, 2, 8, 3, 7, 10, 12, NULL, NULL, 0, 29, 38, NULL, NULL, 67, 67, 2.4, 2, 1),
(58, 1, 9, 3, 5, NULL, 15, 8, 8, 80, 36, 40, 10, 10, 96, 64, 2, 2, 1),
(59, 17, 10, 3, 5, 15, 20, NULL, NULL, 99, 40, 52, NULL, NULL, 92, 92, 4, 2, 1),
(60, 18, 11, 3, 2, 14, 18, NULL, NULL, 0, 32, 40, NULL, NULL, 72, 72, 3, 2, 1),
(61, 10, 18, 3, 5, 8, 8, 10, NULL, 93, 31, 40, NULL, NULL, 71, 71, 3, 2, 2),
(62, 4, 19, 3, 5, 15, 0, 18, NULL, 98, 38, 40, NULL, NULL, 78, 78, 3.4, 2, 2),
(63, 1, 20, 3, 2, 8, 12, 8, 7, 98, 37, 52, NULL, NULL, 89, 89, 4, 2, 2),
(64, 17, 21, 3, 5, 12, 19, NULL, NULL, 87, 37, 40, NULL, NULL, 77, 77, 3.4, 2, 2),
(65, 18, 22, 3, 5, 15, 20, NULL, NULL, 90, 40, 51, NULL, NULL, 91, 91, 4, 2, 2),
(66, 11, 1, 4, 5, 5, 15, 5, 7, 89, 37, 50, 10, NULL, 97, 97, 4, 1, 1),
(67, 6, 2, 4, 5, 14, 10, 15, NULL, 0, 40, 50, NULL, NULL, 90, 90, 4, 1, 1),
(68, 18, 3, 4, 5, 16, 19, NULL, NULL, 0, 40, 50, NULL, NULL, 90, 90, 4, 1, 1),
(69, 10, 4, 4, 4, 12, 12, 5, NULL, 87, 33, 40, NULL, NULL, 73, 73, 3, 1, 1),
(70, 3, 5, 4, 5, 15, 12, NULL, NULL, 85, 32, 40, NULL, NULL, 72, 72, 3, 1, 0),
(71, 6, 7, 4, 2, 8, 15, 12, NULL, 80, 37, 50, NULL, NULL, 87, 87, 4, 2, 1),
(72, 2, 8, 4, 5, 10, 20, NULL, NULL, 35, 35, 50, NULL, NULL, 85, 85, 3.7, 2, 1),
(73, 1, 9, 4, 5, 10, 10, 5, 7, 98, 37, 54, NULL, NULL, 91, 91, 4, 2, 1),
(74, 17, 10, 4, 5, 14, 10, 0, NULL, 79, 32, 38, NULL, NULL, 70, 70, 2.7, 2, 1),
(75, 18, 11, 4, 2, 8, 20, NULL, NULL, 88, 30, 40, NULL, NULL, 70, 70, 2.7, 2, 1),
(76, 7, 13, 4, 5, 10, 12, 10, NULL, 90, 37, 50, NULL, NULL, 87, 87, 4, 1, 2),
(77, 9, 14, 4, 5, 8, 12, 5, NULL, 99, 30, 48, 10, 10, 98, 65, 2.4, 2, 1),
(78, 6, 15, 4, 5, 14, 14, NULL, NULL, 77, 33, 44, NULL, NULL, 77, 77, 3.4, 2, 1),
(79, 4, 16, 4, 10, 15, 12, 0, NULL, 99, 33, 44, NULL, NULL, 77, 77, 3.4, 2, 2),
(80, 5, 17, 4, 10, 15, 12, NULL, NULL, 88, 37, 50, NULL, NULL, 87, 87, 4, 2, 2),
(81, 10, 18, 4, 5, 8, 12, 5, NULL, 77, 38, 40, 10, NULL, 88, 88, 4, 2, 2),
(82, 6, 19, 4, 5, 10, 10, 0, NULL, 0, 35, 50, 10, NULL, 95, 95, 4, 2, 2),
(83, 1, 20, 4, 4, 5, 15, 10, 6, 99, 40, 51, NULL, NULL, 91, 91, 4, 2, 2),
(84, 12, 21, 4, 5, 10, 15, NULL, NULL, 87, 35, 40, NULL, NULL, 75, 75, 3, 2, 2),
(85, 13, 22, 4, 5, 15, 18, NULL, NULL, 89, 38, 40, NULL, NULL, 88, 88, 4, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `roll_no` varchar(50) NOT NULL,
  `enrollment_no` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `roll_no`, `enrollment_no`) VALUES
(1, 'Hassan', 'CT-001', 'NED/1655/1617'),
(2, 'Tahreem', 'CT-002', 'NED/1755/1617'),
(3, 'Neha', 'CT-003', 'NED/1855/1617'),
(4, 'Tooba', 'CT-004', 'NED/1955/1617'),
(5, 'Aisha', 'CT-005', 'NED/1652/1516'),
(6, 'Shahzaib', 'CT-006', 'NED/1653/1516'),
(7, 'Haiqa', 'CT-007', 'NED/1654/1516'),
(8, 'Ather', 'CT-008', 'NED/1655/1516'),
(9, 'Anusha', 'CT-009', 'NED/1621/1415'),
(10, 'Alqama', 'CT-010', 'NED/1631/1415'),
(11, 'Ayesha', 'CT-011', 'NED/1641/1415'),
(12, 'Iqra', 'CT-012', 'NED/1651/1415'),
(13, 'Hamna', 'CT-013', 'NED/1361/1314'),
(14, 'Waleed', 'CT-014', 'NED/1461/1314'),
(15, 'Musfira', 'CT-015', 'NED/1561/1314'),
(16, 'Fahad', 'CT-016', 'NED/1661/1314');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `id` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `t_pass` varchar(50) NOT NULL,
  `designation` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`id`, `name`, `t_pass`, `designation`) VALUES
(1, 'Muhammad Mubashir Khan', 'CSSE', 'Associate Professor'),
(2, 'Najeed Ahmed Khan', 'CSSE', 'Associate Professor'),
(3, 'Muhammad Wahabuddin Usmani', 'CSSE', 'Associate Professor'),
(4, 'Najmi Ghani Haider', 'CSSE', 'Professor'),
(5, 'Sohail Abdul Sattar', 'CSSE', 'Professor'),
(6, 'Saba Izhar Haque', 'CSSE', 'Assistant Professor'),
(7, 'Saman Hina', 'CSSE', 'Assistant Professor'),
(8, 'Shariq Mahmood Khan', 'CSSE', 'Assistant Professor'),
(9, 'Shehnila Zardari', 'CSSE', 'Assistant Professor'),
(10, 'Raheela Asif', 'CSSE', 'Assistant Professor'),
(11, 'Waseemullah', 'CSSE', 'Lecturer'),
(12, 'Umer Farooq', 'CSSE', 'Lecturer'),
(13, 'Kashif Mehboob Khan', 'CSSE', 'Lecturer'),
(14, 'Uzma Zehra', 'CSSE', 'Lecturer'),
(15, 'Uzma Zehra', 'CSSE', 'Lecturer'),
(16, 'Maria Andaleeb Siddiqui', 'CSSE', 'Lecturer'),
(17, 'Muhammd Ali', 'CSSE', 'Assistant Professor '),
(18, 'Ahmed Khakani', 'CSSE', 'Professor ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_2` (`id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_2` (`id`);

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_2` (`id`),
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_2` (`id`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_2` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
--
-- AUTO_INCREMENT for table `record`
--
ALTER TABLE `record`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;
--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `record`
--
ALTER TABLE `record`
  ADD CONSTRAINT `record_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`),
  ADD CONSTRAINT `record_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`),
  ADD CONSTRAINT `record_ibfk_3` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
