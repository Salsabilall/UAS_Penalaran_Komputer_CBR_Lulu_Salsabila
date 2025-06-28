import os
import PyPDF2

pdf_folder = 'C:\Users\Lulu Salsabila\Downloads\30 file' # GANTI INI DENGAN LOKASI FOLDER PDF ANDA
output_raw_text_folder = os.path.join(os.getcwd(), 'data', 'raw')
os.makedirs(output_raw_text_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        output_filename = filename.replace('.pdf', '.txt')
        output_path = os.path.join(output_raw_text_folder, output_filename)

        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_num in range(len(reader.pages)):
                    text += reader.pages[page_num].extract_text()

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Extracted: {filename} -> {output_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("\nDONE with text extraction. Files are in data/raw/")