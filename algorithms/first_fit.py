import csv

def allocate_first_fit(blocks_csv, processes_csv, output_csv):
    memory_blocks = []
    with open(blocks_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            memory_blocks.append({
                "block_id": row["block_id"],
                "size": int(row["size"])
            })

    results = []

    with open(processes_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for process in reader:
            process_id = process["process_id"]
            process_size = int(process["size"])
            allocated = False

            for block in memory_blocks:
                if block["size"] >= process_size:
                    remaining = block["size"] - process_size

                    results.append({
                        "process_id": process_id,
                        "process_size": process_size,
                        "block_id": block["block_id"],
                        "remaining": remaining,
                        "status": "Allocated"
                    })

                    block["size"] = remaining
                    allocated = True
                    break  # First-Fit

            if not allocated:
                results.append({
                    "process_id": process_id,
                    "process_size": process_size,
                    "block_id": "-",
                    "remaining": "-",
                    "status": "Failed"
                })
    with open(output_csv, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["process_id", "process_size", "block_id", "remaining", "status"]
        )
        writer.writeheader()
        writer.writerows(results)
