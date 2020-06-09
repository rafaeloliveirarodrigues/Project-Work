############################################
#	Author: Rafael Rodrigues	   #
#	Professor:			   #
#	Course:				   #
#	Uni:				   #
############################################

import roslib
roslib.load_manifest('joint_states_listener')
import rospy
import time
import sys
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from std_msgs.msg import String
from joint_states_listener.srv import ReturnJointStates
#python2 for python 3 use just tkinter
from Tkinter import *
import Tkinter as tkinter

#################################################
#		Main window Defeniton		#
#						#
#################################################



window = tkinter.Tk()
window.title("Arm Controller ")
window.geometry("400x700")

# icon not working window.wm_iconbitmap('/home/rr/favicon.ico')



#################################################
#	Joint State 				#
#	Method for calling service		#
#	Define	Joints from the service		#
#	Getting the position			#
#	Print Position to the list		#
#################################################


def call_return_joint_states(joint_names):
    rospy.wait_for_service("return_joint_states")
    try:
        s = rospy.ServiceProxy("return_joint_states", ReturnJointStates)
        resp = s(joint_names)
    except rospy.ServiceException, e:
        print "error when calling return_joint_states: %s"%e
        sys.exit(1)
    for (ind, joint_name) in enumerate(joint_names):
        if(not resp.found[ind]):
            print "joint %s not found!"%joint_name
    return (resp.position, resp.velocity, resp.effort)


#pretty-print list to string
def pplist(list):
    return ' '.join(['%2.2f'%x for x in list])


if __name__ == "__main__":
    joint1 = ["joint1"]
    joint2 = ["joint2"]
    joint3 = ["joint3"]
    joint4 = ["joint4"]
        
def print1act():
	(position, velocity, effort) = call_return_joint_states(joint1)	
	mylist.insert(END, 'Joint 1 position: ' + str(pplist(position)))
	mylist.see(END)
	

def print2act():
	(position, velocity, effort) = call_return_joint_states(joint2)	
	mylist.insert(END, 'Joint 2 position: ' + str(pplist(position)))
	mylist.see(END)
	
	
def print3act():
	(position, velocity, effort) = call_return_joint_states(joint3)	
	mylist.insert(END, 'Joint 3 position: ' + str(pplist(position)))
	mylist.see(END)
	

def print4act():
	(position, velocity, effort) = call_return_joint_states(joint4)	
	mylist.insert(END, 'Joint 4 position: ' + str(pplist(position)))
	mylist.see(END)
	
def printall():
	print1act()
	print2act()
	print3act()
	print4act()

#################################################
#		First Joint 			#
#	Define Label 				#
#	Define Scale				#
#	Define Method that send entry value	#
#	to the Joint				#
#	Define the Submit button		#
#################################################

lbl1 = tkinter.Label(window, text='Joint 1 (-2.83 2.83)')
lbl1.pack()

#first entry if you need free input source
#ent1 = tkinter.Entry(window)
#ent1.pack()

sj1 = tkinter.Scale(window, from_=-2.83, to=2.83, digits=3 ,resolution=0.01, orient=HORIZONTAL) 
sj1.pack() 


def joint1send():
	pub = rospy.Publisher('/om_with_tb3/joint1_position/command', Float64, queue_size=10)
    	rospy.init_node('talker', anonymous=True)	
       	j1_str = float( sj1.get())
       	pub.publish(j1_str)  
	mylist.insert(END, 'Joint 1 Sended: '+  str(j1_str)) 
	mylist.see(END)
	
btn1 = tkinter.Button(window, text='GO J1',command=joint1send)
btn1.pack()

#################################################
#		Second Joint 			#
#	Define Label 				#
#	Define Entry				#
#	Define Method that send entry value	#
#	to the Joint				#
#	Define the Submit button		#
#################################################

#Second label
lbl2 = tkinter.Label(window, text='Joint 2 (-1.79 1.57)')
lbl2.pack()

sj2 = tkinter.Scale(window, from_=-1.79, to=1.57, digits=3 ,resolution=0.01, orient=HORIZONTAL) 
sj2.pack() 


def joint2send():
	
	pub = rospy.Publisher('/om_with_tb3/joint2_position/command', Float64, queue_size=10)
    	rospy.init_node('talker', anonymous=True) #possible not needed but can be the first in used	
       	j2_str = float( sj2.get())
       	pub.publish(j2_str)  
	mylist.insert(END, 'Joint 2 Sended: '+  str(j2_str))  
	mylist.see(END)
	
# Submit joint 2
btn2 = tkinter.Button(window, text='GO J2',command=joint2send)
btn2.pack()


#################################################
#		Third Joint 			#
#	Define Label 				#
#	Define Entry				#
#	Define Method that send entry value	#
#	to the Joint				#
#	Define the Submit button		#
#################################################

lbl3 = tkinter.Label(window, text='Joint 3 (-0.94 1.38)')
lbl3.pack()

sj3 = tkinter.Scale(window, from_=-0.94, to=1.38, digits=3 ,resolution=0.01, orient=HORIZONTAL) 
sj3.pack() 

def joint3send():
	
	pub = rospy.Publisher('/om_with_tb3/joint3_position/command', Float64, queue_size=10)
    	rospy.init_node('talker', anonymous=True)	
       	j3_str = float( sj3.get())
       	pub.publish(j3_str)   
	mylist.insert(END, 'Joint 3 Sended: '+  str(j3_str))  
	mylist.see(END)

