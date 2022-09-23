use flask_mysql_coding_dojo;

CREATE TABLE dojos(
id int not null auto_increment PRIMARY KEY,
name varchar(45),
created_at datetime,
updated_at datetime
);

CREATE TABLE ninjas(
id int not null auto_increment primary key,
first_name varchar(45) not null,
last_name varchar(45) not null,
age int not null,
dojo_id int,
created_at datetime,
updated_at datetime,
CONSTRAINT fk_dojos FOREIGN KEY (dojo_id) REFERENCES dojos(id) on delete cascade on update cascade
);
