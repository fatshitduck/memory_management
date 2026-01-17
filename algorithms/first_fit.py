def allocate(blocks, processes):
    """
    First-Fit memory allocation algorithm

    Parameters:
    - blocks: list of dict
        Example:
        [
            {"block_id": "B1", "size": 100},
            {"block_id": "B2", "size": 500}
        ]

    - processes: list of dict
        Example:
        [
            {"process_id": "P1", "size": 212}
        ]

    Returns:
    - list of dict (allocation result)
    """

    results = []

    # Make a copy so original blocks data is not modified outside
    memory_blocks = []
    for block in blocks:
        memory_blocks.append({
            "block_id": block["block_id"],
            "size": block["size"]
        })

    for process in processes:
        allocated = False

        for block in memory_blocks:
            if block["size"] >= process["size"]:
                # Allocate process to this block
                results.append({
                    "process_id": process["process_id"],
                    "process_size": process["size"],
                    "block_id": block["block_id"],
                    "block_size": block["size"],
                    "remaining": block["size"] - process["size"],
                    "status": "Allocated"
                })

                # Update remaining block size
                block["size"] -= process["size"]
                allocated = True
                break  # First-Fit → stop at first suitable block

        if not allocated:
            results.append({
                "process_id": process["process_id"],
                "process_size": process["size"],
                "status": "Not Allocated"
            })

    return results
