data temp1;
set sashelp.cars(obs=1);
run;

proc sql;
select make into:CarMaker
from temp1;
quit;

%put &CarMaker.;
