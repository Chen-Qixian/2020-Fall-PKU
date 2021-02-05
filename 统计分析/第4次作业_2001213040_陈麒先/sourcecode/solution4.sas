data work.visit1;
input id expense;
datalines;
001      500
001      400
003      350
;

data work.visit2;
input id cost;
datalines;
001     300
002     600
;

proc sql;
select Id, sum(Expense) label='COST'
from WORK.VISIT1
group by 1
union all
select Id, sum(Cost)
from WORK.VISIT2
group by 1
order by 1,2;
quit;
