# file_tools.py
import os
import shutil

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def classify_and_move(input_str: str) -> str:
    src_folder = "sample_files"
    dest_folder = "organized_files"
    os.makedirs(dest_folder, exist_ok=True)

    files = list_files(src_folder)
    moved = []

    for file in files:
        lower = file.lower()
        if "resume" in lower:
            category = "Resumes"
        elif "invoice" in lower:
            category = "Invoices"
        elif file.endswith(('.jpg', '.png')):
            category = "Images"
        elif file.endswith('.pdf'):
            category = "PDFs"
        else:
            category = "Others"

        target_path = os.path.join(dest_folder, category)
        os.makedirs(target_path, exist_ok=True)

        shutil.move(os.path.join(src_folder, file), os.path.join(target_path, file))
        moved.append(f"{file} → {category}")

    return "\n".join(moved)
