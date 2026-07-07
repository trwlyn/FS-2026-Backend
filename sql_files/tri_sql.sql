CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    description TEXT,
    price DECIMAL(10, 2),
    image_url TEXT,
    availability_status VARCHAR(50) DEFAULT 'Available', -- Available, Borrowed, Traded
    can_be_borrowed BOOLEAN DEFAULT TRUE,
    can_be_bought BOOLEAN DEFAULT TRUE,
    can_be_bartered BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);