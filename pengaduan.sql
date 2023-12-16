-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 16, 2023 at 12:15 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pengaduan`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_mahasiswa`
--

CREATE TABLE `data_mahasiswa` (
  `angkatan` int(10) NOT NULL,
  `jumlah` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_mahasiswa`
--

INSERT INTO `data_mahasiswa` (`angkatan`, `jumlah`) VALUES
(2019, 50),
(2020, 130),
(2021, 150),
(2022, 180),
(2023, 200);

-- --------------------------------------------------------

--
-- Table structure for table `kontak_pelayanan`
--

CREATE TABLE `kontak_pelayanan` (
  `pelayanan` varchar(20) NOT NULL,
  `kontak` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kontak_pelayanan`
--

INSERT INTO `kontak_pelayanan` (`pelayanan`, `kontak`) VALUES
('peminjaman', '081234567891'),
('administrasi', '082198765430'),
('kemahasiswaan', '083219845769');

-- --------------------------------------------------------

--
-- Table structure for table `pengaduan_dosen`
--

CREATE TABLE `pengaduan_dosen` (
  `no_pengaduan` int(10) NOT NULL,
  `tanggal` date NOT NULL,
  `nim` varchar(15) NOT NULL,
  `jenis_pengaduan` varchar(20) NOT NULL,
  `matakuliah` varchar(10) NOT NULL,
  `kelas` varchar(5) NOT NULL,
  `keluhan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengaduan_dosen`
--

INSERT INTO `pengaduan_dosen` (`no_pengaduan`, `tanggal`, `nim`, `jenis_pengaduan`, `matakuliah`, `kelas`, `keluhan`) VALUES
(1, '2023-12-16', '220421100076', 'a', 'a', 'a', 'a'),
(3, '2023-12-16', '220421100061', 'a', 'a', 'a', 'a'),
(4, '2023-12-16', '220421100071', 'a', 'a', 'a', 'a'),
(6, '2023-12-16', '220421100176', 'a', 'a', 'a', 'a'),
(7, '2023-12-16', '220421100165', 'a', 'a', 'a', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `pengaduan_fasilitas`
--

CREATE TABLE `pengaduan_fasilitas` (
  `no_pengaduan` int(10) NOT NULL,
  `tanggal` date NOT NULL,
  `nim` varchar(15) NOT NULL,
  `letak` varchar(50) NOT NULL,
  `objek_fasilitas` varchar(20) NOT NULL,
  `kondisi` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pengaduan_pelayanan`
--

CREATE TABLE `pengaduan_pelayanan` (
  `no_pengaduan` int(10) NOT NULL,
  `tanggal` date NOT NULL,
  `nim` varchar(15) NOT NULL,
  `objek_pengaduan` varchar(50) NOT NULL,
  `objek_pelayanan` varchar(50) NOT NULL,
  `keluhan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `nim` varchar(15) NOT NULL,
  `angkatan` int(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`nim`, `angkatan`, `nama`, `email`, `password`) VALUES
('220421100061', 2022, 'M. Aldi Arman H.', '220421100061@student.trunojoyo.ac.id', '324125'),
('220421100071', 2022, 'Nashwa Mayumi', '220421100071@student.trunojoyo.ac.id', '32534'),
('220421100076', 2022, 'Muchammad Bisri', '220421100076@student.trunojoyo.ac.id', '12345'),
('220421100165', 2022, 'Dita Amelia', '220421100165@student.trunojoyo.ac.id', '65675'),
('220421100176', 2022, 'Rif\'atul Amaliyah', '220421100176@student.trunojoyo.ac.id', '5678');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_mahasiswa`
--
ALTER TABLE `data_mahasiswa`
  ADD PRIMARY KEY (`angkatan`);

--
-- Indexes for table `kontak_pelayanan`
--
ALTER TABLE `kontak_pelayanan`
  ADD PRIMARY KEY (`kontak`);

--
-- Indexes for table `pengaduan_dosen`
--
ALTER TABLE `pengaduan_dosen`
  ADD PRIMARY KEY (`no_pengaduan`),
  ADD KEY `melakukan_pengaduan` (`nim`);

--
-- Indexes for table `pengaduan_fasilitas`
--
ALTER TABLE `pengaduan_fasilitas`
  ADD PRIMARY KEY (`no_pengaduan`),
  ADD KEY `nim` (`nim`);

--
-- Indexes for table `pengaduan_pelayanan`
--
ALTER TABLE `pengaduan_pelayanan`
  ADD PRIMARY KEY (`no_pengaduan`),
  ADD UNIQUE KEY `mengadu` (`nim`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`nim`),
  ADD KEY `terdiri` (`angkatan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pengaduan_dosen`
--
ALTER TABLE `pengaduan_dosen`
  MODIFY `no_pengaduan` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `pengaduan_fasilitas`
--
ALTER TABLE `pengaduan_fasilitas`
  MODIFY `no_pengaduan` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pengaduan_pelayanan`
--
ALTER TABLE `pengaduan_pelayanan`
  MODIFY `no_pengaduan` int(10) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pengaduan_dosen`
--
ALTER TABLE `pengaduan_dosen`
  ADD CONSTRAINT `pengaduan_dosen_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `user` (`nim`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pengaduan_fasilitas`
--
ALTER TABLE `pengaduan_fasilitas`
  ADD CONSTRAINT `pengaduan_fasilitas_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `user` (`nim`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pengaduan_pelayanan`
--
ALTER TABLE `pengaduan_pelayanan`
  ADD CONSTRAINT `pengaduan_pelayanan_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `user` (`nim`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`angkatan`) REFERENCES `data_mahasiswa` (`angkatan`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
