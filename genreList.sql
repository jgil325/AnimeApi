-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: genreList
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `genreList`
--

DROP TABLE IF EXISTS `genreList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genreList` (
  `Anime Name` text DEFAULT NULL,
  `Popularity` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genreList`
--

LOCK TABLES `genreList` WRITE;
/*!40000 ALTER TABLE `genreList` DISABLE KEYS */;
INSERT INTO `genreList` VALUES ('Cowboy Bebop',202706),('Cowboy Bebop: Tengoku no Tobira',39291),('Trigun',69358),('Witch Hunter Robin',10268),('Eyeshield 21',17761),('Initial D Fourth Stage',18978),('Naruto',302557),('One Piece',244518),('Tennis no Ouji-sama',17343),('Ring ni Kakero 1',702),('Sunabouzu',13889),('Texhnolyze',34104),('Trinity Blood',13582),('Zipang',2976),('Shin Seiki Evangelion',192826),('Shin Seiki Evangelion: THE END OF EVANGELION',97844),('Kenpuu Denki Berserk',59534),('Koukaku Kidoutai',69255),('Rurouni Kenshin: Meiji Kenkaku Romantan - Tsuioku-hen',24973),('Rurouni Kenshin: Meiji Kenkaku Romantan',44358);
/*!40000 ALTER TABLE `genreList` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-08 18:51:27
