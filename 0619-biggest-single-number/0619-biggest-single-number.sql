# Write your MySQL query statement below
# select
#     case
#         when num in (
#             (select num
#             from MyNumbers
#             group by num
#             having count(num) = 1 
#             order by num desc 
#             limit 1)
#         )
#         then num
#         else null
#     end as num
# from MyNumbers;



select max(num) as num
from (
    select num
    from myNumbers
    group by num
    having count(num) = 1
) as unique_number

