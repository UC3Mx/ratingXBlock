

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `DATABASE`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `item_rating`
--

CREATE TABLE IF NOT EXISTS `item_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `youtube_id` varchar(11) COLLATE utf8_bin NOT NULL,
  `user` varchar(254) COLLATE utf8_bin DEFAULT NULL,
  `rating` int(11) NOT NULL,
  `comment` varchar(1024) COLLATE utf8_bin DEFAULT NULL,
  `ip` varchar(20) COLLATE utf8_bin NOT NULL,
  `creation_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=40 ;