btn3 = tkinter.Button(window, text='GO J3',command=joint3send)
btn3.pack()



#################################################
#		Fourth Joint 			#
#	Define Label 				#
#	Define Entry				#
#	Define Method that send entry value	#
#	to the Joint				#
#	Define the Submit button		#
#################################################


lbl4 = tkinter.Label(window, text='Joint 4 (-1.79 2.04)')
lbl4.pack()

sj4 = tkinter.Scale(window, from_=-1.79, to=2.04, digits=3 ,resolution=0.01, orient=HORIZONTAL) 
sj4.pack() 

def joint4send():
	
	pub = rospy.Publisher('/om_with_tb3/joint4_position/command', Float64, queue_size=10)
    	rospy.init_node('talker', anonymous=True)	
       	j4_str = float( sj4.get())
       	pub.publish(j4_str) 
	mylist.insert(END, 'Joint 4 Sended: '+  str(j4_str))  
	mylist.see(END)  
	
	
btn4 = tkinter.Button(window, text='GO J4',command=joint4send)
btn4.pack()



#################################################
#		 Gripper Button			#
#	Send Comand Gripper open/close		#
#################################################
lbl5 = tkinter.Label(window, text='')
lbl5.pack()

def update_btn_text():
	global b 
	btn5_text.set("G Open")	
	pub = rospy.Publisher('/om_with_tb3/gripper_position/command', Float64, queue_size=10)
    	rospy.init_node('talker', anonymous=True)	
       	gripper_str = float(-0.01)
       	pub.publish(gripper_str)
	mylist.insert(END, 'Gripper sended: Close '+  str(gripper_str)) 
	mylist.see(END)
	
	b+=1
	if b%2 :
	  btn5_text.set("G Close")
	  pub = rospy.Publisher('/om_with_tb3/gripper_position/command', Float64, queue_size=10)
    	  rospy.init_node('talker', anonymous=True)	
       	  gripper_str = float(0.01)
       	  pub.publish(gripper_str)	
	  mylist.insert(END, 'Gripper sended: Open' + str(gripper_str)) 
       	  mylist.see(END) 

	

b=1
btn5_text = tkinter.StringVar()
btn5 = tkinter.Button(window, textvariable=btn5_text, command=update_btn_text)
btn5_text.set("G Close")
btn5.pack()


#################################################
#		 Home Button			#
#	Send All Joints to 0 Position 		#
#################################################
def Home():
	pub = rospy.Publisher('/om_with_tb3/joint1_position/command', Float64, queue_size=10)
    	rospy.init_node('talker', anonymous=True)	
       	hello_str = float(0)
       	pub.publish(hello_str) 
	pub = rospy.Publisher('/om_with_tb3/joint2_position/command', Float64, queue_size=10)
	rospy.init_node('talker', anonymous=True)    	
	pub.publish(hello_str) 
	pub = rospy.Publisher('/om_with_tb3/joint3_position/command', Float64, queue_size=10)
	rospy.init_node('talker', anonymous=True)       	
	pub.publish(hello_str) 
	pub = rospy.Publisher('/om_with_tb3/joint4_position/command', Float64, queue_size=10)
       	pub.publish(hello_str) 



btn6 = tkinter.Button(window, text='Home',command=Home).place(x=10,y=660)




#################################################
#		 ALL Button			#
#	Send All Joints to X Position 		#
#################################################
def All():
	joint1send()
	joint2send()
	joint3send()
	joint4send()

	
btn7 = tkinter.Button(window, text='Go All',command=All).place(x=320,y=660)




#################################################
#		Scroll Bar			#
#	Define scroll bar and list		#
#################################################


scrollbar = tkinter.Scrollbar(window) 
scrollbar.pack(side = RIGHT) 
mylist = Listbox(window, yscrollcommand = scrollbar.set ) 
for line in range(1): 
   mylist.insert(END, 'This is line number' + str(line)) 
   mylist.see(END)
mylist.pack(fill= X ) 
scrollbar.config( command = mylist.yview ) 

def a (c):
	mylist.insert(END, 'This is line number' + str(c))
	
#################################################
#			 Menu			#
#		    Joint  Position		#
#################################################
menubar = tkinter.Menu(window)
jointmenu = tkinter.Menu(menubar, tearoff=0)
jointmenu.add_command(label="Joint1" , command=print1act)
jointmenu.add_command(label="Joint2" , command= print2act)
jointmenu.add_command(label="Joint3" , command= print3act)
jointmenu.add_command(label="Joint4" , command= print4act)
jointmenu.add_command(label="All Joint" , command= printall)

menubar.add_cascade(label="Joint Status", menu=jointmenu)
window.config(menu=menubar)


"""
Not in use but can be useful

m1 = tkinter.PanedWindow() 
m1.pack(fill = BOTH, expand = 1) 
left = Entry(m1, bd = 5) 
m1.add(left) 
m2 = tkinter.PanedWindow(m1, orient = VERTICAL) 
m1.add(m2) 
top = tkinter.Scale( m2, orient = HORIZONTAL) 
m2.add(top) 
"""
window.mainloop()

		
