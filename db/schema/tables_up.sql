

grant all privileges on database userdb to postgres;

CREATE TABLE IF NOT EXISTS users (user_id text primary key, first_name text NOT NULL,  last_name text NOT NULL);
    
CREATE TABLE IF NOT EXISTS user_cars (car_id text primary key,  model text NOT NULL, price text NULL, user_id text references users(user_id));

CREATE TABLE IF NOT EXISTS user_phones (phone_id text primary key,  home text NULL,mobile text NOT NULL,user_id text references users(user_id));

CREATE TABLE IF NOT EXISTS products (product_id int primary key,  item text NULL,price int NOT NULL);

CREATE TABLE IF NOT EXISTS user_purchases (purchase_id int primary key, product_id int references products(product_id), count int, dt date, st text, user_id text references users(user_id));
   
