data work.one;
input year qtr budget;
datalines;
2001   3     500
2001   4     400
2003   1     350
;

data work.two;
input year qtr sales;
datalines;
2001   4     300
2002   1     600
;

proc sql;
select TWO.*, budget
from WORK.ONE full join WORK.TWO
on ONE.Year=TWO.Year;
quit;

