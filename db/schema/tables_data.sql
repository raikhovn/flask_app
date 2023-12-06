INSERT INTO users (user_id, first_name,  last_name ) VALUES ('user1', 'john1', 'doe1');
INSERT INTO users (user_id, first_name,  last_name ) VALUES ('user2', 'john2', 'doe2');
INSERT INTO users (user_id, first_name,  last_name ) VALUES ('user3', 'john3', 'doe3');

INSERT INTO user_cars (car_id, model,  price, user_id ) VALUES ('1', 'bmw', '30,000', 'user1');
INSERT INTO user_cars (car_id, model,  price, user_id ) VALUES ('2', 'merc', '30,000', 'user1');
INSERT INTO user_cars (car_id, model,  price, user_id ) VALUES ('3', 'ferrari', '330,000', 'user2');
INSERT INTO user_cars (car_id, model,  price, user_id ) VALUES ('4', 'porshe', '90,000', 'user3');

INSERT INTO user_phones (phone_id, mobile, user_id) VALUES ( '1', '2126969944', 'user1');
INSERT INTO user_phones (phone_id, mobile, user_id) VALUES ( '2', '2126969945', 'user2');
INSERT INTO user_phones (phone_id, mobile, user_id) VALUES ( '3', '2126969946', 'user3');

INSERT INTO products (product_id, item, price) VALUES (1, 'table', 100);
INSERT INTO products (product_id, item, price) VALUES (2, 'chair', 60);
INSERT INTO products (product_id, item, price) VALUES (3, 'lamp', 20);
INSERT INTO products (product_id, item, price) VALUES (4, 'dresser', 500);

INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (1, 1, '2023/11/4', 1, 'CT', 'user1' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (2, 1, '2023/11/1', 1, 'NY', 'user1' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (3, 2, '2023/11/8', 4, 'CT', 'user1' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (4, 3, '2023/11/7', 4, 'MA', 'user1' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (5, 1, '2023/11/4', 1, 'FL', 'user2' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (6, 2, '2023/11/4', 4, 'FL', 'user2' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (7, 4, '2023/11/1', 3, 'IL', 'user3' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (8, 1, '2023/11/1', 1, 'NY', 'user3' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (9, 3, '2023/11/1', 4, 'NY', 'user3' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (10, 2, '2023/11/1', 2, 'NY', 'user2' );
INSERT INTO user_purchases (purchase_id , product_id, dt, count, st, user_id) VALUES (11, 4, '2023/11/1', 3, 'NY', 'user2' );


--select u.first_name, u.last_name, up.st, up.count * p.price as total, RANK() OVER (PARTITION BY up.st ORDER BY up.count * p.price DESC) FROM  users u  INNER JOIN user_purchases up ON u.user_id = up.user_id INNER JOIN products p ON up.product_id = p.product_id;