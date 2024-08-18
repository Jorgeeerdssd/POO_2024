-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2024 a las 01:50:53
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `frutimax`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categories`
--

CREATE TABLE `categories` (
  `idCategory` int(11) NOT NULL,
  `name` tinytext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categories`
--

INSERT INTO `categories` (`idCategory`, `name`) VALUES
(1, 'Fruta'),
(2, 'Verdura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clients`
--

CREATE TABLE `clients` (
  `idClient` int(11) NOT NULL,
  `name` tinytext DEFAULT NULL,
  `lastname` tinytext DEFAULT NULL,
  `rfc` varchar(13) NOT NULL,
  `phone` tinytext DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(60) NOT NULL,
  `postalcode` varchar(20) DEFAULT NULL,
  `country` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clients`
--

INSERT INTO `clients` (`idClient`, `name`, `lastname`, `rfc`, `phone`, `email`, `password`, `address`, `city`, `state`, `postalcode`, `country`) VALUES
(10001, 'Pedro', 'Gutierrez', 'GUMP991229KJ2', '618-334-2970', 'pedroguttierez@email.com', '5c39a20951f564d316aa816d3011a1d2c305d5306f7677bc14b9c1efef02a7b1', 'Constitucion SN', 'Canatlan', 'Durango', '34465', 'Mexico'),
(10000, 'Juan', 'Perez', 'PEGJ900701CN1', '618-200-1200', 'juanperez@email.com', 'jupe12', '8 de Julio', 'Durango', 'Durango', '34165', 'Mexico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `details_ticket`
--

CREATE TABLE `details_ticket` (
  `id` int(11) NOT NULL,
  `details_code` int(11) NOT NULL,
  `idTicket` int(11) NOT NULL,
  `idProduct` int(11) NOT NULL,
  `idOrder` int(11) NOT NULL,
  `quantity_product` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `details_ticket`
--

INSERT INTO `details_ticket` (`id`, `details_code`, `idTicket`, `idProduct`, `idOrder`, `quantity_product`) VALUES
(6, 30001, 20000, 100, 40002, 50),
(7, 30001, 20000, 101, 40002, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `employee`
--

CREATE TABLE `employee` (
  `idEmployee` int(11) NOT NULL,
  `name` tinytext DEFAULT NULL,
  `lastname` tinytext DEFAULT NULL,
  `rfc` varchar(13) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `address` varchar(60) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(60) NOT NULL,
  `postalcode` varchar(20) NOT NULL,
  `country` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `employee`
--

INSERT INTO `employee` (`idEmployee`, `name`, `lastname`, `rfc`, `email`, `password`, `phone`, `address`, `city`, `state`, `postalcode`, `country`) VALUES
(0, 'ADMIN', NULL, '', 'admin@frutimax.com', 'admin', NULL, '', '', '', '', ''),
(70000, 'Humberto', 'Martinez', 'MADH991203KL0', 'humar@gmail.com', '1e0960a966c51ffc365bb815fffa84806040cb080a4ebb3f7c27c6b7d60cc2ee', '644-200-1200', 'VI Vicentenario', 'Durango', 'Durango', '34115', 'Mexico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orders`
--

CREATE TABLE `orders` (
  `code_order` int(11) NOT NULL,
  `idOrder` int(11) NOT NULL,
  `idClient` int(11) NOT NULL,
  `idDetails` int(11) NOT NULL,
  `status` varchar(60) NOT NULL,
  `date_delivery` date NOT NULL,
  `date_order` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `orders`
--

INSERT INTO `orders` (`code_order`, `idOrder`, `idClient`, `idDetails`, `status`, `date_delivery`, `date_order`) VALUES
(40001, 1, 10000, 30001, 'PENDING', '0000-00-00', '2024-08-02'),
(40002, 2, 10001, 30002, 'Delivered', '2024-08-07', '2025-08-06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `idProduct` int(11) NOT NULL,
  `idCategory` int(11) DEFAULT NULL,
  `idSupplier` int(11) DEFAULT NULL,
  `name_product` tinytext DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` decimal(11,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`idProduct`, `idCategory`, `idSupplier`, `name_product`, `quantity`, `price`) VALUES
(100, 1, 60000, 'Manzana', 2000, 20.00),
(101, 2, 60000, 'Lechuga', 100, 10.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `supplier`
--

CREATE TABLE `supplier` (
  `idSupplier` int(11) NOT NULL,
  `name` tinytext DEFAULT NULL,
  `lastname` tinytext DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `rfc` varchar(13) NOT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `address` varchar(60) DEFAULT NULL,
  `city` varchar(60) DEFAULT NULL,
  `state` varchar(60) NOT NULL,
  `postalcode` varchar(60) DEFAULT NULL,
  `country` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `supplier`
--

INSERT INTO `supplier` (`idSupplier`, `name`, `lastname`, `company`, `rfc`, `phone`, `email`, `address`, `city`, `state`, `postalcode`, `country`) VALUES
(60000, 'Gerardo', 'Ontiveros', 'FrutotasDGO', 'FTD990110k7a', '6771135160', 'frutotas@email.com', 'Benito', 'Durango', 'Durango', '34160', 'Mexico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ticket`
--

CREATE TABLE `ticket` (
  `idTicket` int(11) NOT NULL,
  `details_code` int(11) NOT NULL,
  `rfc_client` varchar(13) DEFAULT NULL,
  `idOrder` int(11) NOT NULL,
  `idEmployee` int(11) NOT NULL,
  `total_quantity` int(11) NOT NULL,
  `pursache_date` date NOT NULL,
  `pursache_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ticket`
--

INSERT INTO `ticket` (`idTicket`, `details_code`, `rfc_client`, `idOrder`, `idEmployee`, `total_quantity`, `pursache_date`, `pursache_time`) VALUES
(20000, 30001, 'PEGJ900701CN1', 1, 70000, 1000, '2024-08-01', '20:59:00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`idCategory`);

--
-- Indices de la tabla `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`rfc`),
  ADD UNIQUE KEY `idClient` (`idClient`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `details_ticket`
--
ALTER TABLE `details_ticket`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idProducto` (`idProduct`),
  ADD KEY `idOrder` (`idOrder`),
  ADD KEY `idTicket` (`idTicket`),
  ADD KEY `details_code` (`details_code`);

--
-- Indices de la tabla `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`idEmployee`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`code_order`),
  ADD KEY `idDetails` (`idDetails`),
  ADD KEY `idClient` (`idClient`),
  ADD KEY `idOrder` (`idOrder`);

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`idProduct`),
  ADD KEY `idCategory` (`idCategory`),
  ADD KEY `idSupplier` (`idSupplier`);

--
-- Indices de la tabla `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`idSupplier`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`idTicket`),
  ADD KEY `idEmployee` (`idEmployee`),
  ADD KEY `idDetails` (`details_code`),
  ADD KEY `rfc` (`rfc_client`),
  ADD KEY `details_code` (`details_code`),
  ADD KEY `idOrder` (`idOrder`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categories`
--
ALTER TABLE `categories`
  MODIFY `idCategory` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `details_ticket`
--
ALTER TABLE `details_ticket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `supplier`
--
ALTER TABLE `supplier`
  MODIFY `idSupplier` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60002;

--
-- AUTO_INCREMENT de la tabla `ticket`
--
ALTER TABLE `ticket`
  MODIFY `idTicket` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20001;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `details_ticket`
--
ALTER TABLE `details_ticket`
  ADD CONSTRAINT `details_ticket_ibfk_1` FOREIGN KEY (`idProduct`) REFERENCES `products` (`idProduct`),
  ADD CONSTRAINT `details_ticket_ibfk_3` FOREIGN KEY (`idOrder`) REFERENCES `orders` (`code_order`),
  ADD CONSTRAINT `details_ticket_ibfk_4` FOREIGN KEY (`details_code`) REFERENCES `ticket` (`details_code`);

--
-- Filtros para la tabla `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`idClient`) REFERENCES `clients` (`idClient`);

--
-- Filtros para la tabla `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`idCategory`) REFERENCES `categories` (`idCategory`),
  ADD CONSTRAINT `products_ibfk_2` FOREIGN KEY (`idSupplier`) REFERENCES `supplier` (`idSupplier`);

--
-- Filtros para la tabla `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`idEmployee`) REFERENCES `employee` (`idEmployee`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`rfc_client`) REFERENCES `clients` (`rfc`),
  ADD CONSTRAINT `ticket_ibfk_4` FOREIGN KEY (`idOrder`) REFERENCES `orders` (`idOrder`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
