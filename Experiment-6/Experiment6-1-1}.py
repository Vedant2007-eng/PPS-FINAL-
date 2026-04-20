Date = int(input())
Month = int(input())
Year = int(input())
flag = True 
if Year < 0 or Month < 0 or Month > 12 :
	flag = False 
if Month in (1,3,5,7,8,10,12) :
	Maxday = 31
elif Month in (4,6,9,11) :
	Maxday = 30
else :
	if (Year % 4 == 0 ) :
		Maxday = 29
	else :
		Maxday = 28
if Date > Maxday :
	flag = False
Date = Date + 1
if Date > Maxday :
	Date = 1
	Month = Month + 1
if Month > 12 :
	Month = 1
	Year = Year + 1
if flag :
	print(f"{Date:02d}-{Month:02d}-{Year:02d}")
else :
	print("Invalid Date")
