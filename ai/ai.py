import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# === قراءة قاعدة المعرفة من ملف ===
def load_knowledge(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


knowledge = load_knowledge("aa.txt")

# === تحويل النصوص إلى أرقام (تدريب النموذج) ===
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(knowledge)


# === دالة للإجابة ===
def answer_question(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    worst_match = similarity.argmax()
    return knowledge[worst_match]


# === واجهة المستخدم ===
root = tk.Tk()
root.title("AI programming helper")
root.geometry("700x500")
root.configure(bg="#045951")

# صندوق النصوص (المحادثة)
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 13), height=20)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.config(state=tk.DISABLED)

# إطار لمدخل النص والزر
bottom_frame = tk.Frame(root, bg="#f7f7f7")
bottom_frame.pack(fill=tk.X, padx=10, pady=5)

# إدخال المستخدم
user_input = tk.Entry(bottom_frame, font=("Arial", 14))
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))


# دالة إرسال الرسالة
def send_message(event=None):
    q = user_input.get().strip()
    if not q:
        return
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"👤 You: {q}\n", "user")
    answer = answer_question(q)
    chat_box.insert(tk.END, f"🤖 AI: {answer}\n\n", "bot")
    chat_box.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)
    chat_box.yview(tk.END)


# زر الإرسال
send_btn = tk.Button(
    bottom_frame,
    text="send",
    command=send_message,
    font=("Arial", 12),
    bg="#E43636",
    fg="white",
)
send_btn.pack(side=tk.RIGHT)

# تفعيل الضغط على Enter للإرسال
root.bind("<Return>", send_message)

# تشغيل التطبيق
root.mainloop()
