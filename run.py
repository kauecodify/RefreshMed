# -*- coding: utf-8 -*-
"""

Created on Mon Mar 17 22:18:40 2025

@author: Kaue

"""

import tkinter as tk
from tkinter import ttk, messagebox

# Função para calcular a dosagem
def calcular_dosagem():
    try:
        peso = float(entrada_peso.get())
        dose_por_kg = float(entrada_dose.get())
        dosagem_total = peso * dose_por_kg
        resultado.config(text=f"Dosagem total: {dosagem_total:.2f} mg")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# interface gráfica
app = tk.Tk()
app.title("RefreshMed")
app.geometry("400x300")
app.configure(bg="#2E3440")  # Cor de fundo cinza escuro

# bordas arredondadas e cores
style = ttk.Style()
style.configure("TFrame", background="#2E3440")
style.configure("TLabel", background="#2E3440", foreground="#88C0D0", font=("Arial", 12))  # Azul bebê para texto
style.configure("TButton", background="#81A1C1", foreground="#2E3440", font=("Arial", 12, "bold"), borderwidth=0)
style.map("TButton", background=[("active", "#5E81AC")])  # Azul bebê mais escuro ao passar o mouse

# frame principal
frame = ttk.Frame(app, padding="20")
frame.pack(expand=True, fill="both")

# titulo
titulo = ttk.Label(frame, text="RefreshMed", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# peso
label_peso = ttk.Label(frame, text="Peso do paciente (kg):")
label_peso.pack(pady=5)
entrada_peso = ttk.Entry(frame, font=("Arial", 12))
entrada_peso.pack(pady=5)

# dose por kg
label_dose = ttk.Label(frame, text="Dose por kg (mg/kg):")
label_dose.pack(pady=5)
entrada_dose = ttk.Entry(frame, font=("Arial", 12))
entrada_dose.pack(pady=5)

# calcular
botao_calcular = ttk.Button(frame, text="Calcular Dosagem", command=calcular_dosagem)
botao_calcular.pack(pady=20)

# resultado
resultado = ttk.Label(frame, text="", font=("Arial", 14, "bold"))
resultado.pack(pady=10)

app.mainloop()