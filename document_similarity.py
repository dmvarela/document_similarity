import glob
import os
file_list = glob.glob(os.path.join(os.getcwd(), "zone/document_similarity", "*.txt"))

raw_documents = []

for file_path in file_list:
    with open(file_path, encoding="utf8") as f_input:
        raw_documents.append(f_input.read())

print("Number of documents:",len(raw_documents))
