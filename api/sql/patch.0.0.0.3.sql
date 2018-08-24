USE collect;

SET character_set_client='utf8';
SET character_set_connection='utf8';
SET character_set_database='utf8';

begin;

CREATE TABLE `userinfo` (
  `id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `user_type` integer NOT NULL,
  `username` varchar(32) NOT NULL UNIQUE,
  `password` varchar(64) NOT NULL
) ENGINE=InnoDB, DEFAULT CHARSET=utf8;

CREATE TABLE `usertoken` (
  `id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `token` varchar(64) NOT NULL, `
  user_id` integer NOT NULL UNIQUE
) ENGINE=InnoDB, DEFAULT CHARSET=utf8;

ALTER TABLE `bookmark` ADD CONSTRAINT `bookmark_owner_id_433b364e_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `command` ADD CONSTRAINT `command_owner_id_9ce053fa_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `usertoken` ADD CONSTRAINT `usertoken_user_id_1359036f_fk_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`id`);

commit;
