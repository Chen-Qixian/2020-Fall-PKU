data concrete;
    infile datalines dsd dlm=' ';
    input Brand : $12. Additive : $10. Strength;
datalines;
Graystone reinforced 32.6
Graystone reinforced 31.5
Graystone reinforced 30.0
Graystone standard 29.8
Graystone reinforced 29.7
Graystone reinforced 29.5
Consolidated reinforced 29.3
"EZ Mix" reinforced 30.2
"EZ Mix" reinforced 28.2
"EZ Mix" standard 28.0
"EZ Mix" standard 28.0
"EZ Mix" reinforced 26.7
Graystone standard 26.4
Consolidated reinforced 26.3
"EZ Mix" reinforced 25.7
"EZ Mix" reinforced 25.5
Consolidated reinforced 25.4
Consolidated reinforced 25.3
"EZ Mix" standard 24.9
Graystone standard 24.6
Graystone standard 24.4
Consolidated standard 24.2
Consolidated standard 23.9
Consolidated reinforced 22.7
Consolidated standard 22.4
Consolidated standard 22.1
"EZ Mix" standard 21.3
Graystone standard 21.2
Consolidated standard 20.4
"EZ Mix" standard 19.8
;
run;
proc means data=concrete;
class brand additive;
var strength;
run;
proc glm data=concrete;
class additive brand;
model Strength=additive brand/ ss3 singular=1e-07;
lsmeans additive brand / adjust=tukey;
run;
