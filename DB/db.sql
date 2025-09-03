CREATE DATABASE IF NOT EXISTS univap ;

USE univap ;

CREATE TABLE IF NOT EXISTS `univap`.`professores` (
  `registro` INT NOT NULL,
  `nomeprof` VARCHAR(50) NULL,
  `telefoneprof` VARCHAR(30) NULL,
  `idadeprof` INT NULL,
  `salarioprof` FLOAT NULL,
  PRIMARY KEY (`registro`)) ;


CREATE TABLE IF NOT EXISTS `univap`.`disciplinas` (
  `codigodisc` INT NOT NULL,
  `nomedisc` VARCHAR(50) NULL,
  PRIMARY KEY (`codigodisc`)) ;



CREATE TABLE IF NOT EXISTS `univap`.`disciplinasxprofessores` (
  `codigodisciplinanocurso` VARCHAR(10) NOT NULL,
  `codprofessor` INT NULL,
  `coddisciplina` INT NULL,
  `curso` INT NULL,
  `cargahoraria` INT NULL,
  `anoletivo` INT NULL,
  INDEX `fk_professores_has_disciplinas_disciplinas1_idx` (`coddisciplina` ASC),
  INDEX `fk_professores_has_disciplinas_professores_idx` (`codprofessor` ASC),
  PRIMARY KEY (`codigodisciplinanocurso`),
  CONSTRAINT `fk_professores_has_disciplinas_professores`
    FOREIGN KEY (`codprofessor`)
    REFERENCES `univap`.`professores` (`registro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_professores_has_disciplinas_disciplinas1`
    FOREIGN KEY (`coddisciplina`)
    REFERENCES `univap`.`disciplinas` (`codigodisc`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION) ;
