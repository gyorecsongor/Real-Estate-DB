-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2021. Nov 20. 18:44
-- Kiszolgáló verziója: 10.4.21-MariaDB
-- PHP verzió: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `ingatlan`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `ember`
--

CREATE TABLE `ember` (
  `emberID` bigint(20) UNSIGNED NOT NULL,
  `nev` varchar(50) DEFAULT NULL,
  `szuldatum` date DEFAULT NULL,
  `penz` bigint(20) UNSIGNED DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefon` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `ember`
--

INSERT INTO `ember` (`emberID`, `nev`, `szuldatum`, `penz`, `email`, `telefon`) VALUES
(1, 'Feles Elek', '1923-01-29', 3546879543, 'feles@gmail.com', 7141749),
(2, 'Para Zita', '1986-10-20', 13537324, 'para@gmail.com', 4435958),
(3, 'Techno Kolos', '1912-02-14', 8635431, 'tecno@gmail.com', 9190718),
(4, 'Dil Emma', '1918-08-25', 794531237, 'dil@gmail.com', 6084619),
(5, 'Külö Nóra', '1991-03-03', 8753316, 'kulo@gmail.com', 2671146),
(6, 'Git Áron', '1912-07-23', 897342123, 'git@gmail.com', 1195091),
(7, 'Meg Győző', '1935-11-19', 789734, 'meg@gmail.com', 7006868),
(8, 'Kasza Blanka', '1924-10-10', 123456789, 'kasza@gmail.com', 1635329),
(9, 'Wincs Eszter', '1928-12-24', 78975345, 'wincs@gmail.com', 9446649),
(10, 'Bekre Pál', '1919-12-31', 56894347, 'bekre@gmail.com', 9814952),
(11, 'Trap Pista', '2010-06-27', 76342321, 'trap@gmail.com', 7651474),
(12, 'Patkóm Ágnes', '1993-05-17', 785315386, 'patkom@gmail.com', 1397807),
(13, 'Ka Pál', '1993-03-18', 1563864534, 'ka@gmail.com', 8492360),
(14, 'Metall Ica', '1993-10-28', 2368343834, 'metall@gmail.com', 7358514),
(15, 'Lev Elek', '2010-07-20', 7864239, 'lev@gmail.com', 7651474),
(16, 'Teásk Anna', '1993-10-17', 34634535, 'teask@gmail.com', 1397807),
(17, 'Gá Zóra', '1993-03-08', 953154344435, 'ga@gmail.com', 8492360),
(18, 'Ipsz Ilonka', '1993-04-14', 4697643486, 'ipsz@gmail.com', 7358514),
(19, 'Nyúl Kálmán', '1993-12-04', 33546767868, 'nyul@gmail.com', 7358514),
(20, 'Ács Milán', '1993-10-28', 7867623413, 'acs@gmail.com', 2434379),
(21, 'Ba Rika', '2010-07-20', 646876313, 'ba@gmail.com', 3451474),
(22, 'Bánk Bán', '1993-10-17', 786786431, 'bank@gmail.com', 1397807),
(23, 'Bársony Aura', '1993-03-08', 646834343, 'barsony@gmail.com', 6992360),
(24, 'Békés Csaba', '1993-04-14', 4348676434, 'bekes@gmail.com', 4576154),
(25, 'Darabos Milka', '1993-12-04', 338316383, 'darabos@gmail.com', 68958514),
(26, 'Szikla Szilárd', '2011-06-10', 679653154686, 'szikla@gmail.com', 7731341);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `epulet`
--

CREATE TABLE `epulet` (
  `epuletID` bigint(20) UNSIGNED NOT NULL,
  `terulet` bigint(20) UNSIGNED DEFAULT NULL,
  `cim` varchar(50) DEFAULT NULL,
  `epites_eve` date DEFAULT NULL,
  `ar` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `epulet`
--

INSERT INTO `epulet` (`epuletID`, `terulet`, `cim`, `epites_eve`, `ar`) VALUES
(1, 552, 'Rém, Veres Pálné u. 40.', '1923-01-29', 6714149),
(2, 815, 'Ipacsfa, Hegyalja út 535.', '1986-10-20', 4435958),
(3, 480, 'Adony, Erzsébet krt. 448.', '1912-02-14', 49190718),
(4, 220, 'Budapest, Csabai kapu 433.', '1918-08-25', 6082619),
(5, 981, 'Olaszliszka, Bem rkp. 945.', '1991-03-03', 32671496),
(6, 517, 'Sümeg, Rákóczi út 418.', '1912-07-23', 119105091),
(7, 437, 'Nagydobsza, Teréz krt. 640.', '1935-11-19', 17006868),
(8, 670, 'Békés, Veres Pálné u. 625.', '1924-10-10', 16353290),
(9, 571, 'Budapest, Árpád fejedelem útja 852.', '1928-12-24', 94466479),
(10, 123, 'Pácsony, Belgrád rkp. 10.', '1919-12-31', 91466952),
(11, 253, 'Pánd, Síp utca 236.', '2010-06-27', 7651474),
(12, 156, 'Szemely, Piroska u. 658.', '1993-05-17', 137807),
(13, 189, 'Homokterenye, Apáczai Csere János u. 636.', '1993-03-18', 8492360),
(14, 295, 'Gödöllô, Apor Péter u. 236.', '1993-10-28', 73518514),
(15, 153, 'Zajk, Csavargyár u. 232.', '1919-12-31', 54121752),
(16, 879, 'Balinka, Teréz krt. 551.', '2010-06-27', 4351474),
(17, 786, 'Szeged, Fő Fasor 37.', '1993-05-17', 1374567),
(18, 178, 'Szomód, Munkácsy Mihály út 51.', '1993-03-18', 3457360),
(19, 100, 'Makád, Izabella u. 639.', '1993-10-28', 73458514),
(20, 125, 'Komárom, Rákóczi út 626.', '1993-10-28', 456786434),
(21, 468, 'Monoszló, Teréz krt. 625.', '1993-10-28', 43486676),
(22, 135, 'Zalaszentiván, Csavargyár u. 138.', '1993-10-28', 7676438675),
(23, 437, 'Sajtoskál, Victor Hugo u. 720.', '1993-10-28', 468879437),
(24, 673, 'Gyöngyfa, Agip u. 538.', '1993-10-28', 13457343),
(25, 876, 'Szentimrefalva, Kárpát u. 35.', '1993-10-28', 464358676),
(26, 300, 'Nagylók, Erzsébet krt. 345.', '2011-06-10', 1581391);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `epuletkereskedes`
--

CREATE TABLE `epuletkereskedes` (
  `kereskedesID` bigint(20) UNSIGNED NOT NULL,
  `emberID` bigint(20) UNSIGNED DEFAULT NULL,
  `epuletID` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `epuletkereskedes`
--

INSERT INTO `epuletkereskedes` (`kereskedesID`, `emberID`, `epuletID`) VALUES
(1, 2, 1),
(2, 4, 3),
(3, 6, 5),
(4, 8, 7),
(5, 10, 9),
(6, 12, 11),
(7, 14, 13),
(8, 16, 15),
(9, 18, 17),
(10, 20, 19),
(11, 22, 21),
(12, 24, 23),
(13, 26, 25);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `telek`
--

CREATE TABLE `telek` (
  `telekID` bigint(20) UNSIGNED NOT NULL,
  `terulet` bigint(20) UNSIGNED DEFAULT NULL,
  `cim` varchar(50) DEFAULT NULL,
  `ar` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `telek`
--

INSERT INTO `telek` (`telekID`, `terulet`, `cim`, `ar`) VALUES
(1, 552, 'Rém, Veres Pálné u. 40.', 7141549),
(2, 815, 'Ipacsfa, Hegyalja út 535.', 4123458),
(3, 480, 'Adony, Erzsébet krt. 448.', 9190718),
(4, 220, 'Budapest, Csabai kapu 433.', 6082619),
(5, 981, 'Olaszliszka, Bem rkp. 945.', 23544496),
(6, 517, 'Sümeg, Rákóczi út 418.', 11955091),
(7, 437, 'Nagydobsza, Teréz krt. 640.', 7006868),
(8, 670, 'Békés, Veres Pálné u. 625.', 163543290),
(9, 571, 'Budapest, Árpád fejedelem útja 852.', 94443649),
(10, 123, 'Pácsony, Belgrád rkp. 10.', 9149552),
(11, 253, 'Pánd, Síp utca 236.', 7651474),
(12, 156, 'Szemely, Piroska u. 658.', 137833307),
(13, 189, 'Homokterenye, Apáczai Csere János u. 636.', 849231640),
(14, 295, 'Gödöllô, Apor Péter u. 236.', 735158514),
(15, 153, 'Röszke, Csavargyár u. 232.', 32197543),
(16, 879, 'Balinka, Teréz krt. 551.', 4351474),
(17, 999, 'Szeged, Fő Fasor 37.', 137455867),
(18, 178, 'Szomód, Munkácsy Mihály út 51.', 345360),
(19, 100, 'Makád, Izabella u. 639.', 73458514),
(20, 278, 'Komárom, Rákóczi út 626.', 123455676),
(21, 768, 'Monoszló, Teréz krt. 625.', 7857372),
(22, 383, 'Zalaszentiván, Csavargyár u. 138.', 573737),
(23, 973, 'Sajtoskál, Victor Hugo u. 720.', 36467966),
(24, 456, 'Gyöngyfa, Agip u. 538.', 1356723),
(25, 437, 'Szentimrefalva, Kárpát u. 35.', 543547387),
(26, 300, 'Nagylók, Erzsébet krt. 345.', 7754331);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `telekkereskedes`
--

CREATE TABLE `telekkereskedes` (
  `kereskedesID` bigint(20) UNSIGNED NOT NULL,
  `emberID` bigint(20) UNSIGNED DEFAULT NULL,
  `telekID` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `telekkereskedes`
--

INSERT INTO `telekkereskedes` (`kereskedesID`, `emberID`, `telekID`) VALUES
(1, 1, 2),
(2, 3, 4),
(3, 5, 6),
(4, 7, 8),
(5, 9, 10),
(6, 11, 12),
(7, 13, 14),
(8, 15, 16),
(9, 17, 18),
(10, 19, 20),
(11, 21, 22),
(12, 23, 24),
(13, 25, 26);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `ember`
--
ALTER TABLE `ember`
  ADD PRIMARY KEY (`emberID`),
  ADD UNIQUE KEY `emberID` (`emberID`);

--
-- A tábla indexei `epulet`
--
ALTER TABLE `epulet`
  ADD PRIMARY KEY (`epuletID`),
  ADD UNIQUE KEY `epuletID` (`epuletID`);

--
-- A tábla indexei `epuletkereskedes`
--
ALTER TABLE `epuletkereskedes`
  ADD PRIMARY KEY (`kereskedesID`),
  ADD UNIQUE KEY `kereskedesID` (`kereskedesID`),
  ADD KEY `emberID` (`emberID`),
  ADD KEY `epuletID` (`epuletID`);

--
-- A tábla indexei `telek`
--
ALTER TABLE `telek`
  ADD PRIMARY KEY (`telekID`),
  ADD UNIQUE KEY `telekID` (`telekID`);

--
-- A tábla indexei `telekkereskedes`
--
ALTER TABLE `telekkereskedes`
  ADD PRIMARY KEY (`kereskedesID`),
  ADD UNIQUE KEY `kereskedesID` (`kereskedesID`),
  ADD KEY `emberID` (`emberID`),
  ADD KEY `telekID` (`telekID`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `ember`
--
ALTER TABLE `ember`
  MODIFY `emberID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT a táblához `epulet`
--
ALTER TABLE `epulet`
  MODIFY `epuletID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT a táblához `epuletkereskedes`
--
ALTER TABLE `epuletkereskedes`
  MODIFY `kereskedesID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT a táblához `telek`
--
ALTER TABLE `telek`
  MODIFY `telekID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT a táblához `telekkereskedes`
--
ALTER TABLE `telekkereskedes`
  MODIFY `kereskedesID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `epuletkereskedes`
--
ALTER TABLE `epuletkereskedes`
  ADD CONSTRAINT `epuletKereskedes_kk_1` FOREIGN KEY (`emberID`) REFERENCES `ember` (`emberID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `epuletKereskedes_kk_2` FOREIGN KEY (`epuletID`) REFERENCES `epulet` (`epuletID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `telekkereskedes`
--
ALTER TABLE `telekkereskedes`
  ADD CONSTRAINT `telekKereskedes_kk_1` FOREIGN KEY (`emberID`) REFERENCES `ember` (`emberID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `telekKereskedes_kk_2` FOREIGN KEY (`telekID`) REFERENCES `telek` (`telekID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
