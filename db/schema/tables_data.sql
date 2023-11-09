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