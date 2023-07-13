-- Create table "users" if it doesn't already exist
-- Define an enumeration column "country" with allowed values 'US', 'CO', and 'TN'
-- It should not be null and the default value is set to 'US'
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
