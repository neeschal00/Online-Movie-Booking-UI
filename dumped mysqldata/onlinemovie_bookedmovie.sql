-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: onlinemovie
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookedmovie`
--

DROP TABLE IF EXISTS `bookedmovie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookedmovie` (
  `registrationN` varchar(50) NOT NULL,
  `movie_name` varchar(50) DEFAULT NULL,
  `date_booked` varchar(50) DEFAULT NULL,
  `time_booked` varchar(50) DEFAULT NULL,
  `tickets` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`registrationN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookedmovie`
--

LOCK TABLES `bookedmovie` WRITE;
/*!40000 ALTER TABLE `bookedmovie` DISABLE KEYS */;
INSERT INTO `bookedmovie` VALUES ('20200828200130509220','The Intouchables','Aug/31/2020','15:00-18:30','3','300'),('20200901224018783721','Lion King 2','Sep/04/2020','15:00-18:30','4','400'),('20200901224106258864','The Lives Of Others','Sep/02/2020','11:00-14:30','2','200'),('20200902131403656007','Lion King 2','Sep/05/2020','11:00-14:30','4','400'),('20200902131426266215','The Intouchables','Sep/05/2020','15:00-18:30','3','300'),('20200902132022336912','Oldboy','Sep/05/2020','11:00-14:30','4','400'),('20200902132109331085','Mad Max Fury Road','Sep/05/2020','11:00-14:30','2','200'),('20200902132218270923','Fight Club','Sep/04/2020','07:00-10:30','3','300'),('20200902132303873808','Lion King 2','Sep/03/2020','11:00-14:30','4','400'),('20200902132326419972','Mad Max Fury Road','Sep/04/2020','15:00-18:30','5','500'),('20200902132457478005','Lion King','Sep/05/2020','15:00-18:30','4','400'),('20200904083747470167','Mad Max Fury Road','09/07/2020','15:00-18:30','4','400');
/*!40000 ALTER TABLE `bookedmovie` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-04 23:32:54
