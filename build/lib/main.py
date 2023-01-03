import tkinter as tk
from dialog.dialog_box import MyApp

root = tk.Tk()
root.withdraw()
window = MyApp(root)

root.mainloop()

if __name__ == '__main__':
    print("\nThe program has finished operations.")

