import pandas as pd
import json

INPUT_CSV = "tagged_curriculum_chunks.csv"
OUTPUT_JSONL = "cleaned_curriculum_chunks.jsonl"

def clean_metadata(row):
    for field in ['disciplinary_core_ideas', 'science_practices', 'crosscutting_concepts']:
        try:
            row[field] = eval(row[field]) if isinstance(row[field], str) else row[field]
        except:
            row[field] = []
    return row

def main():
    print("📥 Loading tagged curriculum chunks...")
    df = pd.read_csv(INPUT_CSV)
    df = df.apply(clean_metadata, axis=1)

    print("🧹 Cleaning and formatting...")
    records = []
    for _, row in df.iterrows():
        record = {
            "id": f"{row['file']}_p{row['page']}",
            "text": row['text'].strip(),
            "metadata": {
                "unit": row.get("unit", ""),
                "chapter": row.get("chapter", ""),
                "chapter_title": row.get("chapter_title", ""),
                "grade_band": row.get("grade_band", ""),
                "disciplinary_core_ideas": row.get("disciplinary_core_ideas", []),
                "science_practices": row.get("science_practices", []),
                "crosscutting_concepts": row.get("crosscutting_concepts", []),
            }
        }
        records.append(record)

    print(f"💾 Writing {len(records)} chunks to JSONL for embedding...")
    with open(OUTPUT_JSONL, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print("✅ Ingestion complete.")

if __name__ == "__main__":
    main()
