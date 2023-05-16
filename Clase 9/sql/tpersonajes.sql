create database test1;

CREATE TABLE `tpersonajes` (
  `idpersonaje` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `atler` varchar(255) NOT NULL,
  `edad` smallint(5) UNSIGNED NOT NULL,
  `ideditorial` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `tpersonajes`
  ADD PRIMARY KEY (`idpersonaje`),
  ADD UNIQUE KEY `nombre_UNIQUE` (`nombre`),
  ADD UNIQUE KEY `atler_UNIQUE` (`atler`);

ALTER TABLE `tpersonajes`
  MODIFY `idpersonaje` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

INSERT INTO `teditorial` (`ideditorial`, `editorial`) VALUES ('1', 'DC'), ('2', 'Marvel');

INSERT INTO `tpersonajes` (`idpersonaje`, `nombre`, `atler`, `edad`, `ideditorial`) VALUES ('1', 'Superman', 'Clark Kent', '35', '1'), ('2', 'Batman', 'Bruce Wayne', '45', '1');
INSERT INTO `tpersonajes` (`idpersonaje`, `nombre`, `atler`, `edad`, `ideditorial`) VALUES ('3', 'Ironman', 'Tony Stark', '50', '2'), ('4', 'Captain America', 'Steve Rogers', '99', '2');

SELECT nombre FROM `tpersonajes`;
SELECT * FROM `tpersonajes` WHERE edad >35 ORDER BY nombre asc
 /*DELETE FROM `tpersonajes` WHERE `tpersonajes`.`idpersonaje` = 1*/