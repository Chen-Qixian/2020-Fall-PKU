data work.one;
input name $ salary;
datalines;
Hans      200
Maria     205
Jose        310
Ariel       523
;

proc sql;
select Salary, Salary*.10 label='Bonus'
from WORK.ONE;
quit;

