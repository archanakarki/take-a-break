import time
import webbrowser

my_url = "https://www.youtube.com/watch?v=xdcIwXC_Ouk"
seconds_in_one_hour = 60 * 60
number_of_hour = 2
waiting_time = seconds_in_one_hour * number_of_hour

#Reminding after every two hours
total_breaks_count = 10
number_of_breaks_taken = 0

print("The program has started on " + time.ctime())
while (number_of_breaks_taken < total_breaks_count) :
    time.sleep(waiting_time)
    webbrowser.open(my_url)
    number_of_breaks_taken += 1