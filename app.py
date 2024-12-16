import customtkinter as ctk

# Configure the appearance mode and theme
ctk.set_appearance_mode("Light")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create the main application window
app = ctk.CTk()
app.title("VESCA")
app.geometry("600x600")
app.configure(fg_color="#f8fafc")
app.grid_columnconfigure((0), weight=1)

main_frame = ctk.CTkFrame(app, corner_radius=24, fg_color="#f1f5f9", border_width=1, border_color="#e2e8f0")
main_frame.grid(row=0, column=0, padx=64, pady=64, sticky="")

# Create a label with the title of the application
title_label = ctk.CTkLabel(main_frame, text="Controles para el VESCA", font=("Roboto", 24, "bold"), text_color="#334155")
title_label.grid(row=0, column=0, columnspan=2, padx=32, pady=32, sticky="ew")

# Function to handle button clicks
def button_click(button_id):
    print(f"Button {button_id} clicked!")

button1 = ctk.CTkButton(main_frame, text="Frenar", command=lambda: button_click(1), font=("Roboto", 20), width=150, height=85, corner_radius=16, text_color="#f8fafc", fg_color="#991b1b", hover_color="#dc2626")
button1.grid(row=1, column=0, rowspan=2, padx=(32, 16), pady=16)

button3 = ctk.CTkButton(main_frame, text="+ Subir velocidad", command=lambda: button_click(3), font=("Roboto", 20), width=150, height=85, corner_radius=16, text_color="#f8fafc", fg_color="#1e293b", )
button3.grid(row=1, column=1, sticky="ew", padx=(16, 32), pady=(0, 16))

button4 = ctk.CTkButton(main_frame, text="- Bajar velocidad", command=lambda: button_click(4), font=("Roboto", 20), width=150, height=85, corner_radius=16, text_color="#f8fafc", fg_color="#1e293b")
button4.grid(row=2, column=1, sticky="ew", padx=(16, 32), pady=(0, 32))

# Run the application
app.mainloop()

