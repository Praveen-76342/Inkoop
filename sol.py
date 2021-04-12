import csv
state=input('What is the state: ')
filterType=input('Cost or Rating: ')
operation=input('Operation: ')
cost=int(0)
rating=0
hotelCode=""
with open('hotels.csv',mode='r') as file:
	csvFile=csv.reader(file,delimiter=',')
	if(filterType.lower()=="cost"):
		if(operation.lower()=="highest"):
			cost=int(0)
			lineNum=int(0)
			i=int(0)
			for row in csvFile:
				if(lineNum!=0 and row[2].lower()==state.lower()):
					if(cost<int(row[3])):
						hotelCode=row[1]
						cost=int(row[3])
				lineNum+=1
			print("Hotel with highest price in "+state+" is "+ hotelCode+ " with price "+str(cost))
		if(operation.lower()=="cheapest"):
			cost=int(9999999)
			lineNum=int(0)
			i=int(0)
			for row in csvFile:
				if(lineNum!=0 and row[2].lower()==state.lower()):
					if(cost>int(row[3])):
						hotelCode=row[1]
						cost=int(row[3])
				lineNum+=1
			print("Hotel with cheapest price in "+state+" is "+ hotelCode+ " with price "+str(cost))
		if(operation.lower()=="average"):
			total=int(0)
			lineNum=int(0)
			num=int(0)
			for row in csvFile:
				if(lineNum!=0 and row[2].lower()==state.lower()):
					total+=int(row[3])
					num+=1
				lineNum+=1
			print("Average cost in "+state+" is "+ str(total/num))
	if(filterType.lower()=="rating"):
		if(operation.lower()=="highest"):
			cost=float(0)
			lineNum=int(0)
			for row in csvFile:
				if(lineNum!=0 and row[2].lower()==state.lower()):
					if(cost<float(row[4])):
						hotelCode=row[1]
						cost=float(row[4])
				lineNum+=1
			print("Hotel with highest rating in "+state+" is "+ hotelCode+ " with rating "+str(cost))
		if(operation.lower()=="cheapest"):
			cost=float(9999999)
			lineNum=int(0)
			for row in csvFile:
				if(lineNum!=0 and row[2].lower()==state.lower()):
					if(cost>float(row[4])):
						hotelCode=row[1]
						cost=float(row[4])
				lineNum+=1
			print("Hotel with cheapest rating in "+state+" is "+ hotelCode+ " with rating "+str(cost))
		if(operation.lower()=="average"):
			total=float(0)
			lineNum=int(0)
			num=int(0)
			for row in csvFile:
				if(lineNum!=0 and row[2].lower()==state.lower()):
					total+=float(row[4])
					num+=1
				lineNum+=1
			print("Average rating in "+state+" is "+ str(total/num))				