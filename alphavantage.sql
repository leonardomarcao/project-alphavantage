BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `stock_import` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`close`	REAL NOT NULL DEFAULT 0,
	`stock_id`	INTEGER NOT NULL,
	FOREIGN KEY(`stock_id`) REFERENCES `stock`(`id`)
);
CREATE TABLE IF NOT EXISTS `stock` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`symbol`	TEXT NOT NULL,
	`name`	TEXT NOT NULL,
	`active`	INTEGER NOT NULL DEFAULT 1
);
INSERT INTO `stock` (id,symbol,name,active) VALUES (1,'B3SA3.SA','B3SA3.SAO',1);
INSERT INTO `stock` (id,symbol,name,active) VALUES (2,'PETR4.SA','PETR4.SAO',1);
CREATE UNIQUE INDEX IF NOT EXISTS `stock_imported_date_idx` ON `stock_import` (
	`stock_id`,
	`date`
);
COMMIT;
