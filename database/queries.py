

CREATE_MEMBERS_TABLE = """
    CREATE TABLE IF NOT EXISTS members(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    total_borrows INT NOT NULL DEFAULT 0
    )
    """

CREATE_BOOKS_TABLE = """
    CREATE TABLE IF NOT EXISTS books(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    genre ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other'),
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    borrowed_by_member_id INT DEFAULT NULL,
    FOREIGN KEY (borrowed_by_member_id) REFERENCES members(id) ON DELETE SET NULL
    )
    """