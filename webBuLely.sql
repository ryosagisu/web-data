-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 31, 2018 at 04:25 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.1.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webBuLely`
--

-- --------------------------------------------------------

--
-- Table structure for table `kkni`
--

CREATE TABLE `kkni` (
  `bidang` varchar(64) NOT NULL,
  `jenjang` varchar(8) NOT NULL,
  `sikap_kerja` varchar(255) NOT NULL,
  `kd_profesi` varchar(10) NOT NULL,
  `nama_profesi` varchar(100) NOT NULL,
  `deskripsi_profesi` varchar(255) NOT NULL,
  `kemungkinan_jabatan` varchar(255) NOT NULL,
  `peran_kerja` varchar(255) NOT NULL,
  `unit_kompetensi` varchar(255) NOT NULL,
  `kd_unit_kompetensi` varchar(255) NOT NULL,
  `judul_unit_kompetensi` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `kkni`
--

INSERT INTO `kkni` (`bidang`, `jenjang`, `sikap_kerja`, `kd_profesi`, `nama_profesi`, `deskripsi_profesi`, `kemungkinan_jabatan`, `peran_kerja`, `unit_kompetensi`, `kd_unit_kompetensi`, `judul_unit_kompetensi`) VALUES
('Operator and system tools', '1', 'sikap kerja 1, sikap kerja 2', '050105', 'Print Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '1', 'sikap kerja 1, sikap kerja 2', '050104', 'Asisten Operator Komputer', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '1', 'sikap kerja 1, sikap kerja 2', '050103', 'Computer Technician Clerk', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '1', 'sikap kerja 1, sikap kerja 2', '050102', 'Basic Office Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '1', 'sikap kerja 1, sikap kerja 2', '050101', 'Junior Office Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '2', 'sikap kerja 1, sikap kerja 2', '050205', 'Computer Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '2', 'sikap kerja 1, sikap kerja 2', '050204', 'Word Processing Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '2', 'sikap kerja 1, sikap kerja 2', '050203', 'Helpdesk', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '2', 'sikap kerja 1, sikap kerja 2', '050202', 'Senior Office Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '2', 'sikap kerja 1, sikap kerja 2', '050201', 'Operator Komputer Muda', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050312', 'Desktop Technician', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050311', 'Computer Repair Technician', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050310', 'Word Processing Lead Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050309', 'Desktop Specialist', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050308', 'Helpdesk Specialist', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050307', 'Advance Office Operator', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050306', 'Operator Komputer Olah Data Statistik', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050305', 'Operator Komputer Kependudukan', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050304', 'Operator Komputer Quantity Surveyor', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050303', 'Operator Komputer Rancang Bangun', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050302', 'Operator Komputer Penjaminan Mutu', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2'),
('Operator and system tools', '3', 'sikap kerja 1, sikap kerja 2', '050301', 'Operator Komputer Madya', 'deskripsi 1, deskripsi 2', 'jabatan 1, jabatan 2', 'peran kerja 1, peran kerja 2', 'kompetensi 1, kompetensi 2', 'kode 1, kode 2', 'judul 1, judul 2');

-- --------------------------------------------------------

--
-- Table structure for table `peta_okupasi`
--

CREATE TABLE `peta_okupasi` (
  `kode_okupasi` varchar(64) NOT NULL,
  `nama_okupasi` varchar(100) NOT NULL,
  `kd_kompetensi` varchar(20) NOT NULL,
  `deskripsi` varchar(64) NOT NULL,
  `tugas_utama` varchar(64) NOT NULL,
  `persyaratan` varchar(64) NOT NULL,
  `lingkup_pekerjaan` varchar(64) NOT NULL,
  `verifikasi` varchar(64) NOT NULL,
  `wewenang` varchar(64) NOT NULL,
  `jenjang_karir` varchar(64) NOT NULL,
  `sertifikasi` varchar(64) NOT NULL,
  `profil` varchar(64) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `peta_okupasi`
--

INSERT INTO `peta_okupasi` (`kode_okupasi`, `nama_okupasi`, `kd_kompetensi`, `deskripsi`, `tugas_utama`, `persyaratan`, `lingkup_pekerjaan`, `verifikasi`, `wewenang`, `jenjang_karir`, `sertifikasi`, `profil`) VALUES
('050105', 'Print Operator', 'TIK.CS02.019.01', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2'),
('050105', 'Print Operator', 'ICAICT101A', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2'),
('050105', 'Print Operator', 'ICAICT201A', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2'),
('050105', 'Print Operator', 'TIK.OP02.002.01', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2'),
('050105', 'Print Operator', 'J.620900.016.02', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2'),
('050103', 'Computer Technician Clerk', 'J.620900.007.02', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2'),
('050103', 'Computer Technician Clerk', 'J.620900.006.01', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2'),
('050103', 'Computer Technician Clerk', 'ICAICT101A', 'deskripsi 1, deskripsi 2', 'tu 1, tu 2', 'syarat 1, syarat 2', 'scope 1, scope 2', 'verifikasi 1, verifikasi 2', 'wewenang 1, wewenang 2', 'karir 1, karir 2', 'sertifikat 1, sertifikat 2', 'profil 1, profil 2');

-- --------------------------------------------------------

--
-- Table structure for table `skkni`
--

CREATE TABLE `skkni` (
  `tujuan_utama` text NOT NULL,
  `fungsi_kunci` text NOT NULL,
  `fungsi_utama` text NOT NULL,
  `kode_unit` varchar(20) NOT NULL,
  `judul_unit` varchar(255) NOT NULL,
  `elemen_kompetensi` text NOT NULL,
  `deskripsi_unit` text NOT NULL,
  `panduan_penilaian` text NOT NULL,
  `konteks_penilaian` text NOT NULL,
  `ketrampilan` text NOT NULL,
  `aspek_kritis` text NOT NULL,
  `sikap_kerja` text NOT NULL,
  `pengetahuan` text NOT NULL,
  `batasan_variabel` text NOT NULL,
  `konteks_variabel` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `skkni`
--

INSERT INTO `skkni` (`tujuan_utama`, `fungsi_kunci`, `fungsi_utama`, `kode_unit`, `judul_unit`, `elemen_kompetensi`, `deskripsi_unit`, `panduan_penilaian`, `konteks_penilaian`, `ketrampilan`, `aspek_kritis`, `sikap_kerja`, `pengetahuan`, `batasan_variabel`, `konteks_variabel`) VALUES
('Menggunakan perangkat komputer dan aplikasinya sesuai dengan kebutuhan pengguna', 'Menggunakan perangkat komputer dan aplikasinya tingkat dasar', 'Mengoperasikan computer', 'TIK.CS02.019.01', 'Menggunakan  perangkat komputer', 'Menyalakan perangkat komputer dan mengamati proses aktifasi sistem (booting) hingga selesai', 'Unit kompetensi ini berkaitan dengan pengetahuan keterampilan dan sikap kerja yang dibutuhkan untuk menggunakan perangkat komputer dalam kondisi normal.', 'penilaian 1, penilaian 2', 'konteks 1, konteks 2', 'keterampilan a, b, c', 'aspek 1, aspek 2, aspek 3', 'sk1, sk2, sk3', 'pengetahuan 1, pengetahuan 2', 'bv1, bv2, bv3', 'kv1, kv2, kv3'),
('Menggunakan perangkat komputer dan aplikasinya sesuai dengan kebutuhan pengguna', 'Menggunakan perangkat komputer dan aplikasinya tingkat dasar', 'Mengoperasikan computer', 'ICAICT101A', 'Menggunakan Sistem Operasi', 'Mengenali perintah dan GUI windows/ menu/ ikon (icon)/  kursor yang berasosiasi dengannya', 'Unit kompetensi ini berhubungan dengan pengetahuan, keterampilan, dan sikap kerja yang dibutuhkan untuk menggunakan sistem operasi pada perangkat komputer dalam kondisi normal.', 'penilaian 1, penilaian 2', 'konteks 1, konteks 2', 'keterampilan a, b, c', 'aspek 1, aspek 2, aspek 3', 'sk1, sk2, sk3', 'pengetahuan 1, pengetahuan 2', 'bv1, bv2, bv3', 'kv1, kv2, kv3'),
('Menggunakan perangkat komputer dan aplikasinya sesuai dengan kebutuhan pengguna', 'Menggunakan perangkat komputer dan aplikasinya tingkat dasar', 'Mengoperasikan computer', 'ICAICT201A', 'Menggunakan Sistem Operasi 1', 'Mengenali perintah dan GUI windows/ menu/ ikon (icon)/  kursor yang berasosiasi dengannya', 'Unit kompetensi ini berhubungan dengan pengetahuan, keterampilan, dan sikap kerja yang dibutuhkan untuk menggunakan sistem operasi pada perangkat komputer dalam kondisi normal.', 'penilaian 1, penilaian 2', 'konteks 1, konteks 2', 'keterampilan a, b, c', 'aspek 1, aspek 2, aspek 3', 'sk1, sk2, sk3', 'pengetahuan 1, pengetahuan 2', 'bv1, bv2, bv3', 'kv1, kv2, kv3'),
('Menggunakan perangkat komputer dan aplikasinya sesuai dengan kebutuhan pengguna', 'Menggunakan perangkat komputer dan aplikasinya tingkat dasar', 'Mengoperasikan computer', 'TIK.OP02.002.01', 'Menggunakan Sistem Operasi 2', 'Mengenali perintah dan GUI windows/ menu/ ikon (icon)/  kursor yang berasosiasi dengannya', 'Unit kompetensi ini berhubungan dengan pengetahuan, keterampilan, dan sikap kerja yang dibutuhkan untuk menggunakan sistem operasi pada perangkat komputer dalam kondisi normal.', 'penilaian 1, penilaian 2', 'konteks 1, konteks 2', 'keterampilan a, b, c', 'aspek 1, aspek 2, aspek 3', 'sk1, sk2, sk3', 'pengetahuan 1, pengetahuan 2', 'bv1, bv2, bv3', 'kv1, kv2, kv3'),
('Menggunakan perangkat komputer dan aplikasinya sesuai dengan kebutuhan pengguna', 'Menggunakan perangkat komputer dan aplikasinya tingkat dasar', 'Mengoperasikan computer', 'J.620900.016.02', 'Menggunakan Sistem Operasi 3', 'Mengenali perintah dan GUI windows/ menu/ ikon (icon)/  kursor yang berasosiasi dengannya', 'Unit kompetensi ini berhubungan dengan pengetahuan, keterampilan, dan sikap kerja yang dibutuhkan untuk menggunakan sistem operasi pada perangkat komputer dalam kondisi normal.', 'penilaian 1, penilaian 2', 'konteks 1, konteks 2', 'keterampilan a, b, c', 'aspek 1, aspek 2, aspek 3', 'sk1, sk2, sk3', 'pengetahuan 1, pengetahuan 2', 'bv1, bv2, bv3', 'kv1, kv2, kv3'),
('Menggunakan perangkat komputer dan aplikasinya sesuai dengan kebutuhan pengguna', 'Menggunakan perangkat komputer dan aplikasinya tingkat dasar', 'Mengoperasikan computer', 'J.620900.007.02', 'Menggunakan Sistem Operasi 4', 'Mengenali perintah dan GUI windows/ menu/ ikon (icon)/  kursor yang berasosiasi dengannya', 'Unit kompetensi ini berhubungan dengan pengetahuan, keterampilan, dan sikap kerja yang dibutuhkan untuk menggunakan sistem operasi pada perangkat komputer dalam kondisi normal.', 'penilaian 1, penilaian 2', 'konteks 1, konteks 2', 'keterampilan a, b, c', 'aspek 1, aspek 2, aspek 3', 'sk1, sk2, sk3', 'pengetahuan 1, pengetahuan 2', 'bv1, bv2, bv3', 'kv1, kv2, kv3'),
('Menggunakan perangkat komputer dan aplikasinya sesuai dengan kebutuhan pengguna', 'Menggunakan perangkat komputer dan aplikasinya tingkat dasar', 'Mengoperasikan computer', 'J.620900.006.01', 'Menggunakan Sistem Operasi 5', 'Mengenali perintah dan GUI windows/ menu/ ikon (icon)/  kursor yang berasosiasi dengannya', 'Unit kompetensi ini berhubungan dengan pengetahuan, keterampilan, dan sikap kerja yang dibutuhkan untuk menggunakan sistem operasi pada perangkat komputer dalam kondisi normal.', 'penilaian 1, penilaian 2', 'konteks 1, konteks 2', 'keterampilan a, b, c', 'aspek 1, aspek 2, aspek 3', 'sk1, sk2, sk3', 'pengetahuan 1, pengetahuan 2', 'bv1, bv2, bv3', 'kv1, kv2, kv3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `skkni`
--
ALTER TABLE `skkni`
  ADD PRIMARY KEY (`kode_unit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
