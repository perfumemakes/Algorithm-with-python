-- 코드를 입력하세요
select a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS,
to_char(b.CREATED_DATE, 'yyyy-mm-dd') CREATED_DATE
from USED_GOODS_BOARD a, USED_GOODS_REPLY b
where a.BOARD_ID = b.BOARD_ID
and a.CREATED_DATE
between to_date('2022-10-01', 'yyyy-mm-dd') and to_date('2022-10-31','yyyy-mm-dd')
order by b.CREATED_DATE asc, a.TITLE asc