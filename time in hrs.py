minutes=int(input("Enter the time in minutes"))
if(minutes<60):
  print("The time in hours is","0 hrs and",minutes,"mins")
else:
  hr=int(minutes/60)
  mn=minutes%60
  print("The time in hours is",hr,"hrs and",mn,"mins")
