import customtkinter as ctk

# Configure the appearance mode and theme
ctk.set_appearance_mode("Light")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

def refresh_state():
    global is_accelerating
    if is_accelerating == True:
        state_label.configure(text="Acelerando", text_color="#1e40af")
    else:
        state_label.configure(text="Detenido", text_color="#b91c1c")

def accelerate():
    global speed
    global is_accelerating
    is_accelerating = True
    refresh_state()
    
def brake():
    global speed
    global is_accelerating
    is_accelerating = False
    refresh_state()

def refresh_speed():
    global speed
    accelerate()
    speed_label.configure(text=f"Velocidad: {speed}%")

def increase_speed():
    global speed
    if speed >= 100:
        return
    speed += 10
    refresh_speed()
    
def decrease_speed():
    global speed
    if speed <= 0:
        return
    speed -= 10
    refresh_speed()
    
speed = 10

# Create the main application window
app = ctk.CTk()
app.title("VESCA")
app.geometry("1000x600")
app.configure(fg_color="#f8fafc")
app.grid_columnconfigure((0, 1), weight=1)

state_frame = ctk.CTkFrame(app, corner_radius=24, fg_color="#f1f5f9", border_width=1, border_color="#e2e8f0")
state_frame.grid(row=0, column=0, pady=64, sticky="en")

state_title = ctk.CTkLabel(state_frame, text="Estado del vehículo", font=("Roboto", 24, "bold"), text_color="#334155")
state_title.grid(row=0, column=0, padx=32, pady=32, sticky="ew")

speed_label = ctk.CTkLabel(state_frame, text=f"Velocidad: {speed}%", font=("Roboto", 20), text_color="#334155")
speed_label.grid(row=1, column=0, padx=32, pady=(0, 32), sticky="ew")

state_label = ctk.CTkLabel(state_frame, text=f"Detenido", font=("Roboto", 20, "bold"), text_color="#b91c1c")
state_label.grid(row=2, column=0, padx=32, pady=(0, 32), sticky="ew")

main_frame = ctk.CTkFrame(app, corner_radius=24, fg_color="#f1f5f9", border_width=1, border_color="#e2e8f0")
main_frame.grid(row=0, column=1, padx=32, pady=64, sticky="wn")

# Create a label with the title of the application
main_title = ctk.CTkLabel(main_frame, text="Controles para el VESCA", font=("Roboto", 24, "bold"), text_color="#334155")
main_title.grid(row=0, column=0, columnspan=2, padx=32, pady=32, sticky="ew")

# Function to handle button clicks
def button_click(button_id):
    print(f"Button {button_id} clicked!")

accelerator_button = ctk.CTkButton(main_frame, text="Acelerar", command=lambda: accelerate(), font=("Roboto", 20), width=150, height=85, corner_radius=16, text_color="#f8fafc", fg_color="#1e293b", )
accelerator_button.grid(row=1, column=0, padx=(32, 8), pady=(0, 16))

brake_button = ctk.CTkButton(main_frame, text="Frenar", command=lambda: brake(), font=("Roboto", 20), width=150, height=85, corner_radius=16, text_color="#f8fafc", fg_color="#991b1b", hover_color="#dc2626")
brake_button.grid(row=2, column=0, padx=(32, 8), pady=(0, 32))

increase_button = ctk.CTkButton(main_frame, text="+ Subir velocidad", command=lambda: increase_speed(), font=("Roboto", 20), width=150, height=85, corner_radius=16, text_color="#f8fafc", fg_color="#1e293b", )
increase_button.grid(row=1, column=1, sticky="ew", padx=(8, 32), pady=(0, 16))

decrease_button = ctk.CTkButton(main_frame, text="- Bajar velocidad", command=lambda: decrease_speed(), font=("Roboto", 20), width=150, height=85, corner_radius=16, text_color="#f8fafc", fg_color="#1e293b")
decrease_button.grid(row=2, column=1, sticky="ew", padx=(8, 32), pady=(0, 32))

# Run the application
app.mainloop()

