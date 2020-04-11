-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Apr 2020 pada 09.24
-- Versi server: 10.4.8-MariaDB-log
-- Versi PHP: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `log`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `akun`
--

CREATE TABLE `akun` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(25) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `akun`
--

INSERT INTO `akun` (`id`, `username`, `password`, `email`) VALUES
(4, 'ss', 'ss', 'ss@mail.com'),
(5, 'sss', 'sss', 'rizqiakbar281@gmail.');

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_kend`
--

CREATE TABLE `data_kend` (
  `ID` int(11) NOT NULL,
  `JML` int(20) NOT NULL,
  `TGL` date NOT NULL,
  `BLN` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_kend`
--

INSERT INTO `data_kend` (`ID`, `JML`, `TGL`, `BLN`) VALUES
(12534401, 1, '2020-04-11', '04'),
(12534901, 2, '2020-04-11', '04'),
(13445201, 1, '2020-04-11', '04'),
(13445301, 2, '2020-04-11', '04'),
(13450001, 3, '2020-04-11', '04'),
(14201301, 1, '2020-04-11', '04'),
(14201601, 2, '2020-04-11', '04'),
(14204001, 1, '2020-04-11', '04'),
(14204201, 2, '2020-04-11', '04'),
(14224001, 1, '2020-04-11', '04'),
(14230601, 1, '2020-04-11', '04'),
(14230602, 2, '2020-04-11', '04'),
(14230603, 3, '2020-04-11', '04'),
(14230604, 4, '2020-04-11', '04'),
(14230605, 5, '2020-04-11', '04'),
(14230606, 6, '2020-04-11', '04'),
(14230801, 7, '2020-04-11', '04'),
(14230901, 8, '2020-04-11', '04'),
(14230902, 9, '2020-04-11', '04'),
(14231201, 10, '2020-04-11', '04'),
(14231202, 11, '2020-04-11', '04'),
(14231301, 12, '2020-04-11', '04'),
(14231302, 13, '2020-04-11', '04'),
(14231401, 14, '2020-04-11', '04'),
(14231402, 15, '2020-04-11', '04'),
(14231501, 16, '2020-04-11', '04'),
(14231601, 17, '2020-04-11', '04'),
(14231602, 18, '2020-04-11', '04'),
(14231801, 19, '2020-04-11', '04'),
(14231901, 20, '2020-04-11', '04'),
(14232001, 21, '2020-04-11', '04'),
(14232002, 22, '2020-04-11', '04'),
(14232101, 23, '2020-04-11', '04'),
(14232301, 24, '2020-04-11', '04'),
(14232302, 25, '2020-04-11', '04'),
(14232303, 26, '2020-04-11', '04');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `akun`
--
ALTER TABLE `akun`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `data_kend`
--
ALTER TABLE `data_kend`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `akun`
--
ALTER TABLE `akun`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
