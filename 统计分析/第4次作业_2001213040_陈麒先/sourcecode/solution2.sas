data work.one;
	input rep $ cost;
	datalines;
	SMITH       200
	SMITH       400
	JONES       100
	SMITH       600
	JONES       100
	;

	proc sql;
	select Rep, avg(Cost)
	from WORK.ONE
	order by Rep;
	quit;