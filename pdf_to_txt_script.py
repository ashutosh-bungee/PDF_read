import re
import pdfplumber


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=3, y_tolerance=3) + "\n"
    return text


def structure_text(raw_text):
    structured = []
    current_indent = 0
    print(raw_text)
    lines = raw_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect main headings (e.g., "1. INTRODUCTION")
        if re.match(r'^\d+\.\s', line):
            structured.append(line)
            current_indent = 0
      
        # Detect subheadings (e.g., "1.1. History")
        elif re.match(r'^\d+\.\d+\.\s', line):
            structured.append('\t' + line)
            current_indent = 1
       
        # Detect bullet points (starts with "-" or "" or "1)")
        elif line.startswith('-') or line.startswith('') or line.startswith('•') or line.startswith('') or line.startswith(r'\d+\)'):
            structured.append('\t' * (current_indent + 1) + '• ' + line[1:].strip())
        else:
            if structured:
                structured[-1] += ' ' + line
            else:
                structured.append(line)
    
    return '\n'.join(structured)

if __name__ == "__main__":
    raw_text = extract_text_from_pdf("Labour Act.pdf")
    structured_text = structure_text(raw_text)
    with open("output11.txt", "w", encoding="utf-8") as f:
        f.write(structured_text)
    print("Structured text saved to output.txt")