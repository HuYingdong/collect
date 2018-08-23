USE collect;

SET character_set_client='utf8';
SET character_set_connection='utf8';
SET character_set_database='utf8';

begin;

ALTER TABLE `bookmark` ADD COLUMN `owner_id` int(11) NOT NULL;
UPDATE `bookmark` set `owner_id`=1;

commit;
