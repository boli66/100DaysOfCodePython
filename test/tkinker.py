import tkinter as tk

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Counter")

        self.click_count = 0

        self.label = tk.Label(root, text="Clicks: 0")
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Click me!", command=self.increment_count)
        self.button.pack()

    def increment_count(self):
        self.click_count += 1
        self.label.config(text=f"Clicks: {self.click_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.geometry("300x200")  # Set the window size to 300x200
    root.mainloop()