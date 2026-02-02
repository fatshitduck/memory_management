import csv
def read_blocks(filename):
    blocks = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ["block_id", "size"]:
            raise ValueError("Invalid header for blocks.csv")
        for row in reader:
            blocks.append({
                "block_id": row["block_id"],
                "size": int(row["size"])
            })
    return blocks
def read_processes(filename):
    processes = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ["process_id", "size"]:
            raise ValueError("Invalid header for processes.csv")
        for row in reader:
            processes.append({
                "process_id": row["process_id"],
                "size": int(row["size"])
            })
    return processes