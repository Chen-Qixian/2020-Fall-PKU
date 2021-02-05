proc reg data = WORK.HOUSE_PRICE;
	model SalePrice = MSSubClass--SaleCondition_Partial
	/selection=stepwise slstay=0.05 slentry=0.15;
run;  