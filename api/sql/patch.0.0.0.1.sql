USE collect;

SET character_set_client='utf8';
SET character_set_connection='utf8';
SET character_set_database='utf8';

begin;

CREATE TABLE `bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT primary key,
  `issue` varchar(255) not null,
  `url` varchar(255) not null unique,
  `sort` varchar(20) not null DEFAULT 'unknown',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) not null default '0'
) ENGINE=InnoDB, DEFAULT CHARSET=utf8;

CREATE TABLE `command` (
  `id` int(11) NOT NULL AUTO_INCREMENT primary key,
  `issue` varchar(255) not null,
  `cmd` varchar(255) not null unique,
  `remark` varchar(255) not null default 'null',
  `sort` varchar(20) not null DEFAULT 'unknown',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) not null default '0'
) ENGINE=InnoDB, DEFAULT CHARSET=utf8;


commit;
