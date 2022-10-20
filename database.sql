use code_metrics;
drop table if exists users;
create table if not exists users(
	id int primary key not null auto_increment,
	name varchar(20) unique not null,
	password varchar(20)
);
