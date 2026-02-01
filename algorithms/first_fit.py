def first_fit(blocks, processes):
    memory_blocks = []
    for b in blocks:
        memory_blocks.append({
            "block_id": b["block_id"],
            "size": b["size"]
        })

    results = []

    for p in processes:
        allocated = False

        for block in memory_blocks:
            if block["size"] >= p["size"]:
                remaining = block["size"] - p["size"]

                results.append([
                    p["process_id"],
                    p["size"],
                    block["block_id"],
                    remaining,
                    "Allocated"
                ])

                block["size"] = remaining
                allocated = True
                break

        if not allocated:
            results.append([
                p["process_id"],
                p["size"],
                "-",
                "-",
                "Failed"
            ])

    return results
