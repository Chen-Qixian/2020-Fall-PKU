data NormTemp;
    input @1 ID 3. @5 BodyTemp 5.1 @11 Gender $6. @18 HeartRate 3.;
    datalines;
  1  96.3 Male    70
  2  96.7 Male    71
  3  96.9 Male    74
  4  97.0 Male    80
  5  97.1 Male    73
  6  97.1 Male    75
  7  97.1 Male    82
  8  97.2 Male    64
  9  97.3 Male    69
 10  97.4 Male    70
 11  97.4 Male    68
 12  97.4 Male    72
 13  97.4 Male    78
 14  97.5 Male    70
 15  97.5 Male    75
 16  97.6 Male    74
 17  97.6 Male    69
 18  97.6 Male    73
 19  97.7 Male    77
 20  97.8 Male    58
 21  97.8 Male    73
 22  97.8 Male    65
 23  97.8 Male    74
 24  97.9 Male    76
 25  97.9 Male    72
 26  98.0 Male    78
 27  98.0 Male    71
 28  98.0 Male    74
 29  98.0 Male    67
 30  98.0 Male    64
 31  98.0 Male    78
 32  98.1 Male    73
 33  98.1 Male    67
 34  98.2 Male    66
 35  98.2 Male    64
 36  98.2 Male    71
 37  98.2 Male    72
 38  98.3 Male    86
 39  98.3 Male    72
 40  98.4 Male    68
 41  98.4 Male    70
 42  98.4 Male    82
 43  98.4 Male    84
 44  98.5 Male    68
 45  98.5 Male    71
 46  98.6 Male    77
 47  98.6 Male    78
 48  98.6 Male    83
 49  98.6 Male    66
 50  98.6 Male    70
 51  98.6 Male    82
 52  98.7 Male    73
 53  98.7 Male    78
 54  98.8 Male    78
 55  98.8 Male    81
 56  98.8 Male    78
 57  98.9 Male    80
 58  99.0 Male    75
 59  99.0 Male    79
 60  99.0 Male    81
 61  99.1 Male    71
 62  99.2 Male    83
 63  99.3 Male    63
 64  99.4 Male    70
 65  99.5 Male    75
 66  96.4 Female  69
 67  96.7 Female  62
 68  96.8 Female  75
 69  97.2 Female  66
 70  97.2 Female  68
 71  97.4 Female  57
 72  97.6 Female  61
 73  97.7 Female  84
 74  97.7 Female  61
 75  97.8 Female  77
 76  97.8 Female  62
 77  97.8 Female  71
 78  97.9 Female  68
 79  97.9 Female  69
 80  97.9 Female  79
 81  98.0 Female  76
 82  98.0 Female  87
 83  98.0 Female  78
 84  98.0 Female  73
 85  98.0 Female  89
 86  98.1 Female  81
 87  98.2 Female  73
 88  98.2 Female  64
 89  98.2 Female  65
 90  98.2 Female  73
 91  98.2 Female  69
 92  98.2 Female  57
 93  98.3 Female  79
 94  98.3 Female  78
 95  98.3 Female  80
 96  98.4 Female  79
 97  98.4 Female  81
 98  98.4 Female  73
 99  98.4 Female  74
100  98.4 Female  84
101  98.5 Female  83
102  98.6 Female  82
103  98.6 Female  85
104  98.6 Female  86
105  98.6 Female  77
106  98.7 Female  72
107  98.7 Female  79
108  98.7 Female  59
109  98.7 Female  64
110  98.7 Female  65
111  98.7 Female  82
112  98.8 Female  64
113  98.8 Female  70
114  98.8 Female  83
115  98.8 Female  89
116  98.8 Female  69
117  98.8 Female  73
118  98.8 Female  84
119  98.9 Female  76
120  99.0 Female  79
121  99.0 Female  81
122  99.1 Female  80
123  99.1 Female  74
124  99.2 Female  77
125  99.2 Female  66
126  99.3 Female  68
127  99.4 Female  77
128  99.9 Female  79
129 100.0 Female  78
130 100.8 Female  77
;
ods pdf
	file='~/sasuser.v94/problem1.pdf'
	style=EGDefault;
proc univariate data=NormTemp;
var BodyTemp;
histogram BodyTemp 
/
normal(
mu = est
sigma = est
color = red
w = 3
noprint);
run;

proc ttest data=NormTemp alpha=0.05 h0=98.6 plots(shownull)=interval;
	var BodyTemp;
run;

ods pdf close;

