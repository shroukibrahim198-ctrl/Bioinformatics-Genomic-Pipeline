import os

def fastq_parser_and_features(file_path):
    """
    وظيفة الكود: قراءة ملف FASTQ وحساب الخصائص (Parsing & Feature Extraction)
    """
    if not os.path.exists(file_path):
        return f"File {file_path} not found!"

    read_count = 0
    total_bases = 0
    gc_count = 0
    lengths = []

    with open(file_path, 'r') as f:
        # بنقرأ الملف سطر بسطر (السيناريو: بنمشي على بلوكات من 4 سطور)
        lines = f.readlines()
        for i in range(1, len(lines), 4):
            sequence = lines[i].strip() # السطر التاني هو اللي فيه الـ DNA
            read_count += 1
            total_bases += len(sequence)
            gc_count += sequence.count('G') + sequence.count('C')
            lengths.append(len(sequence))

    # الحسابات النهائية
    gc_content = (gc_count / total_bases) * 100 if total_bases > 0 else 0
    avg_length = sum(lengths) / len(lengths) if lengths else 0

    return {
        "Total Reads": read_count,
        "GC Content (%)": round(gc_content, 2),
        "Average Read Length": round(avg_length, 2)
    }

# تشغيل الكود على ملفات المشروع
if __name__ == "main":
    # المسارات دي بناءً على تنظيم الفولدرات اللي عملناه سوا
    cancer_path = 'results/cleaned_data/cancer/cleaned_cancer_1.fastq'
    healthy_path = 'results/cleaned_data/healthy/cleaned_healthy_1.fastq'

    print("--- Cancer Data Features ---")
    print(fastq_parser_and_features(cancer_path))

    print("\n--- Healthy Data Features ---")
    print(fastq_parser_and_features(healthy_path))