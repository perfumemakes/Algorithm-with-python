-- 코드를 입력하세요
select a.product_id, a.product_name, (a.price*b.amount) as total_sales
from food_product a, 
(select product_id, sum(amount) as amount
from food_order
where to_char(produce_date,'yyyymmdd') >= 20220501
and
to_char(produce_date,'yyyymmdd') <20220601
group by product_id) b
where a.product_id = b.product_id
order by 3 desc, 1;