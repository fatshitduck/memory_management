def first_fit(blocks, processes):
    """
    First-Fit memory allocation (GUI-compatible)

    blocks: list of dict
        [{"block_id": "B1", "size": 100}, ...]

    processes: list of dict
        [{"process_id": "P1", "size": 212}, ...]

    return: list of list
        [process_id, process_size, block_id, remaining, status]
    """

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
                break  # First-Fit

        if not allocated:
            results.append([
                p["process_id"],
                p["size"],
                "-",
                "-",
                "Failed"
            ])

    return results
