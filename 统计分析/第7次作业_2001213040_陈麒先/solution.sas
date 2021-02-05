data Safety;
     input @1 Unsafe 1. @3 Size 1. @5 Weight 2. @8 Region $9. @18 Type $13.;
datalines;
0 2  3 N America Medium
0 3  4 N America Sport/Utility
0 2  3 N America Medium
0 1  3 N America Small
0 2  3 N America Medium
0 2  3 N America Medium
0 3  4 N America Sport/Utility
0 2  3 Asia      Medium
0 2  4 N America Medium
0 1  3 N America Small
1 1  3 N America Small
0 1  3 Asia      Small
0 2  3 N America Medium
0 2  3 N America Medium
0 2  3 N America Medium
0 3  3 N America Large
0 3  4 N America Large
0 3  4 N America Large
0 3  4 N America Large
0 3  4 N America Large
1 1  3 N America Small
1 2  3 N America Medium
1 2  3 N America Medium
0 3  4 N America Large
1 1  3 N America Sports
0 1  3 N America Sports
0 3  6 N America Sport/Utility
0 3  4 N America Large
0 3  4 N America Large
0 3  3 N America Large
0 1  3 N America Small
1 1  2 N America Small
0 3  4 N America Large
1 1  3 N America Sports
1 1  3 N America Small
0 3  4 N America Large
1 1  3 N America Sports
1 1  3 N America Sports
0 3  1 N America Sport/Utility
0 3  5 N America Sport/Utility
0 3  6 N America Sport/Utility
0 3  5 N America Sport/Utility
1 1  3 N America Small
1 1  2 N America Small
1 3  3 N America Sport/Utility
1 1  2 Asia      Small
0 2  3 Asia      Medium
1 1  3 Asia      Sports
1 1  2 Asia      Sports
0 3  4 Asia      Sport/Utility
0 2  3 Asia      Medium
0 2  4 Asia      Medium
0 3  4 Asia      Sport/Utility
0 3  4 Asia      Sport/Utility
0 3  4 N America Sport/Utility
0 3  3 N America Sport/Utility
0 3  3 N America Sport/Utility
0 2  3 Asia      Medium
0 3  4 N America Large
1 1  3 Asia      Small
0 2  3 Asia      Medium
0 1  2 Asia      Sports
0 1  3 Asia      Sports
1 1  3 N America Small
0 2  3 N America Medium
0 3  4 N America Large
1 1  2 Asia      Small
0 2  4 Asia      Medium
1 2  3 Asia      Medium
0 1  4 Asia      Sports
1 1  3 Asia      Sports
1 1  3 Asia      Small
0 2  3 Asia      Medium
1 2  3 Asia      Medium
0 1  4 Asia      Sports
0 2  3 N America Medium
0 2  3 N America Medium
0 2  3 N America Medium
0 3  3 N America Large
0 3  4 N America Large
0 2  3 N America Medium
0 2  4 N America Medium
0 3  4 N America Large
1 1  4 N America Sports
0 1  2 N America Small
0 1  2 N America Sports
0 1  2 Asia      Small
0 2  3 Asia      Medium
1 1  2 Asia      Small
1 3  3 Asia      Sport/Utility
1 1  2 Asia      Small
1 1  3 Asia      Small
0 2  3 Asia      Medium
1 2  3 Asia      Medium
1 1  3 Asia      Sports
0 3  5 Asia      Sport/Utility
;
run;
proc means data=Safety;
var weight;
run;
proc logistic data=Safety descending plots=all;
model Unsafe=Weight;
run;
