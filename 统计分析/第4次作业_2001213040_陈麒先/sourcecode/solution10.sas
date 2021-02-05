data work.SQL01;
set sashelp.cars;

proc sql;
select make, avg(MPG_City) label='AvgCityMPG'
from work.SQL01
group by make;
quit;
