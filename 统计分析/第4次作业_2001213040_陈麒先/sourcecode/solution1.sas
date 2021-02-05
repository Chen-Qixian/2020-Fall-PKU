data work.transact;
	input rep $ cost ship;
	datalines;
	SMITH   200     50
	SMITH   400     20
	JONES   100     10
	SMITH   600    100
	JONES   100     5 
	;

proc sql;
	select Rep, min(Cost+Ship) 
	from WORK.TRANSACT
	group by Rep
	order by Rep;
quit;