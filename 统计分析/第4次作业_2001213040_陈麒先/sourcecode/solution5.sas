data work.first;
input common $ x;
datalines;
A            10
A            13
A            14
B            9

;

data work.second;
input common $ y;
datalines;
A             1
A             3
B             4
B             2
A             5
;

proc sql;
data WORK.COM;
set WORK.FIRST;
set WORK.SECOND;
run;
quit;

proc print data = work.com;
run;
