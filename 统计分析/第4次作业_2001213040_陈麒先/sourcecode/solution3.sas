data work.math1a;
input name $ fi $;
datalines;
Lauren   L         
Patel     A          
Chang    Z      
Hillier    R
;

data work.math1b;
input name $ fi $;
datalines;
Smith    M
Lauren   L
Patel     A
;

proc sql;
select *
from WORK.MATH1A
outer union corr
select *
from WORK.MATH1B;
quit; 

