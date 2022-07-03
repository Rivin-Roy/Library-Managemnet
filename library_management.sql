-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2022 at 08:02 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` int(11) NOT NULL,
  `language_id` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL,
  `bname` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `qty` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `language_id`, `genre_id`, `bname`, `author`, `image`, `description`, `qty`, `status`) VALUES
(5, 1, 5, 'Naruto', 'Masashi Kishimoto', 'static/images8d21864c-acd8-4240-8daf-6e12ef1bf8afnaruto.jpg', 'Naruto is a young shinobi with an incorrigible knack for mischief. He’s got a wild sense of humor, but Naruto is completely serious about his mission to be the world’s greatest ninja!', '5', 'active'),
(6, 1, 4, 'Little Women', 'Louisa May Alcott', 'static/images/1f4f230c-8956-49da-ae5d-7467858b78eeLITTLE WOMEN.jpg', 'Little Women was an immediate commercial and critical success, with readers eager for more about the characters.', '3', 'active'),
(7, 1, 4, 'Anne of Green Gables', 'L. M. Montgomery', 'static/images/180ba3e1-b765-4273-b618-f1fbc2e8bb30ANNE OF GREEN GABLE.jfif', 'The novel recounts the adventures of Anne Shirley, an 11-year-old orphan girl, who is sent by mistake to two middle-aged siblings, Matthew and Marilla Cuthbert, who had originally intended to adopt a boy to help them on their farm in the fictional town of Avonlea in Prince Edward Island, Canada.', '5', 'active'),
(8, 1, 5, 'Alice Adventures in Wonderland', 'Lewis Carroll', 'static/images/02379bdb-2887-4f32-8992-5651ce19bbb3ALICE IN WONDERLAND.jpg', 'It is an 1865 English novel by Lewis Carroll. A young girl named Alice falls through a rabbit hole into a fantasy world of anthropomorphic creatures. It is seen as an example of the literary nonsense genre.', '8', 'active'),
(9, 4, 5, 'AZADI: Freedom. Fascism. Fiction', 'Arundhati Roy', 'static/images/45d114a3-9d39-47e1-8b8c-a39e18b866dfAZADI(HINDI).jpg', 'The chant of Azadi!--Urdu for \"Freedom!\"--is the slogan of the freedom struggle in Kasmir against what Kasmirris see as the Indian Occupation. Ironically it has also become the chant of millions on the streets of India against the project of Hindu Nationalism. What lies between these two calls for Freedom? A chasm or a bridge?', '5', 'active'),
(10, 3, 6, 'Chemmeen', 'Thakazhi Sivasankara Pillai', 'static/images/385baf4a-5e1c-465e-be34-36073e6acbe5chemmeen.jpg', ' Chemmeen tells the story of the relationship between Karuthamma, the daughter of a Hindu fisherman, and Pareekutti, the son of a Muslim fish wholesaler. The theme of the novel is a myth among the fishermen communities along the coastal Kerala State in the Southern India.', '6', 'active'),
(11, 4, 6, 'Half Girlfriend', 'Chetan Bhagat', 'static/images/6d52a07a-0fc7-4629-ae1f-94d3dd5519d6half girlfriend (hindi).jpg', 'The novel, set in rural Bihar, New Delhi, Patna, and New York, is the story of a Bihari boy in quest of winning over the girl he loves.', '4', 'active'),
(12, 1, 7, 'Heidi', 'Johanna Spyri', 'static/images/af088021-eaed-4911-af88-6928dc1e4f98HEIDI.webp', 'It is a novel about the events in the life of a 5-year-old girl in her paternal grandfather care in the Swiss Alps. It was written as a book \"for children and those who love children\"', '2', 'active'),
(13, 3, 8, 'Khasakkinte Itihasam', 'O. V. Vijayan', 'static/images/370e2561-5efa-44fd-b7d8-537c502522a5KHASAKINTE ITHIHASAM.jpg', 'The novel tells the story of a young university student, who leaves a promising future to take up a primary school teacher’s job in the remote village of Khasak. Little by little, the village reveals its secrets.', '6', 'active'),
(14, 3, 6, 'Mathilukal', 'Vaikom Muhammad Basheer', 'static/images/a44d5c08-2ebf-493b-ae5f-97f2fd6b9126mathilukal.jpg', 'Its hero, Basheer himself, and heroine, Narayani, never meet, yet they love each other passionately. Despite being imprisoned and separated by a huge wall that divides their prisons, the two romance each other.', '8', 'active'),
(15, 4, 5, 'One Indian girl Novel ', 'Chetan Bhagat', 'static/images/160a085f-4ece-4fc0-9ecd-99c683169c08One-indian-girl ( HINDI).jpg', ' The book is about a girl name Radhika Mehta, who is a worker at the Distressed Debt group of Goldman Sachs, the investment bank.', '9', 'active'),
(16, 3, 8, 'Aadujeevitham', 'Benyamin', 'static/images/531a48c7-ae7d-4bf1-a4d8-4678c84f8963aadujeevitham.jpg', 'The novel about an abused migrant worker in Saudi Arabia written by Bahrain-based Indian author Benyamin (born Benny Daniel).', '4', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `house` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `username`, `first_name`, `last_name`, `phone`, `email`, `house`, `district`, `pincode`) VALUES
(1, 'anna@gmail.com', 'anna', 'rose', '7034589624', 'joyelroy24@gmail.com', 'kalarikkal', 'ernakulam', '682508'),
(2, 'aleena@gmail.com', 'Aleena', 'tree', '9630011203', 'aleena@gmail.com', 'kalarikkal', 'Ernakulam', '682007'),
(3, 'feena@gmail.com', 'feena', 'andrews', '9874563210', 'feena@gmail.com', 'valappill', 'kollam', '677889'),
(4, 'feena@gmail.com', 'RITHI', 'GEORGE', '7356702122', 'feena@gmail.com', 'sdf', 'we', '682019'),
(6, 'rithigeo@gmail.com', 'RITHI', 'GEORGE', '7356702122', 'rithigeo@gmail.com', 'wert', '123456', '682019'),
(7, 'egdevika4@gmail.com', 'devika', 'eg', '7025789318', 'egdevika4@gmail.com', 'ellakattu', 'Thriussur', '682019'),
(8, 'reethugeorge19@gmail.com', 'REETHU', 'GEORGE', '6282222386', 'reethugeorge19@gmail.com', 'KOODARAPILLY HOUSE', 'ERNAKULAM', '682019'),
(9, 'rithi@gmail.com', 'RITHI', 'GEORGE', '7356702122', 'rithi@gmail.com', 'qwerty', 'wertyu', '682019');

-- --------------------------------------------------------

--
-- Table structure for table `fine`
--

CREATE TABLE `fine` (
  `fine_id` int(11) NOT NULL,
  `fcategory_id` int(11) DEFAULT NULL,
  `rmaster_id` int(11) DEFAULT NULL,
  `fine_amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fine`
--

INSERT INTO `fine` (`fine_id`, `fcategory_id`, `rmaster_id`, `fine_amount`, `status`) VALUES
(1, 2, 1, '100', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `fine_category`
--

CREATE TABLE `fine_category` (
  `fcategory_id` int(11) NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `fine_amount` varchar(100) DEFAULT NULL,
  `month` varchar(100) DEFAULT NULL,
  `fcstatus` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fine_category`
