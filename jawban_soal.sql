drop table if exists pelukis CASCADE;

create table pelukis (
    pelukis_id int PRIMARY KEY,
    nama_pelukis VARCHAR(255)
);

insert into 
    pelukis(pelukis_id,nama_pelukis)
values 
(1,'Suprapti'),
(2,'Supratman'),
(3,'Suprapto'),
(4,'Suprapta'),
(5,'Supraptu');