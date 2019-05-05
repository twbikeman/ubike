CREATE TABLE ubike (
    id INT NOT NULL AUTO_INCREMENT,
    sno VARCHAR(10),
    sna VARCHAR(16),
    tot INT,
    sbi INT,
    sarea VARCHAR(40),
    mday DATETIME,
    lat FLOAT(9,6),
    lng FLOAT(9,6),
    sareaen VARCHAR(20),
    snaen VARCHAR(80),
    ar VARCHAR(160),
    aren VARCHAR(160),
    bemp INT,
    act INT,
    PRIMARY KEY(id)
);
