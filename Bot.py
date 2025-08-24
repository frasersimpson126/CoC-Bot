import time as t
import customtkinter as ctk
import func as f
import threading
import attacks as a

trophiebypass = False
attacktype = "Sdrag"

p = '5554' # port
bot_thread = None
bot_running = threading.Event()


def start_bot():
    global bot_thread
    if not bot_running.is_set():
        bot_thread = threading.Thread(target=Bot, daemon=True)
        bot_thread.start()
        log("Bot started.")

def stop_bot():
    bot_running.clear()
    log("Stopping bot...")




def Bot():
    bot_running.set()
    f.checktrophies(p)
    log(f.checktrophies.result[0] + " Trophies") 

    while bot_running.is_set():
        while bot_running.is_set() and int(f.checktrophies.result[0]) < 4968 or trophiebypass == True:
            f.find(p)
            t.sleep(6)
            f.checkloot(p)
            while int(f.checkloot.result[0]) + int(f.checkloot.result[1]) < 1000000 and bot_running.is_set():
                log("base found: " +  format(int(f.checkloot.result[0]), ",") + " Gold   " + format(int(f.checkloot.result[1]), ",") + " Elixer   " +  format(int(f.checkloot.result[2]), ",") + " Dark elixer")
                f.next(p)
                t.sleep(6)
                f.checkloot(p)

            if bot_running.is_set():
                log("base found: " +  format(int(f.checkloot.result[0]), ",") + " Gold   " + format(int(f.checkloot.result[1]), ",") + " Elixer   " +  format(int(f.checkloot.result[2]), ",") + " Dark elixer")
                log("going to attack")
                attak = getattr(a, attacktype)
                attak()
                t.sleep(25)
            else:
                return
                
            while f.checkpixel(p) == False and bot_running.is_set():
                f.checkpixel(p)
                t.sleep(2)

            if bot_running.is_set():
                log("returning")
                t.sleep(2)
                f.tap(900,910,p)
                t.sleep(5)
                f.checktrophies(p)
                log(f.checktrophies.result[0] + " Trophies") 
            else:
                return
        if bot_running.is_set():       
            log("dropping Trophies")
            for x in range(0,3):
                a.droptrophies()
                t.sleep(4)

            t.sleep(7)
            f.checktrophies(p)
            t.sleep(1)
            log(f.checktrophies.result[0] + " Trophies") 


# Create main window
App = ctk.CTk()        
App.title("CoC Bot Main")
App.geometry("700x400")  # Wider window to accommodate loot display

# Button frame
App.button_frame = ctk.CTkFrame(App)
App.button_frame.pack(pady=10)
        
App.button2 = ctk.CTkButton(App.button_frame, text="Start Bot", command=start_bot)
App.button2.grid(row=0, column=0, padx=5)
        
App.button3 = ctk.CTkButton(App.button_frame, text="Stop Bot", command=stop_bot)
App.button3.grid(row=0, column=1, padx=5)

# Main content frame
App.content_frame = ctk.CTkFrame(App)
App.content_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Log textbox
App.log_textbox = ctk.CTkTextbox(App.content_frame, height=200, wrap="word")
App.log_textbox.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

# Configure grid weights
App.content_frame.columnconfigure(0, weight=3)

App.content_frame.rowconfigure(0, weight=1)

def log(message):
    textbox = App.log_textbox._textbox
    textbox.tag_configure("spacing", spacing3=8)
    textbox.insert("end", message + "\n", "spacing")
    textbox.see("end")


App.mainloop()