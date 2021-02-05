
data VIOLENTCRIME;
	set '/folders/myfolders/Lesson_8_violentcrime.sas7bdat';
run;

proc timeseries data=VIOLENTCRIME plots=(series tc sc); 
  id Date interval=month; 
  var MurdersTX; 
  decomp tc sc / mode=multoradd;
run;  
