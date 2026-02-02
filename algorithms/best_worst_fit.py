import csv
import copy

def read_blocks(filename):
    blocks = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            blocks.append({
                "block_id": row["block_id"],
                "size": int(row["size"])
            })
    return blocks


def read_processes(filename):
    processes = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            processes.append({
                "process_id": row["process_id"],
                "size": int(row["size"])
            })
    return processes


def best_fit(blocks, processes):
    blocks = copy.deepcopy(blocks)
    output = []

    for p in processes:
        best_block = None

        for b in blocks:
            if b["size"] >= p["size"]:
                if best_block is None or b["size"] < best_block["size"]:
                    best_block = b

        if best_block:
            remaining = best_block["size"] - p["size"]
            output.append([
                p["process_id"],
                p["size"],
                best_block["block_id"],
                remaining,
                "Allocated"
            ])
            best_block["size"] = remaining
        else:
            output.append([
                p["process_id"],
                p["size"],
                "-",
                "-",
                "Failed"
            ])

    return output


def worst_fit(blocks, processes):
    blocks = copy.deepcopy(blocks)
    output = []

    for p in processes:
        worst_block = None

        for b in blocks:
            if b["size"] >= p["size"]:
                if worst_block is None or b["size"] > worst_block["size"]:
                    worst_block = b

        if worst_block:
            remaining = worst_block["size"] - p["size"]
            output.append([
                p["process_id"],
                p["size"],
                worst_block["block_id"],
                remaining,
                "Allocated"
            ])
            worst_block["size"] = remaining
        else:
            output.append([
                p["process_id"],
                p["size"],
                "-",
                "-",
                "Failed"
            ])

    return output


def write_output(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["process_id", "process_size", "block_id", "remaining", "status"])
        writer.writerows(data)


if __name__ == "__main__":
    blocks = read_blocks("blocks.csv")
    processes = read_processes("processes.csv")

    best_fit_result = best_fit(blocks, processes)
    write_output("best_fit_output.csv", best_fit_result)

    worst_fit_result = worst_fit(blocks, processes)
    write_output("worst_fit_output.csv", worst_fit_result)
