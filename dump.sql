-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema pharmacy
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pharmacy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pharmacy` DEFAULT CHARACTER SET latin1 ;
USE `pharmacy` ;

-- -----------------------------------------------------
-- Table `pharmacy`.`overview_customuser`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`overview_customuser` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `phone` BIGINT(20) NOT NULL,
  `isadmin` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`account_emailaddress`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`account_emailaddress` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(254) NOT NULL,
  `verified` TINYINT(1) NOT NULL,
  `primary` TINYINT(1) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email` (`email` ASC),
  INDEX `account_emailaddress_user_id_2c513194_fk_overview_customuser_id` (`user_id` ASC),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_overview_customuser_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`account_emailconfirmation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`account_emailconfirmation` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `sent` DATETIME NULL DEFAULT NULL,
  `key` VARCHAR(64) NOT NULL,
  `email_address_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `key` (`key` ASC),
  INDEX `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id` ASC),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e`
    FOREIGN KEY (`email_address_id`)
    REFERENCES `pharmacy`.`account_emailaddress` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`auth_group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`django_content_type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 24
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`auth_permission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT(11) NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `pharmacy`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 93
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`auth_group_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `group_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC),
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `pharmacy`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `pharmacy`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`authtoken_token`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`authtoken_token` (
  `key` VARCHAR(40) NOT NULL,
  `created` DATETIME NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE INDEX `user_id` (`user_id` ASC),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_overview_customuser_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`overview_pharmacy`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`overview_pharmacy` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `address` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 24
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_stock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_stock` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `unit` INT(11) NOT NULL,
  `desc` VARCHAR(200) NULL DEFAULT NULL,
  `pharmacy_id` INT(11) NOT NULL,
  `date_created` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_stock_pharmacy_id_755f7481_fk_overview_pharmacy_id` (`pharmacy_id` ASC),
  CONSTRAINT `company_stock_pharmacy_id_755f7481_fk_overview_pharmacy_id`
    FOREIGN KEY (`pharmacy_id`)
    REFERENCES `pharmacy`.`overview_pharmacy` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_company` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `Description` VARCHAR(200) NULL DEFAULT NULL,
  `stock_id` INT(11) NULL DEFAULT NULL,
  `address` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_company_stock_id_43f06c9c_fk_company_stock_id` (`stock_id` ASC),
  CONSTRAINT `company_company_stock_id_43f06c9c_fk_company_stock_id`
    FOREIGN KEY (`stock_id`)
    REFERENCES `pharmacy`.`company_stock` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_message`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_message` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `msg` VARCHAR(200) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  `date_created` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_message_user_id_5c276638_fk_overview_customuser_id` (`user_id` ASC),
  CONSTRAINT `company_message_user_id_5c276638_fk_overview_customuser_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_order` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `total` INT(11) NOT NULL,
  `date_created` DATETIME NOT NULL,
  `total_profit` INT(11) NOT NULL,
  `stock_id` INT(11) NOT NULL,
  `company_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_order_stock_id_f2ba3c9a_fk_company_stock_id` (`stock_id` ASC),
  INDEX `company_order_company_id_485d8f44_fk_company_company_id` (`company_id` ASC),
  CONSTRAINT `company_order_company_id_485d8f44_fk_company_company_id`
    FOREIGN KEY (`company_id`)
    REFERENCES `pharmacy`.`company_company` (`id`),
  CONSTRAINT `company_order_stock_id_f2ba3c9a_fk_company_stock_id`
    FOREIGN KEY (`stock_id`)
    REFERENCES `pharmacy`.`company_stock` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_stockitem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_stockitem` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `unit` INT(11) NOT NULL,
  `desc` VARCHAR(200) NULL DEFAULT NULL,
  `type` VARCHAR(200) NULL DEFAULT NULL,
  `cost_per_tab` DECIMAL(5,2) NOT NULL,
  `stock_id` INT(11) NOT NULL,
  `profit_per_tab` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_stockitem_stock_id_1e7e9834_fk_company_stock_id` (`stock_id` ASC),
  CONSTRAINT `company_stockitem_stock_id_1e7e9834_fk_company_stock_id`
    FOREIGN KEY (`stock_id`)
    REFERENCES `pharmacy`.`company_stock` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 42
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_userstock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_userstock` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `unit` INT(11) NOT NULL,
  `desc` VARCHAR(200) NULL DEFAULT NULL,
  `date_created` DATETIME NOT NULL,
  `pharmacy_id` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_userstock_pharmacy_id_cc269028_fk_overview_pharmacy_id` (`pharmacy_id` ASC),
  INDEX `company_userstock_user_id_fc42be73_fk_overview_customuser_id` (`user_id` ASC),
  CONSTRAINT `company_userstock_pharmacy_id_cc269028_fk_overview_pharmacy_id`
    FOREIGN KEY (`pharmacy_id`)
    REFERENCES `pharmacy`.`overview_pharmacy` (`id`),
  CONSTRAINT `company_userstock_user_id_fc42be73_fk_overview_customuser_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_userorder`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_userorder` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `total` INT(11) NOT NULL,
  `date_created` DATETIME NOT NULL,
  `total_profit` INT(11) NOT NULL,
  `company_id` INT(11) NULL DEFAULT NULL,
  `stock_id` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  `fulfilled` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_userorder_company_id_fde649a9_fk_company_company_id` (`company_id` ASC),
  INDEX `company_userorder_user_id_c0cf0681_fk_overview_customuser_id` (`user_id` ASC),
  INDEX `company_userorder_stock_id_48559fda_fk_company_userstock_id` (`stock_id` ASC),
  CONSTRAINT `company_userorder_company_id_fde649a9_fk_company_company_id`
    FOREIGN KEY (`company_id`)
    REFERENCES `pharmacy`.`company_company` (`id`),
  CONSTRAINT `company_userorder_stock_id_48559fda_fk_company_userstock_id`
    FOREIGN KEY (`stock_id`)
    REFERENCES `pharmacy`.`company_userstock` (`id`),
  CONSTRAINT `company_userorder_user_id_c0cf0681_fk_overview_customuser_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`company_userstockitem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`company_userstockitem` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `unit` INT(11) NOT NULL,
  `desc` VARCHAR(200) NULL DEFAULT NULL,
  `type` VARCHAR(200) NULL DEFAULT NULL,
  `cost_per_tab` DECIMAL(5,2) NOT NULL,
  `profit_per_tab` DECIMAL(5,2) NOT NULL,
  `stock_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `company_userstockitem_stock_id_feae1ac9_fk_company_userstock_id` (`stock_id` ASC),
  CONSTRAINT `company_userstockitem_stock_id_feae1ac9_fk_company_userstock_id`
    FOREIGN KEY (`stock_id`)
    REFERENCES `pharmacy`.`company_userstock` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`django_admin_log` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT(5) UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT(11) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC),
  INDEX `django_admin_log_user_id_c564eba6_fk_overview_customuser_id` (`user_id` ASC),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `pharmacy`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_overview_customuser_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`django_migrations` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 74
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`django_site`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`django_site` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `domain` VARCHAR(100) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_site_domain_a2e37b91_uniq` (`domain` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`drug_drug`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`drug_drug` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `unit` INT(11) NOT NULL,
  `desc` VARCHAR(200) NULL DEFAULT NULL,
  `type` VARCHAR(200) NULL DEFAULT NULL,
  `cost_per_tab` DECIMAL(5,2) NOT NULL,
  `pharmacy_id` INT(11) NOT NULL,
  `expiry_date` DATE NOT NULL,
  `profit_per_tab` DECIMAL(5,2) NOT NULL,
  `shelf_number` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `drug_drug_pharmacy_id_015d687b_fk_overview_pharmacy_id` (`pharmacy_id` ASC),
  CONSTRAINT `drug_drug_pharmacy_id_015d687b_fk_overview_pharmacy_id`
    FOREIGN KEY (`pharmacy_id`)
    REFERENCES `pharmacy`.`overview_pharmacy` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`overview_customuser_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`overview_customuser_groups` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` INT(11) NOT NULL,
  `group_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `overview_customuser_groups_customuser_id_group_id_8549d3ec_uniq` (`customuser_id` ASC, `group_id` ASC),
  INDEX `overview_customuser_groups_group_id_e2f8df1e_fk_auth_group_id` (`group_id` ASC),
  CONSTRAINT `overview_customuser__customuser_id_abad17ab_fk_overview_`
    FOREIGN KEY (`customuser_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`),
  CONSTRAINT `overview_customuser_groups_group_id_e2f8df1e_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `pharmacy`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`overview_customuser_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`overview_customuser_user_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `overview_customuser_user_customuser_id_permission_1e8eb965_uniq` (`customuser_id` ASC, `permission_id` ASC),
  INDEX `overview_customuser__permission_id_3aff94a5_fk_auth_perm` (`permission_id` ASC),
  CONSTRAINT `overview_customuser__customuser_id_24733784_fk_overview_`
    FOREIGN KEY (`customuser_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`),
  CONSTRAINT `overview_customuser__permission_id_3aff94a5_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `pharmacy`.`auth_permission` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`socialaccount_socialaccount`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`socialaccount_socialaccount` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `provider` VARCHAR(30) NOT NULL,
  `uid` VARCHAR(191) NOT NULL,
  `last_login` DATETIME NOT NULL,
  `date_joined` DATETIME NOT NULL,
  `extra_data` LONGTEXT NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider` ASC, `uid` ASC),
  INDEX `socialaccount_social_user_id_8146e70c_fk_overview_` (`user_id` ASC),
  CONSTRAINT `socialaccount_social_user_id_8146e70c_fk_overview_`
    FOREIGN KEY (`user_id`)
    REFERENCES `pharmacy`.`overview_customuser` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`socialaccount_socialapp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`socialaccount_socialapp` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `provider` VARCHAR(30) NOT NULL,
  `name` VARCHAR(40) NOT NULL,
  `client_id` VARCHAR(191) NOT NULL,
  `secret` VARCHAR(191) NOT NULL,
  `key` VARCHAR(191) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`socialaccount_socialapp_sites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`socialaccount_socialapp_sites` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `socialapp_id` INT(11) NOT NULL,
  `site_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id` ASC, `site_id` ASC),
  INDEX `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id` ASC),
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc`
    FOREIGN KEY (`socialapp_id`)
    REFERENCES `pharmacy`.`socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id`
    FOREIGN KEY (`site_id`)
    REFERENCES `pharmacy`.`django_site` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pharmacy`.`socialaccount_socialtoken`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pharmacy`.`socialaccount_socialtoken` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `token` LONGTEXT NOT NULL,
  `token_secret` LONGTEXT NOT NULL,
  `expires_at` DATETIME NULL DEFAULT NULL,
  `account_id` INT(11) NOT NULL,
  `app_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id` ASC, `account_id` ASC),
  INDEX `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id` ASC),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc`
    FOREIGN KEY (`account_id`)
    REFERENCES `pharmacy`.`socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc`
    FOREIGN KEY (`app_id`)
    REFERENCES `pharmacy`.`socialaccount_socialapp` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
