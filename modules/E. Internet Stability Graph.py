#Internet Stabiltiy Graph#

# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


from subprocess import run
from time import sleep
from matplotlib.pyplot import *
from datetime import datetime

start_h = int(datetime.now().strftime("%H"))
start_m = int(datetime.now().strftime("%M"))
start_s = int(datetime.now().strftime("%S"))

ion()

y = [0,0,0,0,0,0,0,0,0,0]
x = [0,0,0,0,0,0,0,0,0,0]

tmax = 0
tmin = 999999999
lmax = 0
lmin = 999999999
errors = 0
ta1k = []

fig,ax = subplots()
line, = ax.plot(x, y)

ax.set_xlabel("More than 1000 = Poor Connection   &    -1 = Network Error")
ax.set_ylabel("Latency (ms)")
fig.canvas.manager.set_window_title("Internet Stability Graph")


def close(event):
    cmd = open("shell_temp_folder.sh","w")	# Open shell script with write permissions
    cmd.write(' '.join(["  **Overview**","\n",
                        "\n","\n",
                        "	Totals:","\n",
                        "Total minimum:",str(tmin)+"ms","on iteration",str(tminloc),"\n",
                        "Total maximum:",str(tmax)+"ms","on iteration",str(tmaxloc),"\n",
                        "Total iterations:",str((x)[0]),"\n",
                        "\n","\n",
                        "	Locals:","\n",
                        "Local minimum before exit:",str(lmin)+"ms","\n",
                        "Local maximum before exit:",str(lmax)+"ms","\n",
                        "Local average before exit:",str(lavg)+"ms","\n",
                        "\n","\n",
                        "	Other:","\n",
                        "Last range before exit:",str(y),"\n",
                        "Iterations above 1000:",str(ta1k),"("+str(len(ta1k)),"iterations)","\n",
                        "Connection Errors:",str(errors),"\n",
                        "\n","\n",
                        "	Timestamps:","\n",
                        "Start Time:",str(start_h)+":"+str(start_m)+":"+str(start_s),"\n",
                        "End Time:",datetime.now().strftime("%H:%M:%S"),"\n",
                        "Runtime:",str(int(datetime.now().strftime("%H"))-start_h),"hours",str(int(datetime.now().strftime("%M"))-start_m),"minutes and",str(int(datetime.now().strftime("%S"))-start_s),"seconds","\n"
                        ]))
    cmd.close()
    run('gnome-terminal -- python3 ~/simple-linux-utility-and-toolbox/home.py && exit', shell=True) # Launch edited shell script in terminal
    run('gnome-terminal -- xed ~/simple-linux-utility-and-toolbox/shell_temp_folder.sh', shell=True) # Launch edited shell script in terminal
    exit()
fig.canvas.mpl_connect('close_event', close) 
 

while True:
    result = str(run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True).stdout)
    if (result == "") or ("100% packet loss" in result):
        
        #fix issue of sending multiple errors if internet disconnects
        y[9] = y[8]
        y[8] = y[7]
        y[7] = y[6]
        y[6] = y[5]
        y[5] = y[4]
        y[4] = y[3]
        y[3] = y[2]
        y[2] = y[1]
        y[1] = y[0]
        y[0] = -1
        errors += 1

    else:
        for letter in range(len(result)):
            if (result[letter] == "=") and (result[letter -1] == "e"):
                loc1 = letter + 1
                
        for letter in range(len(result)):
            if (result[letter] == "m") and (result[letter +1] == "s"):
                loc2 = letter
                break
                
        packet_drop = float(result[loc1:loc2])
        
        y[9] = y[8]
        y[8] = y[7]
        y[7] = y[6]
        y[6] = y[5]
        y[5] = y[4]
        y[4] = y[3]
        y[3] = y[2]
        y[2] = y[1]
        y[1] = y[0]
        y[0] = packet_drop
        
        x[9] = x[8]
        x[8] = x[7]
        x[7] = x[6]
        x[6] = x[5]
        x[5] = x[4]
        x[4] = x[3]
        x[3] = x[2]
        x[2] = x[1]
        x[1] = x[0]
        x[0] += 1
        
        if y[0] > tmax:
            tmax = y[0]
            tmaxloc = " ".join([str(x[0]),"("+str(datetime.now().strftime("%H:%M:%S"))+")"])
            
        if y[0] < tmin:
            if y[0] != -1:
                tmin = y[0]
                tminloc = " ".join([str(x[0]),"("+str(datetime.now().strftime("%H:%M:%S"))+")"])
                
        if y[0] >= 1000:
             ta1k.append(y[0])
        
        if (errors != 0) and (len(ta1k) != 0):
            if (errors == 1) and (len(ta1k) == 1):
                ax.set_xlabel("".join(["More than 1000 = Poor Connection ","(",str(len(ta1k))," peak)","    &    -1 = Network Error ","(",str(errors)," error)"]))
            elif (errors != 1) and (len(ta1k) == 1):
                ax.set_xlabel("".join(["More than 1000 = Poor Connection ","(",str(len(ta1k))," peak)","    &    -1 = Network Error ","(",str(errors)," errors)"]))

            elif (errors == 1) and (len(ta1k) != 1):
                ax.set_xlabel("".join(["More than 1000 = Poor Connection ","(",str(len(ta1k))," peaks)","    &    -1 = Network Error ","(",str(errors)," error)"]))
            else: 
                ax.set_xlabel("".join(["More than 1000 = Poor Connection ","(",str(len(ta1k))," peaks)","    &    -1 = Network Error ","(",str(errors)," errors)"]))
            
                
        lmin = min(y)
        lmax = max(y)
        lavg = round(sum(y)/len(y),1)
        title = ''.join(["Total Min: ",str(tmin)," | Total Max: ",str(tmax)," | Latest Val: ",str(y[0]),"\n",
                         "Local Min: ",str(lmin)," | Local Max: ",str(lmax)," | Local Avg: ",str(lavg)])
 
        
        line.set_xdata(x)
        line.set_ydata(y)
        ax.relim()
        ax.autoscale_view()
        draw()
        pause(0.001)
        
        ax.set_title(title)
        
    
    sleep(0.5)


        
