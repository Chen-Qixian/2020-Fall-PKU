data work.class1;
input name $ course $;
datalines;
Lauren  MATH1
Patel     MATH1
Chang   MATH1
Chang   MATH3
;

data work.class2;
input name $ class $;
datalines;
Smith    MATH2
Farmer  MATH2
Patel     MATH2
Hillier   MATH2
;

proc sql;
select Name
from WORK.CLASS1
except all
select Name
from WORK.CLASS2;
quit;