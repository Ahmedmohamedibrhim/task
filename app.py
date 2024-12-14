import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time
import threading

def start_download(quality):
    link = link_entry.get()
    if not link:
        messagebox.showerror("خطأ", "يرجى إدخال رابط الفيديو.")
        return

    status_label.config(text=f"جاري تحميل الفيديو ({quality})...")
    progress_bar['value'] = 0
    speed_label.config(text="Speed: 0.00 MB/s")
    file_path = filedialog.asksaveasfilename(
        title="اختر مكان حفظ الملف",
        defaultextension=".mp4" if quality != "audio" else ".mp3",
        filetypes=[("Video Files", ".mp4"), ("Audio Files", ".mp3")]
    )

    # تشغيل التنزيل في خيط مستقل لتجنب تجميد الواجهة
    threading.Thread(target=download_process, args=(quality,)).start()

def download_process(quality):
    for i in range(1, 101):  # شريط التقدم (1 إلى 100)
        time.sleep(0.05)  # محاكاة زمن التحميل
        progress_bar['value'] = i
        speed_label.config(text=f"Speed: {round(1.37 + (i / 100), 2)} MB/s")
        root.update_idletasks()

    status_label.config(text="تم التحميل بنجاح!")

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x250")

# إدخال الرابط
tk.Label(root, text="أدخل رابط الفيديو").pack(pady=5)
link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

# أزرار التحميل
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="High quality download", command=lambda: start_download("High Quality")).grid(row=0, column=0, padx=5)
tk.Button(buttons_frame, text="Low quality download", command=lambda: start_download("Low Quality")).grid(row=0, column=1, padx=5)
tk.Button(buttons_frame, text="Only audio", command=lambda: start_download("Audio Only")).grid(row=0, column=2, padx=5)

# شريط التقدم
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# زر الإلغاء
tk.Button(root, text="Cancel", command=root.quit).pack(pady=5)

# تسميات الحالة والسرعة
status_label = tk.Label(root, text="Starting download...", fg="gray")
status_label.pack(pady=5)
speed_label = tk.Label(root, text="Speed: 0.00 MB/s", fg="green")
speed_label.pack(pady=5)

# تشغيل التطبيق
root.mainloop()