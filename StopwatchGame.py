import simplegui

tick_count = 0
stops = 0
successful_stops = 0
timer_running = False
D = 0

def format(t):
    """converts time in tenths of seconds 
    into formatted string A:BC.D"""
    global D
    D = t%10
    C = (t // 10) % 10
    B = (t // 100) % 6
    A = (t // 100) // 6
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
   
def start():
    """starts timer, sets timer_running to true"""
    global timer_running
    timer_running = True
    timer.start()

def stop():
    """checks timer status, stops timer 
    and sets global variables"""
    global D
    global timer_running
    global stops
    global successful_stops
    if timer_running:
        timer.stop()
        timer_running = False
        stops += 1
        if D == 0:
            successful_stops += 1

def reset():
    """resets score and timer"""
    global tick_count
    global stops
    global successful_stops
    timer.stop()
    tick_count = 0
    stops = 0
    successful_stops = 0

def increment():
    """increments tick count on each tick"""
    global tick_count
    tick_count += 1

def draw(canvas):
    """draws elements on canvas"""
    canvas.draw_text((format(tick_count)), [92, 90], 48, "White")
    canvas.draw_text(str(successful_stops), [220, 30], 24, "White")
    canvas.draw_text(str(stops), [270, 30], 24, "White")
    canvas.draw_text("/", [248, 30], 24, "White")
    
timer = simplegui.create_timer(100, increment)
frame = simplegui.create_frame("Stopwatch: The Game", 300, 150)

frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.start()