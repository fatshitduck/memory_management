def validate_blocks(blocks):
    if not blocks:
        raise ValueError("Blocks list is empty")
    ids = set()
    for b in blocks:
        if "block_id" not in b or "size" not in b:
            raise ValueError("Invalid block format")
        if not isinstance(b["block_id"], str) or b["block_id"] == "":
            raise ValueError("block_id must be a non-empty string")
        if b["block_id"] in ids:
            raise ValueError(f"Duplicate block_id: {b['block_id']}")
        if not isinstance(b["size"], int):
            raise ValueError(f"size must be integer in block {b['block_id']}")
        if b["size"] <= 0:
            raise ValueError(f"size must be > 0 in block {b['block_id']}")
        ids.add(b["block_id"])
def validate_processes(processes):
    if not processes:
        raise ValueError("Processes list is empty")
    ids = set()
    for p in processes:
        if "process_id" not in p or "size" not in p:
            raise ValueError("Invalid process format")

        if not isinstance(p["process_id"], str) or p["process_id"] == "":
            raise ValueError("process_id must be a non-empty string")

        if p["process_id"] in ids:
            raise ValueError(f"Duplicate process_id: {p['process_id']}")

        if not isinstance(p["size"], int):
            raise ValueError(f"size must be integer in process {p['process_id']}")

        if p["size"] <= 0:
            raise ValueError(f"size must be > 0 in process {p['process_id']}")

        ids.add(p["process_id"])