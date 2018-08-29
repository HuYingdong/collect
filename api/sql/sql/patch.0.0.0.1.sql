USE omais;

SET character_set_client='utf8';
SET character_set_connection='utf8';
SET character_set_database='utf8';

BEGIN;

CREATE TABLE `userinfo` (
  `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `user_type` integer NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `usertoken` (
  `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `token` varchar(64) NOT NULL,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` integer NOT NULL UNIQUE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `usertoken` ADD CONSTRAINT `usertoken_user_id_7756243cb6230f7a_fk_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`id`);


insert into userinfo (user_type, username, password) values (1, 'zhangsan', 123),
(1, 'lisi', 123),
(2, 'xiaowang', 123),
(3, 'wangwu', 123);

COMMIT;
