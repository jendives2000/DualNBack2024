import tkinter as tk
from tkinter import messagebox
import random
import pygame
import time
import threading

# Initialize Pygame Mixer pour le son
pygame.mixer.init()

# Chargement des sons
SOUND_FILES = {"b": "b.wav", "d": "d.wav", "h": "h.wav", "k": "k.wav", "p": "p.wav"}

# Préchargement des sons
SOUNDS = {}
for key, file in SOUND_FILES.items():
    try:
        SOUNDS[key] = pygame.mixer.Sound(file)
    except pygame.error:
        print(f"Error loading sound: {file}")
        SOUNDS[key] = None  # au cas où un son manque


class DualAndBackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dual and Back Memory Game")
        self.master.geometry("1920x1080")
        self.master.configure(
            bg="#1A1A1A"
        )  # une couleur noir qui n'est pas du pur noir

        # Variables du jeux
        self.grid_size = 3
        self.cell_color = "light purple"
        self.bg_color = "#1A1A1A"
        self.grid_percent = 0.65
        self.signal_duration = 1000  # en milliseconds (par défaut 1 seconde)
        self.num_signals = 21
        self.custom_signals = False
        self.current_signal = 0
        self.max_signals = 21
        self.active_case = None
        self.previous_case = {}
        self.signals = []
        self.game_running = False
        self.start_time = None
        self.end_time = None
        self.missed = 0
        self.correct = 0
        self.game_number = 1
        self.last_game_time = 0
        self.report_lines = []

        # Dictionnaires pour les infos de la grille
        self.grid_dict = {}
        for i in range(1, 10):
            self.grid_dict[i] = {"position": i, "sound": "nosound", "active": False}

        # Création des éléments du GUI (interface graphique)
        self.create_widgets()

    def create_widgets(self):
        # Calcul des dimensiosns de la grille
        grid_width = int(1920 * self.grid_percent)
        grid_height = grid_width  # Square grid
        cell_width = grid_width // self.grid_size
        cell_height = grid_height // self.grid_size

        # Cadre la grille
        self.grid_frame = tk.Frame(self.master, bg=self.bg_color)
        self.grid_frame.place(
            relx=0.5, rely=0.5, anchor=tk.CENTER, width=grid_width, height=grid_height
        )

        # Creation d'une grille de 3x3 via Canvas
        self.cells = {}
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell_num = row * self.grid_size + col + 1
                canvas = tk.Canvas(
                    self.grid_frame,
                    width=cell_width,
                    height=cell_height,
                    bg="white",
                    highlightthickness=1,
                    highlightbackground="black",
                )
                canvas.grid(row=row, column=col)
                self.cells[cell_num] = canvas

        # Bouton Start
        self.start_button = tk.Button(
            self.master,
            text="START",
            bg="white",
            fg="black",
            font=("Arial", 16),
            command=self.start_game,
        )
        self.start_button.place(
            x=100, y=(1080 - grid_height) // 2 + grid_height + 100, width=150, height=50
        )

        # Boutons de sélection du nombre souhaité de signaux pour 1 jeux
        signal_options = [21, 30, 42, 60]
        self.signal_buttons = []
        for idx, num in enumerate(signal_options):
            btn = tk.Button(
                self.master,
                text=str(num),
                bg="white",
                fg="black",
                font=("Arial", 14),
                command=lambda n=num: self.set_num_signals(n),
            )
            btn.place(x=100, y=100 + idx * 75, width=100, height=50)
            self.signal_buttons.append(btn)

        # Le champs d'input pour rentrer le nombre souhaité de signaux pour 1 jeux
        self.custom_label = tk.Label(
            self.master,
            text="Custom # of signals:",
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12),
        )
        self.custom_label.place(x=100, y=100 + len(signal_options) * 75 + 10)

        self.custom_entry = tk.Entry(
            self.master, bg="white", fg="black", font=("Arial", 12)
        )
        self.custom_entry.place(
            x=100, y=100 + len(signal_options) * 75 + 30, width=100, height=30
        )
        self.custom_entry.bind("<Return>", self.set_custom_signals)

        # Boutons pour le choix de la durée de chaque signal
        durations = [1, 2, 3]
        self.duration_buttons = []
        for idx, dur in enumerate(durations):
            btn = tk.Button(
                self.master,
                text=f"{dur} sec",
                bg="white",
                fg="black",
                font=("Arial", 14),
                command=lambda d=dur: self.set_duration(d),
            )
            btn.place(
                x=100,
                y=100 + (len(signal_options) + 2) * 75 + idx * 75,
                width=100,
                height=50,
            )
            self.duration_buttons.append(btn)

        # Boutons pour les Confirmations POSITION et SOUND
        self.position_button = tk.Button(
            self.master,
            text="POSITION",
            bg="light grey",
            fg="black",
            font=("Arial", 14),
            command=lambda: self.confirm("position"),
        )
        self.position_button.place(
            relx=0.5, rely=0.75, anchor=tk.CENTER, x=-150, y=0, width=150, height=50
        )

        self.sound_button = tk.Button(
            self.master,
            text="SOUND",
            bg="light grey",
            fg="black",
            font=("Arial", 14),
            command=lambda: self.confirm("sound"),
        )
        self.sound_button.place(
            relx=0.5, rely=0.75, anchor=tk.CENTER, x=150, y=0, width=150, height=50
        )

        # Cadre pour le rapport d'info après chaque jeu
        self.report_text = tk.Text(
            self.master,
            bg=self.bg_color,
            fg="white",
            font=("Arial", 12),
            state="disabled",
        )
        self.report_text.place(x=1920 - 400, y=100, width=300, height=800)

        # Bouton Again pour rejouer le meme jeu (tjrs caché au tout 1er  jeu)
        self.again_button = tk.Button(
            self.master,
            text="Again",
            bg="green",
            fg="black",
            font=("Arial", 14),
            command=self.again_game,
        )
        self.again_button.place(x=1920 - 350, y=1000, width=100, height=50)
        self.again_button.lower()  # tjrs caché au tout 1er  jeu

    def set_num_signals(self, num):
        self.num_signals = num
        self.custom_signals = False
        self.custom_entry.delete(0, tk.END)

    def set_custom_signals(self, event):
        try:
            num = int(self.custom_entry.get())
            if num > 0:
                self.num_signals = num
                self.custom_signals = True
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def set_duration(self, dur):
        self.signal_duration = dur * 1000  # Convertis en millisecondes

    def start_game(self):
        if self.game_running:
            return
        self.game_running = True
        self.start_button.config(state="disabled")
        self.reset_game()
        self.start_time = time.time()
        self.run_signals()

    def reset_game(self):
        # Reset du grid_dict
        for i in range(1, 10):
            self.grid_dict[i]["sound"] = "nosound"
            self.grid_dict[i]["active"] = False
            self.clear_cell(i)

        # Reset des variables de jeu
        self.current_signal = 0
        self.missed = 0
        self.correct = 0
        self.signals = []
        self.previous_case = {}
        self.report_lines = []
        self.end_time = None

    def clear_cell(self, cell_num):
        self.cells[cell_num].delete("all")
        self.cells[cell_num].configure(bg="white")

    def run_signals(self):
        if self.current_signal >= self.num_signals:
            self.end_game()
            return

        # Détermination aléatoire de chaque signal
        next_cell = random.randint(1, 9)
        next_sound = random.choice(list(SOUNDS.keys()))
        while self.current_signal > 0 and next_cell == self.active_case:
            # choisi la case de manière alétoire
            next_cell = random.randint(1, 9)
        self.active_case = next_cell
        self.grid_dict[next_cell]["sound"] = next_sound
        self.grid_dict[next_cell]["active"] = True

        # Joue un des sons
        if SOUNDS[next_sound]:
            threading.Thread(target=SOUNDS[next_sound].play).start()

        # Crée le cercle jaune dans les cases
        self.draw_signal(next_cell, "yellow")

        # Copie la case active en cours vers la previous_case si ce n'est pas le 1er signal
        # Anglais : Copy current active case to previous_case if not first signal
        if self.current_signal > 0:
            self.previous_case = self.grid_dict[self.active_case].copy()

        # Pour la fin du signal (Schedule end of signal)
        self.master.after(self.signal_duration, self.end_signal)

        self.current_signal += 1

    def draw_signal(self, cell_num, color):
        canvas = self.cells[cell_num]
        canvas.delete("all")
        width = int(canvas["width"])
        height = int(canvas["height"])
        diameter = min(width, height) - 25
        x0 = (width - diameter) // 2
        y0 = (height - diameter) // 2
        x1 = x0 + diameter
        y1 = y0 + diameter
        canvas.create_oval(x0, y0, x1, y1, fill=color, outline="")

    def end_signal(self):
        # Hide the signal
        self.grid_dict[self.active_case]["active"] = False
        self.clear_cell(self.active_case)

        # Vérifie si le joueur n'a pas clické sur un des boutons POSITION ou SOUND (Check if user did not confirm)
        # Lancé en vérifiant si la confirmation (click du joueur sur les boutons) a été fait avant que le signal ne se termine (Implemented by checking if confirmation was done before signal ended)
        # Pour simplifier, si aucun click de confirmation, considérer que c'est un manqué (A CORRIGER) (For simplicity, assuming if no confirmation was made, it's a missed signal)
        if not hasattr(self, "last_confirmation"):
            self.missed += 1
        else:
            if self.last_confirmation is None:
                self.missed += 1
        self.last_confirmation = None  # Reset for next signal

        # Procéder au prochain signal (Proceed to next signal)
        self.run_signals()

    def confirm(self, conf_type):
        if not self.game_running:
            return
        # Enregistre une confirmation (click)
        if not hasattr(self, "last_confirmation") or self.last_confirmation is None:
            self.last_confirmation = set()
        self.last_confirmation.add(conf_type)

        # Vérifie la confirmation (Check confirmation)
        correct_position = False
        correct_sound = False
        if self.current_signal == 1:
            # Aucune case précédente à comparer (No previous case to compare)
            correct = False
        else:
            prev = self.previous_case
            current = self.grid_dict[self.active_case]
            if "position" in self.last_confirmation:
                correct_position = current["position"] == prev["position"]
            if "sound" in self.last_confirmation:
                correct_sound = current["sound"] == prev["sound"]

            # Détermine la justeté général (Determine overall correctness)
            if (
                "position" in self.last_confirmation
                and "sound" in self.last_confirmation
            ):
                correct = correct_position and correct_sound
            elif "position" in self.last_confirmation:
                correct = correct_position
            elif "sound" in self.last_confirmation:
                correct = correct_sound
            else:
                correct = False

            if correct:
                self.correct += 1
                self.draw_signal(self.active_case, "green")
            else:
                self.missed += 1
                self.draw_signal(self.active_case, "red")

        # Planifie le retour de la couleur du signal à bleu (Schedule reverting color back to blue)
        self.master.after(500, lambda: self.draw_signal(self.active_case, "blue"))

    def end_game(self):
        self.game_running = False
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        success_percentage = (
            (self.correct / self.num_signals) * 100 if self.num_signals > 0 else 0
        )

        # Mise à jour du rapport (Update report)
        report = f"Missed Signals: {self.missed}\n"
        report += (
            f"Success: {self.correct}/{self.num_signals} ({success_percentage:.2f}%)\n"
        )
        report += f"Game Number: {self.game_number}\n"
        report += f"Time Taken: {elapsed_time:.2f} seconds\n"
        report += f"Previous Game Time: {self.last_game_time:.2f} seconds\n"

        self.report_lines.append(report)
        self.update_report(report)

        # Préparation du prochain jeu (Prepare for next game)
        self.last_game_time = elapsed_time
        self.game_number += 1

        # Montrer le bouton AGAIN pour rejouer le même jeu (Show Again button)
        self.again_button.lift()

    def update_report(self, report):
        self.report_text.config(state="normal")
        self.report_text.insert(tk.END, report + "\n")
        self.report_text.config(state="disabled")

    def again_game(self):
        # Cache le bouton AGAIN (Hide Again button)
        self.again_button.lower()

        # Reset de la grille et des variables (Reset grid and variables)
        self.reset_game()
        self.start_time = time.time()
        self.run_signals()

        # Ré-appliquer les même paramètres (Re-apply same settings)
        # en assumant que le joueur n'a pas changé les paramètres durant le jeu (Assuming the user did not change settings during the game)

    def play_sound(self, sound_key):
        if SOUNDS.get(sound_key):
            SOUNDS[sound_key].play()


if __name__ == "__main__":
    root = tk.Tk()
    app = DualAndBackApp(root)
    root.mainloop()
