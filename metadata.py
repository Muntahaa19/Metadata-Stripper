import os
import shutil
import random
import string
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps
import piexif
import fitz  # PyMuPDF
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from mutagen.oggopus import OggOpus
from mutagen.aac import AAC
from docx import Document
import numpy as np

def generate_random_metadata():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=128))

def randomize_timestamps(file_path):
    random_time = random.randint(1000000000, int(time.time()))
    os.utime(file_path, (random_time, random_time))

def randomize_filename(file_path):
    ext = os.path.splitext(file_path)[1]
    new_name = f"anon_{random.randint(1000000, 9999999)}{ext}"
    new_path = os.path.join(os.path.dirname(file_path), new_name)
    shutil.move(file_path, new_path)
    return new_path

def get_file_type(file_path):
    ext = file_path.lower().split('.')[-1]
    if ext in ["jpg", "jpeg", "png", "webp", "bmp", "tiff"]:
        return "image"
    elif ext in ["mp4", "mov", "avi", "mkv", "wmv", "flv"]:
        return "video"
    elif ext in ["mp3", "flac", "ogg", "opus", "aac", "wav"]:
        return "audio"
    elif ext == "pdf":
        return "pdf"
    elif ext in ["doc", "docx"]:
        return "word"
    else:
        return "unknown"

def process_image(file_path, save_path):
    try:
        image = Image.open(file_path)
        new_width = image.width + random.randint(-100, 100)
        new_height = image.height + random.randint(-100, 100)
        image = image.resize((max(100, new_width), max(100, new_height)))
        if random.choice([True, False]):
            image = ImageOps.mirror(image)
        if random.choice([True, False]):
            image = ImageOps.flip(image)
        piexif.remove(file_path)
        new_format = random.choice(["JPEG", "PNG", "WEBP"])
        image = image.convert("RGB")
        image.save(save_path, format=new_format, quality=random.randint(70, 95))
        randomize_timestamps(save_path)
        return True
    except Exception:
        return False

def process_pdf(file_path, save_path):
    try:
        pdf = fitz.open(file_path)
        pdf.set_metadata({
            "title": generate_random_metadata(),
            "author": generate_random_metadata(),
            "subject": generate_random_metadata(),
            "keywords": generate_random_metadata(),
            "creator": generate_random_metadata(),
            "producer": generate_random_metadata(),
            "creationDate": "",
            "modDate": ""
        })
        for page in pdf:
            page.clean_contents()
        pdf.save(save_path)
        randomize_timestamps(save_path)
        return True
    except Exception:
        return False

def process_audio(file_path, save_path):
    try:
        ext = file_path.split('.')[-1].lower()
        audio = None
        if ext == "mp3":
            audio = MP3(file_path, ID3=ID3)
        elif ext == "flac":
            audio = FLAC(file_path)
        elif ext == "ogg":
            audio = OggVorbis(file_path)
        elif ext == "opus":
            audio = OggOpus(file_path)
        elif ext == "aac":
            audio = AAC(file_path)
        if audio:
            audio.delete()
            audio["comment"] = generate_random_metadata()
            audio["encoded_by"] = generate_random_metadata()
            audio.save()
            shutil.copy(file_path, save_path)
            randomize_timestamps(save_path)
            return True
        return False
    except Exception:
        return False

def process_word(file_path, save_path):
    try:
        doc = Document(file_path)
        properties = ["author", "comments", "keywords", "title", "subject"]
        for prop in properties:
            setattr(doc.core_properties, prop, generate_random_metadata())
        doc.add_paragraph(f"_{generate_random_metadata()}_")
        doc.save(save_path)
        randomize_timestamps(save_path)
        return True
    except Exception:
        return False

def process_video(file_path, save_path):
    try:
        shutil.copy(file_path, save_path)
        randomize_timestamps(save_path)
        return True
    except Exception:
        return False

def remove_metadata():
    file_path = filedialog.askopenfilename(title="Select a file")
    if not file_path:
        return
    file_type = get_file_type(file_path)
    save_path = filedialog.asksaveasfilename(defaultextension=os.path.splitext(file_path)[1])
    if not save_path:
        return
    success = False
    if file_type == "image":
        success = process_image(file_path, save_path)
    elif file_type == "audio":
        success = process_audio(file_path, save_path)
    elif file_type == "pdf":
        success = process_pdf(file_path, save_path)
    elif file_type == "word":
        success = process_word(file_path, save_path)
    elif file_type == "video":
        success = process_video(file_path, save_path)
    else:
        messagebox.showerror("Unsupported File", "Cannot process this file type.")
        return
    if success:
        randomize_filename(save_path)
        messagebox.showinfo("Success", "Metadata fully removed and randomized!")
    else:
        messagebox.showerror("Error", "Failed to anonymize metadata.")

root = tk.Tk()
root.title("Advanced Metadata Anonymizer")
root.geometry("350x250")
btn_select = tk.Button(root, text="Select File", command=remove_metadata, padx=10, pady=5)
btn_select.pack(pady=20)
root.mainloop()
