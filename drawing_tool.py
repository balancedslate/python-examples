import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageGrab

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.brush_size_val = 1
        self.brush_color_val = 'black'
        
        self.brush_size = tk.Scale(master, from_=1, to=50, orient=tk.HORIZONTAL, command=self.update_brush_size)
        self.brush_size.pack()
        
        self.brush_color = tk.Button(master, bg='black', command=self.update_brush_color)
        self.brush_color.pack()
        
        self.eraser_on = tk.BooleanVar()
        self.eraser = tk.Checkbutton(master, text='Eraser', variable=self.eraser_on, command=self.activate_eraser)
        self.eraser.pack()
        
        self.save_button = tk.Button(master, text='Save as image', command=self.save_as_image)
        self.save_button.pack()
        
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        
        self.canvas.bind('<B1-Motion>', self.paint)
        
    def update_brush_size(self, size):
        self.brush_size_val = int(size)
        
    def update_brush_color(self):
        self.brush_color_val = self.brush_color.cget('bg')
        
    def activate_eraser(self):
        if self.eraser_on.get():
            self.brush_color_val = 'white'
        else:
            self.brush_color_val = 'black'
        
    def paint(self, event):
        x1, y1 = (event.x - self.brush_size_val), (event.y - self.brush_size_val)
        x2, y2 = (event.x + self.brush_size_val), (event.y + self.brush_size_val)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color_val, outline=self.brush_color_val)
        
    def save_as_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        if file_path:
            x = self.canvas.winfo_rootx()
            y = self.canvas.winfo_rooty()
            x1 = x + self.canvas.winfo_x()
            y1 = y + self.canvas.winfo_y()
            x2 = x1 + self.canvas.winfo_width()
            y2 = y1 + self.canvas.winfo_height()
            image = ImageGrab.grab().crop((x1, y1, x2, y2))
            image.save(file_path)

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
