DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    views INTEGER,
    user_id INTEGER,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (email_address, username) VALUES ('johnjohnson@john.com', 'johnj');
INSERT INTO users (email_address, username) VALUES ('adam@adamson.com', 'adama');
INSERT INTO users (email_address, username) VALUES ('jenjennson@jenny.com', 'jennyj');

INSERT INTO posts (title, content, views, user_id) VALUES ('the title', 'this is some content', 14, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('the title', 'this is some content', 12, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('the title', 'this is some content', 7, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('the title', 'this is some content', 4, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('the title', 'this is some content', 9, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('the title', 'this is some content', 36, 1);
