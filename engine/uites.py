import tkinter as tk
from ..engine.pigtest import angler
import math

# State variable to track whether the arm is open or closed
arm_open = False

def plane(*args):
    """Update Servo 1 and Servo 2 angles together."""
    x = servo1_slider.get()
    y = servo2_slider.get()
    plana(x, y)
def plana(x,y,z=0):
    x=(x+2)
    y=(y)
    a=math.atan2(y,x)
    l=x/math.cos(a)
    print(l,math.degrees(a))
    update_servo0(math.degrees(a)*2)  # Update Servo 1\\
    if __name__ == "__main__":
        coord_Move(l, z)  # Update Servo 3 and Servo 4
    return l, math.degrees(a)
    #angler(int(angle2), 1)  # Update Servo 2

def coord_Move(x, y):
    """Update servo 3 angle using both sliders."""
    # Placeholder for servo 3 functionality
    y=y+5
    print(f"x, y coords: {x}, {y}")
    x=x/6
    y=y/6
    d = math.sqrt(x**2 + y**2)
    a = math.degrees(math.acos(d / 2))
    b = -2 * a
    g = a + math.degrees(math.atan2(y, x))
    print(203 - g)
    print(g + b + 100)
    #angler(203 - g, 2)
    angler(203-g,2,g+b+100,1)  # Example: Update servo 3 angle
    #angler(g + b + 100, 1)  # Example: Update servo 4 angle
    pass

def update_servo0(angle):
    """Update servo 0 angle."""
    angler(min(max(int(angle)+90,0),180),0)

def on_extra_slider_change(*args):
    """Handle changes in the extra sliders and pass values to coord_Move."""
    angle1 = servo3_slider.get()
    angle2 = servo4_slider.get()
    coord_Move(angle1, angle2)

def toggle_sliders():
    """Swap between the first two sliders and the extra sliders."""
    if main_sliders_frame.winfo_ismapped():
        main_sliders_frame.pack_forget()
        extra_sliders_frame.pack()
    else:
        extra_sliders_frame.pack_forget()
        main_sliders_frame.pack()

def toggle_arm():
    """Toggle the arm servo between open and closed states."""
    global arm_open
    if arm_open:
        print("Closing arm...")
        angler(10, 3)  # Example: Close the arm
    else:
        print("Opening arm...")
        angler(50, 3)  # Example: Open the arm
    arm_open = not arm_open
    #arm_toggle_button_main.config(text="Close Arm" if arm_open else "Open Arm")
    #arm_toggle_button_extra.config(text="Close Arm" if arm_open else "Open Arm")

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Servo Controller")

    # Frame for main sliders (Servo 1 and Servo 2)
    main_sliders_frame = tk.Frame(root)

    # Create a slider for Servo 1
    servo1_label = tk.Label(main_sliders_frame, text="distance")
    servo1_label.pack()
    servo1_slider = tk.Scale(main_sliders_frame, from_=0, to=7, orient=tk.HORIZONTAL, command=plane,resolution=0.01, length=800)
    servo1_slider.pack()

    # Create a slider for Servo 2
    servo2_label = tk.Label(main_sliders_frame, text="offset")
    servo2_label.pack()
    servo2_slider = tk.Scale(main_sliders_frame, from_=-4, to=4, orient=tk.HORIZONTAL, command=plane,resolution=0.01, length=800)
    servo2_slider.pack()

    # Create a slider for Servo 0 (visible on both screens)
    servo0_label_main = tk.Label(main_sliders_frame, text="Servo 0 Angle")
    servo0_label_main.pack()
    servo0_slider_main = tk.Scale(main_sliders_frame, from_=-90, to=90, orient=tk.HORIZONTAL, command=update_servo0, length=800)
    servo0_slider_main.pack()

    # Add a button to toggle the arm servo (visible on both screens)
    arm_toggle_button_main = tk.Button(main_sliders_frame, text="Open Arm", command=toggle_arm)
    arm_toggle_button_main.pack()

    # Frame for extra sliders (Servo 3 and Servo 4)
    extra_sliders_frame = tk.Frame(root)

    # Create a slider for Servo 3
    servo3_label = tk.Label(extra_sliders_frame, text="x axis")
    servo3_label.pack()
    servo3_slider = tk.Scale(extra_sliders_frame, from_=1, to=10, orient=tk.HORIZONTAL, resolution=0.01, length=800)
    servo3_slider.pack()

    # Create a slider for Servo 4
    servo4_label = tk.Label(extra_sliders_frame, text="y axis")
    servo4_label.pack()
    servo4_slider = tk.Scale(extra_sliders_frame, from_=-4, to=4, orient=tk.HORIZONTAL, resolution=0.01, length=800)
    servo4_slider.pack()

    # Create a slider for Servo 0 (visible on both screens)
    servo0_label_extra = tk.Label(extra_sliders_frame, text="Servo 0 Angle")
    servo0_label_extra.pack()
    servo0_slider_extra = tk.Scale(extra_sliders_frame, from_=-90, to=90, orient=tk.HORIZONTAL, command=update_servo0, length=800)
    servo0_slider_extra.pack()

    # Add a button to toggle the arm servo (visible on both screens)
    arm_toggle_button_extra = tk.Button(extra_sliders_frame, text="Open Arm", command=toggle_arm)
    arm_toggle_button_extra.pack()

    # Bind the extra sliders to the on_extra_slider_change function
    servo3_slider.config(command=lambda value: on_extra_slider_change())
    servo4_slider.config(command=lambda value: on_extra_slider_change())

    # Initially display the main sliders
    main_sliders_frame.pack()

    # Button to toggle between the two sets of sliders
    toggle_button = tk.Button(root, text="Swap Sliders", command=toggle_sliders)
    toggle_button.pack()

    # Run the Tkinter event loop
    root.mainloop()