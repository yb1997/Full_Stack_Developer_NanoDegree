import time
import webbrowser

break_count = 0
total_breaks = 3
print("The program started on: "+ time.ctime() )
while(total_breaks > break_count ) :
   time.sleep(10) # this time is in seconds
   webbrowser.open("https://www.youtube.com/watch?v=0NMPt7K9ZRs")
   break_count = break_count + 1
