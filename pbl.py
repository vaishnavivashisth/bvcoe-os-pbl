import tkinter as tk
from tkinter import messagebox

# --- Algorithm Implementations ---
def simulate_fifo(pages, frames):
    memory = []
    faults = 0
    steps = []
    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) == frames:
                memory.pop(0)
            memory.append(page)
            steps.append((page, list(memory), True))
        else:
            steps.append((page, list(memory), False))
    return faults, steps

def simulate_lru(pages, frames):
    memory = []
    faults = 0
    steps = []
    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) == frames:
                memory.pop(0)
            memory.append(page)
            steps.append((page, list(memory), True))
        else:
            memory.remove(page)
            memory.append(page)
            steps.append((page, list(memory), False))
    return faults, steps

def simulate_optimal(pages, frames):
    memory = []
    faults = 0
    steps = []
    for i, page in enumerate(pages):
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                farthest = -1
                replace_idx = -1
                for j, mem_page in enumerate(memory):
                    try:
                        next_use = pages[i+1:].index(mem_page)
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest:
                        farthest = next_use
                        replace_idx = j
                memory[replace_idx] = page
            steps.append((page, list(memory), True))
        else:
            steps.append((page, list(memory), False))
    return faults, steps

# --- GUI Application ---
class PageReplacementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Visualizer")
        
        tk.Label(root, text="Reference String (comma separated):").grid(row=0, column=0)
        self.ref_entry = tk.Entry(root, width=30)
        self.ref_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Number of Frames:").grid(row=1, column=0)
        self.frames_entry = tk.Entry(root, width=10)
        self.frames_entry.grid(row=1, column=1, sticky='w')
        
        self.algo_var = tk.StringVar(value="FIFO")
        tk.OptionMenu(root, self.algo_var, "FIFO", "LRU", "Optimal").grid(row=2, column=1, sticky='w')
        
        tk.Button(root, text="Simulate", command=self.run_simulation).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.grid(row=4, column=0, columnspan=2)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=5, column=0, columnspan=2)

    def run_simulation(self):
        try:
            pages = [int(x.strip()) for x in self.ref_entry.get().split(",")]
            frames = int(self.frames_entry.get())
            algo = self.algo_var.get()
            
            if algo == "FIFO":
                faults, steps = simulate_fifo(pages, frames)
            elif algo == "LRU":
                faults, steps = simulate_lru(pages, frames)
            else:
                faults, steps = simulate_optimal(pages, frames)
                
            self.draw_steps(steps, frames)
            self.result_label.config(text=f"Total Page Faults ({algo}): {faults}")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")

    def draw_steps(self, steps, frames):
        self.canvas.delete("all")
        x_offset = 20
        for i, (page, memory, is_fault) in enumerate(steps):
            tk.Label(self.canvas, text=str(page), bg="white").place(x=x_offset + i*40, y=10)
            
            for j in range(frames):
                y_offset = 40 + j*30
                val = str(memory[j]) if j < len(memory) else "-"
                color = "red" if is_fault and (j == len(memory)-1 or val == str(page)) else "lightgrey"
                self.canvas.create_rectangle(x_offset + i*40, y_offset, x_offset + i*40 + 30, y_offset + 30, fill=color)
                self.canvas.create_text(x_offset + i*40 + 15, y_offset + 15, text=val)
                
if __name__ == "__main__":
    root = tk.Tk()
    app = PageReplacementApp(root)
    root.mainloop()