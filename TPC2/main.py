import re

def split_line(line: str) -> list[str]:
    # Splits on semicolon only if an even number of quotes follows.
    fields = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    # Remove extra whitespace and any outer quotes from each field.
    return [field.strip().strip('"') for field in fields]

def process_dataset(file_path: str):
    composers = set()
    period_counts = {}        # period -> count of works
    works_by_period = {}      # period -> list of work titles

    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    
    if not lines:
        return [], {}, {}
    
    header = split_line(lines[0])
    try:
        idx_nome = header.index("nome")
        idx_periodo = header.index("periodo")
        idx_compositor = header.index("compositor")
    except ValueError as e:
        print("Error: Expected columns not found in header.")
        raise e

    record_lines = lines[1:]
    for line in record_lines:
        line = line.strip()
        if not line:
            continue
        fields = split_line(line)
        # Check if we have the expected number of fields.
        if len(fields) < 7:
            continue
        
        title = fields[idx_nome]
        period = fields[idx_periodo]
        composer = fields[idx_compositor]

        composers.add(composer)
        period_counts[period] = period_counts.get(period, 0) + 1
        works_by_period.setdefault(period, []).append(title)
    
    sorted_composers = sorted(composers)
    # Sort the list of titles for each period alphabetically.
    for p in works_by_period:
        works_by_period[p].sort()

    return sorted_composers, period_counts, works_by_period

if __name__ == '__main__':
    file_path = "TPC2/obras.csv"
    composers, period_counts, works_by_period = process_dataset(file_path)
    
    print("Lista ordenada alfabeticamente dos compositores:")
    for comp in composers:
        print(comp)
    
    print("\nDistribuição das obras por período:")
    for period, count in period_counts.items():
        print(f"{period}: {count}")
    
    print("\nDicionário (período -> títulos das obras):")
    for period, titles in works_by_period.items():
        print(f"{period}: {titles}")