--

INSERT INTO `fine_category` (`fcategory_id`, `category`, `fine_amount`, `month`, `fcstatus`) VALUES
(4, 'p', '15', '1', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE `genre` (
  `genre_id` int(11) NOT NULL,
  `genre_name` varchar(100) DEFAULT NULL,
  `gstatus` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`genre_id`, `genre_name`, `gstatus`) VALUES
(1, 'drama', 'active'),
(4, 'Bildungsroman', 'active'),
(5, 'Fiction', 'active'),
(6, 'Romance', 'active'),
(7, 'Childrens Fiction', 'active'),
(8, 'Novel', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `language`
--

CREATE TABLE `language` (
  `language_id` int(11) NOT NULL,
  `language` varchar(100) DEFAULT NULL,
  `lstatus` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `language`
--

INSERT INTO `language` (`language_id`, `language`, `lstatus`) VALUES
(1, 'English', 'active'),
(3, 'Malayalam', 'active'),
(4, 'hindi', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `user_type`) VALUES
('admin', 'admin', 'admin'),
('aleena@gmail.com', 'aleena', 'user'),
('anna@gmail.com', 'ann', 'user'),
('joyelroy24@gmail.com', 'aaa', 'staff'),
('xubujo@mailinator.com', 'Pa$$w0rd!', 'staff'),
('feena@gmail.com', 'feena', 'user'),
('feena@gmail.com', '11111111', 'user'),
('rithigeorg@gmail.com', '1111111111111', 'user'),
('rithigeo@gmail.com', '111111111111', 'user'),
('egdevika4@gmail.com', 'devika@123', 'user'),
('reethugeorge19@gmail.com', '123EERTH', 'user'),
('rithi@gmail.com', '12345678', 'user'),
('rani@gmail.com', '12345678', 'staff'),
('rithigeorge01@gmail.com', '12345678', 'staff');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `rmaster_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `rmaster_id`, `amount`, `date`) VALUES
(2, 1, '100', '2022-02-09'),
(3, 6, '5', '2022-03-08'),
(4, 6, '5', '2022-03-08'),
(5, 6, '10', '2022-03-21'),
(6, 11, '20', '2022-05-11');

-- --------------------------------------------------------

--
-- Table structure for table `plan`
--

CREATE TABLE `plan` (
  `plan_id` int(11) NOT NULL,
  `plan` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `pl_status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `plan`
--

INSERT INTO `plan` (`plan_id`, `plan`, `amount`, `pl_status`) VALUES
(1, '3', '500', 'active'),
(2, '6', '1000', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `publisher_id` int(11) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `pstatus` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`publisher_id`, `email`, `publisher`, `phone`, `city`, `district`, `pincode`, `pstatus`) VALUES
(2, 'penquin134@gmail.com', 'Penquin Publishers', '9897867865', 'Delhi', 'Sarojini Nagar', '110007', 'active'),
(3, 'WestlandPublications@gmail.com', 'Westland Publications', '9898989897', 'Tamil Nadu', 'Chennai', '600001', 'active'),
(4, 'RupaPublications@gmail.com', 'Rupa Publications', '9090989796', 'Kochi', 'Ernakulam', '682019', 'active'),
(5, 'Rolibooks@gmail.com', 'Roli Books', '8789878980', 'Chruch street', 'Bangalore', '560001', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `purchase_child`
--

CREATE TABLE `purchase_child` (
  `pchild_id` int(11) NOT NULL,
  `pmaster_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `purchase_child`
--

INSERT INTO `purchase_child` (`pchild_id`, `pmaster_id`, `book_id`, `amount`, `quantity`) VALUES
(1, 3, 1, '100', '1'),
(2, 4, 3, '1000', '2'),
(3, 5, 3, '1000', '3'),
(4, 6, 1, '100', '10'),
(5, 7, 1, '300', '5'),
(6, 8, 5, '500', '3'),
(7, 9, 5, '500', '4'),
(8, 10, 6, '450', '5'),
(9, 11, 7, '450', '5'),
(10, 12, 6, '500', '3'),
(11, 13, 7, '399', '5'),
(12, 14, 5, '280', '5'),
(13, 15, 8, '499', '8'),
(14, 16, 9, '450', '5'),
(15, 17, 10, '650', '6'),
(16, 18, 11, '250', '4'),
(17, 19, 12, '600', '2'),
(18, 20, 13, '350', '6'),
(19, 21, 14, '500', '8'),
(20, 22, 15, '499', '9'),
(21, 23, 16, '599', '4');

-- --------------------------------------------------------

--
-- Table structure for table `purchase_master`
--

CREATE TABLE `purchase_master` (
  `pmaster_id` int(11) NOT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `pur_date` varchar(100) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `purchase_master`
--

INSERT INTO `purchase_master` (`pmaster_id`, `publisher_id`, `staff_id`, `pur_date`, `total_amount`) VALUES
(1, 1, 1, '2022-02-17', '100'),
(2, 1, 1, '2022-11-09', '100'),
(3, 1, 1, '2022-12-09', '100'),
(4, 1, 1, '2022-02-28', '2000'),
(5, 1, 1, '2022-02-23', '3000'),
(6, 1, 1, '2022-03-08', '1000'),
(7, 1, 1, '2022-05-11', '1500'),
(8, 1, 1, '2022-05-11', '1500'),
(9, 2, 0, '2022-05-16', '2000'),
(12, 2, 0, '2022-05-16', '1500'),
(13, 3, 0, '2022-05-16', '1995'),
(14, 4, 0, '2022-05-16', '1400'),
(15, 4, 0, '2022-05-16', '3992'),
(16, 4, 0, '2022-05-16', '2250'),
(17, 2, 0, '2022-05-16', '3900'),
(18, 2, 0, '2022-05-16', '1000'),
(19, 2, 0, '2022-05-16', '1200'),
(20, 2, 0, '2022-05-16', '2100'),
(21, 2, 0, '2022-05-16', '4000'),
(22, 3, 0, '2022-05-16', '4491'),
(23, 3, 3, '2022-05-16', '2396');

-- --------------------------------------------------------

--
-- Table structure for table `rent_child`
--

CREATE TABLE `rent_child` (
  `rchild_id` int(11) NOT NULL,
  `rmaster_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rent_child`
--

INSERT INTO `rent_child` (`rchild_id`, `rmaster_id`, `book_id`) VALUES
(10, 11, 5),
(11, 12, 5),
(12, 13, 5),
(13, 14, 5),
(14, 15, 5),
(15, 16, 7),
(16, 17, 7),
(17, 18, 8),
(18, 19, 6),
(19, 20, 7),
(20, 21, 8);

-- --------------------------------------------------------

--
-- Table structure for table `rent_master`
--

CREATE TABLE `rent_master` (
  `rmaster_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `rdate` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rent_master`
--

INSERT INTO `rent_master` (`rmaster_id`, `customer_id`, `rdate`, `date`, `status`) VALUES
(6, 1, '12/07/2021', '2021-10-07', 'not picked'),
(7, 1, '', '2022-01-07', 'pending'),
(10, 1, '', '2022-01-08', 'pending'),
(11, 7, '04/09/2022', '2022-05-11', 'paid'),
(12, 8, '', '2022-05-16', 'cancel'),
(13, 8, '', '2022-05-16', 'reject'),
(14, 8, '06/16/2022', '2022-05-16', 'confirm'),
(15, 8, '', '2022-05-16', 'not picked'),
(16, 9, '06/16/2022', '2022-05-16', 'confirm'),
(17, 9, '', '2022-05-16', 'reject'),
(18, 9, '', '2022-05-16', 'reject'),
(19, 9, '', '2022-05-16', 'pending'),
(20, 9, '', '2022-05-16', 'pending'),
(21, 9, '', '2022-05-16', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `house` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `ststatus` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `username`, `firstname`, `lastname`, `place`, `dob`, `phone`, `email`, `house`, `city`, `district`, `pincode`, `ststatus`) VALUES
(1, 'joyelroy24@gmail.com', 'Anupamaa', 'kumar', 'kochin', '1998-02-13', '9530011201', 'joyelroy24@gmail.com', 'jxnjx', 'kochi', 'Ernakulamm', '6289971', 'active'),
(3, 'rani@gmail.com', 'RANI', 'GEORGE', 'Edakochi', '1970-04-12', '7356702122', 'rani@gmail.com', 'Chettikalam', 'Ernakulam', 'Kochi', '682020', 'active'),
(4, 'rithigeorge01@gmail.com', 'RITHI', 'GEORGE', 'Edakochi', '2022-05-03', '7356702122', 'rithigeorge01@gmail.com', 'www', 'Ernakulam', 'ERNAKULAM', '682019', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `subscription`
--

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  `fromdate` varchar(100) DEFAULT NULL,
  `todate` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subscription`
--

INSERT INTO `subscription` (`subscription_id`, `customer_id`, `plan_id`, `fromdate`, `todate`) VALUES
(2, 1, 1, '2022-04-18', '07/18/2022'),
(3, 2, 1, '2022-04-18', '07/18/2022'),
(4, 3, 1, '2022-05-11', '11/08/2022'),
(5, 7, 1, '2022-05-11', '11/08/2022'),
(6, 8, 1, '2022-05-16', '16/08/2022'),
(7, 9, 2, '2022-05-16', '16/11/2022');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `fine`
--
ALTER TABLE `fine`
  ADD PRIMARY KEY (`fine_id`);

--
-- Indexes for table `fine_category`
--
ALTER TABLE `fine_category`
  ADD PRIMARY KEY (`fcategory_id`);

--
-- Indexes for table `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`genre_id`);

--
-- Indexes for table `language`
--
ALTER TABLE `language`
  ADD PRIMARY KEY (`language_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `plan`
--
ALTER TABLE `plan`
  ADD PRIMARY KEY (`plan_id`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`publisher_id`);

--
-- Indexes for table `purchase_child`
--
ALTER TABLE `purchase_child`
  ADD PRIMARY KEY (`pchild_id`);

--
-- Indexes for table `purchase_master`
--
ALTER TABLE `purchase_master`
  ADD PRIMARY KEY (`pmaster_id`);

--
-- Indexes for table `rent_child`
--
ALTER TABLE `rent_child`
  ADD PRIMARY KEY (`rchild_id`);

--
-- Indexes for table `rent_master`
--
ALTER TABLE `rent_master`
  ADD PRIMARY KEY (`rmaster_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `subscription`
--
ALTER TABLE `subscription`
  ADD PRIMARY KEY (`subscription_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `fine`
--
ALTER TABLE `fine`
  MODIFY `fine_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `fine_category`
--
ALTER TABLE `fine_category`
  MODIFY `fcategory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `genre`
--
ALTER TABLE `genre`
  MODIFY `genre_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `language`
--
ALTER TABLE `language`
  MODIFY `language_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `plan`
--
ALTER TABLE `plan`
  MODIFY `plan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `publisher`
--
ALTER TABLE `publisher`
  MODIFY `publisher_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `purchase_child`
--
ALTER TABLE `purchase_child`
  MODIFY `pchild_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `purchase_master`
--
ALTER TABLE `purchase_master`
  MODIFY `pmaster_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `rent_child`
--
ALTER TABLE `rent_child`
  MODIFY `rchild_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `rent_master`
--
ALTER TABLE `rent_master`
  MODIFY `rmaster_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `subscription`
--
ALTER TABLE `subscription`
  MODIFY `subscription_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
