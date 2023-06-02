DROP TABLE IF EXISTS Metal;
DROP TABLE IF EXISTS Size;
DROP TABLE IF EXISTS Style;

CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(60) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(3,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(20) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Jewelry`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `type` NVARCHAR(40) NOT NULL,
    `multiplier` NUMERIC(3,2) NOT NULL
);

CREATE TABLE `Order`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `jewelry_id` INTEGER NOT NULL,
    `timestamp` DATETIME NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metal`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`),
    FOREIGN KEY(`jewelry_id`) REFERENCES `Jewelry`(`id`)
);

INSERT INTO `Metal` VALUES (null, 'Sterling Silver', 500.00);
INSERT INTO `Metal` VALUES (null, '14K Gold', 750.25);
INSERT INTO `Metal` VALUES (null, '24K Gold', 350.00 );
INSERT INTO `Metal` VALUES (null, 'Platinum', 995.45 );
INSERT INTO `Metal` VALUES (null, 'Palladium', 850.99 );

INSERT INTO `Size` VALUES (null, 0.50, 760.00);
INSERT INTO `Size` VALUES (null, 0.75, 500.00);
INSERT INTO `Size` VALUES (null, 1.00, 300.00 );
INSERT INTO `Size` VALUES (null, 1.50, 850.00 );
INSERT INTO `Size` VALUES (null, 2.00, 675.00 );

INSERT INTO `Style` VALUES (null, 'Classic', 710.00 );
INSERT INTO `Style` VALUES (null, 'Modern', 850.00 );
INSERT INTO `Style` VALUES (null, 'Vintage', 565.00 );

INSERT INTO `Jewelry` VALUES (null, 'Ring', 1.00 );
INSERT INTO `Jewelry` VALUES (null, 'Necklace', 2.00 );
INSERT INTO `Jewelry` VALUES (null, 'Earring', 4.00 );

INSERT INTO `Order` VALUES (null, 1, 1, 1, 1, 2023-04-10);
INSERT INTO `Order` VALUES (null, 2, 2, 2, 2, 2023-04-11);
INSERT INTO `Order` VALUES (null, 3, 3, 3, 3, 2023-04-13);
INSERT INTO `Order` VALUES (null, 5, 5, 3, 3, 2023-04-17);

SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    o.jewelry_id,
    o.timestamp,
    m.metal metal_name,
    m.price metal_price,
    z.carets size_carets,
    z.price size_price,
    s.style style_style,
    s.price style_price,
    j.type jewelry_type,
    j.multiplier jewelry_multiplier            
FROM "Order" o
JOIN Metal m
    ON m.id = o.metal_id
JOIN Size z
    ON z.id = o.size_id
JOIN Style s
    ON s.id = o.style_id
JOIN Jewelry j
    ON j.id = o.jewelry_id


SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    o.jewelry_id,
    o.timestamp
FROM "Order" o
WHERE o.id = 2;