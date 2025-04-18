import os
import subprocess

# Folder containing .pptx files
input_folder = "/Users/toan/Downloads/Exam 2 Prep"  # <-- change this

# Loop through all files in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pptx"):
        full_path = os.path.join(input_folder, filename)
        print(f"Converting: {filename}")
        
        try:
            subprocess.run([
                "/Applications/LibreOffice.app/Contents/MacOS/soffice",
                "--headless",
                "--convert-to", "pdf",
                "--outdir", input_folder,
                full_path
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {filename}: {e}")
