CREATE TABLE CarData (
  id INT AUTO_INCREMENT PRIMARY KEY,
  vin VARCHAR(255),
  year INT,
  make VARCHAR(255),
  model VARCHAR(255),
  listing_price DOUBLE,
  listing_mileage DOUBLE
);