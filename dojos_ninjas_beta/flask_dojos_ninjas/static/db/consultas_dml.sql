use flask_mysql_coding_dojo;

 -- select n.id as ninja_id, CONCAT(n.first_name, " ", n.last_name) as ninja_full_name, d.name as dojo_name, d.id as dojo_id from dojos d left join ninjas n on d.id = n.dojo_id where d.id = 9;
-- select d.id as d_id, d.name as d_name, n.id as nid, n.first_name as n_first_name, 
-- n.last_name as n_last_name, n.age as n_age, n.created_at as n_created_at, n.updated_at as n_updated_at 
-- from dojos d left join ninjas n on d.id = n.dojo_id where d.id = 9;

-- insert into ninjas (first_name, last_name, age, dojo_id) values ('Adrien','Dion',30, 8);
-- insert into ninjas (first_name, last_name, age, dojo_id) values ('Francisco','Boisier',30, 9);

-- update dojos set name = 'tokugawa dojo' where id = 4; 
select * from dojos;
