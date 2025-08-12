-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 13, 2025 at 01:45 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_paleteria`
--
CREATE DATABASE IF NOT EXISTS `bd_paleteria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bd_paleteria`;

-- --------------------------------------------------------

--
-- Table structure for table `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `usuario_id` int(25) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `descripcion` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categoria`
--

INSERT INTO `categoria` (`id`, `usuario_id`, `nombre`, `descripcion`) VALUES
(1, 1, 'paletas de crema', 'paletas con base de crema y algun sabor'),
(2, 1, 'paletas de agua', 'paletas a base de agua de algun sabor'),
(3, 1, 'paletas premium de crema', 'paletas premium con base de crema'),
(4, 2, 'paletas especiales de crema', 'paletas especiales con base de crema'),
(5, 2, 'LO', 'S'),
(6, 2, 'HH', 'OO'),
(7, 1, 'aa', 'aa'),
(13, 8, 'LOLO', 'PP'),
(14, 8, 'SS', 'MAMA<AA'),
(15, 8, 'ARI', 'BELA'),
(16, 8, 'KK', 'LL'),
(17, 8, 'OOO', 'OOO'),
(20, 8, 'SS', 'DD'),
(21, 8, 'DEDE', '45'),
(22, 8, 'SS', '8'),
(23, 8, 'SS', 'SS'),
(24, 9, '', ''),
(25, 9, '', ''),
(26, 9, 'SS', 'SS'),
(27, 9, '', ''),
(28, 9, 'OO', 'PP'),
(30, 9, 'HH', 'HH'),
(32, 10, 'PALETAS DE AGUA', 'PALETAS A BASE DE AGUA'),
(33, 12, 'HH', 'HH'),
(35, 12, 'SS', 'SS'),
(37, 14, 'PALETA DE CREMA', 'PALETA A BASE DE CREMA');

-- --------------------------------------------------------

--
-- Table structure for table `productos`
--

CREATE TABLE `productos` (
  `id` int(25) NOT NULL,
  `usuario_id` int(25) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `cantidad` int(100) NOT NULL,
  `precio` decimal(65,0) NOT NULL,
  `codigo` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `productos`
--

INSERT INTO `productos` (`id`, `usuario_id`, `nombre`, `cantidad`, `precio`, `codigo`) VALUES
(1, 1, 'paleta de fresa', 25, 24, 1),
(2, 1, 'paleta de coco', 987, 29, 1),
(3, 3, 'aa', 41, 26, 2),
(14, 8, 'SSS', 122, 33, 1),
(15, 8, 'FFF', 44, 11, 2),
(16, 8, 'PILATES', 69, 32, 2),
(17, 8, 'LA MIRE', 69, 24, 2),
(18, 8, 'SOPA', 54, 78, 1),
(20, 9, '', 6, 2, 1),
(21, 9, '', 6, 2, 2),
(22, 10, 'PEPEPE', 54, 56, 1),
(24, 12, '', 5, 5, 4),
(26, 14, 'PALETA DE COCO', 30, 29, 1),
(27, 15, 'PALETA DE AGUA', 100, 15, 1);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(25) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `email`, `password`) VALUES
(1, 'samantha ', 'presa', 'michi@gmail.com', '1234'),
(2, 'iran', 'palacios', 'iran@gmail.com', '1234'),
(3, 'JIMIN', 'PARQUE', 'jm@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(4, 'KOKO', 'LELE', 'koko@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(5, '', '', '', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'),
(6, 'LELE', 'PONS', 'lele@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(7, 'LOLO', 'ÑÑ', 'lolo@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(8, 'SI', 'NO', 'si@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(9, 'KEN', 'DRYC', 'ken@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(10, 'SAMY', 'FRESA', 'f@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(11, 'SOPE', 'DE', 'pollo@gmail.com', '1718c24b10aeb8099e3fc44960ab6949ab76a267352459f203ea1036bec382c2'),
(12, 'DKD', 'LKSLS', 'po@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(14, 'MIRANDA', 'REYES HERNÁNDEZ', 'mira@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(15, '', 'CARDIEL', 'emi@gmail.com', 'e73b79a0b10f8cdb6ac7dbe4c0a5e25776e1148784b86cf98f7d6719d472af69');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indexes for table `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `codigo` (`codigo`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `categoria`
--
ALTER TABLE `categoria`
  ADD CONSTRAINT `categoria_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Constraints for table `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`codigo`) REFERENCES `categoria` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
