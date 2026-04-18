# 📂 Bulk File Renamer (Python Automation Script)

A simple Python script that automatically renames all files in a folder using a **consistent naming pattern**.

This project is useful for organizing files quickly and efficiently.

---

# 🚀 Features

✔ Automatically renames all files in a folder
✔ Keeps original file extensions
✔ Adds sequential numbering
✔ Fast and efficient
✔ Beginner-friendly script

---

# 🛠 Technologies Used

* Python
* OS module

---

# 📂 Project Structure

```id="ren1"
bulk-file-renamer
│
├── main.py
└── README.md
```

👉 Rename your file to **main.py**.

---

# ⚙️ Setup

1️⃣ Install Python 3.x

2️⃣ Update folder path in code:

```python id="ren2"
folder_path = "C:/Users/ravir/OneDrive/Desktop/Test"
```

---

# ▶️ How to Run

```bash id="ren3"
git clone https://github.com/ravigautam7739/bulk-file-renamer.git
cd bulk-file-renamer
python main.py
```

---

# 🧠 How It Works

1. Reads all files in the specified folder
2. Loops through each file
3. Extracts file extension
4. Renames file as:

```id="ren4"
project_1.jpg
project_2.png
project_3.txt
```

5. Saves renamed files in the same folder

---

# 💻 Example Output

Before:

```id="ren5"
IMG_1234.jpg
file_random.png
test.txt
```

After:

```id="ren6"
project_1.jpg
project_2.png
project_3.txt
```

---

# 🎯 Use Cases

* Organizing files
* Cleaning messy folders
* Batch renaming images/videos
* Automation tasks
* Productivity tools

---

# ⚠️ Notes

* Make sure folder path is correct
* Renaming is permanent (no undo)
* Backup important files before running

---

# 🔮 Future Improvements

* Custom naming patterns
* GUI interface
* Select specific file types
* Add prefixes/suffixes
* Undo functionality

---

# ⭐ Support

If you found this script useful, give it a **star ⭐**.
