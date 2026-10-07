CREATE TABLE expenses(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    category TEXT NOT NULL,
    expense_date DATE NOT NULL
);

SELECT * FROM expenses;