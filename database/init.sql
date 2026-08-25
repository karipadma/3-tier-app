CREATE TABLE IF NOT EXISTS employees (

    id INT AUTO_INCREMENT PRIMARY KEY,

    fullname VARCHAR(100) NOT NULL,

    email VARCHAR(150) NOT NULL,

    department VARCHAR(100),

    salary DECIMAL(10,2)

);
