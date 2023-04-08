-- 코드를 입력하세요
select name, datetime
from (select a.animal_id, a.name as name, a.datetime as datetime, b.animal_id as animal_id2
from animal_ins a left outer join animal_outs b
on a.animal_id = b.animal_id
order by a.datetime)
where animal_id2 is null 
and
rownum < 4