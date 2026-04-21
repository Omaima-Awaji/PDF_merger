from pypdf import PdfReader, PdfWriter

def pdf_merger():

    pdf_files_list = []

    while True:
        pdf_files = input('''
        Please enter file path.
        If you're done type "done"''').lower()

        if pdf_files == "done":
            break

        pdf_files_list.append(pdf_files)

    writer = PdfWriter()

    for files in pdf_files_list:
        try:
            reader = PdfReader(files)
        except FileNotFoundError:
            print(f" File '{files}' not found. Skipping.")
            continue
        for pages in reader.pages:
            writer.add_page(pages)

    new_file_name = input("What would you like to call the new merged file? ")

    with open(new_file_name + ".pdf", "wb") as output_file:
        writer.write(output_file)

    print(f"{new_file_name}.pdf created successfully!")

if __name__ == "__main__":
    pdf_merger()