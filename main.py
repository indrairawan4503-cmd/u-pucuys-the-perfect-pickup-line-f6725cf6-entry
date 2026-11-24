import os

LINE = ("Before you finished saying 'coffee?', I'd already said yes. I've been autocompleting you since hello — care to test me over coffee and see what I predict next?")

def resolve_output_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    if os.path.isdir(out):
        return os.path.join(out, "entry.txt")
    return out

def validate_entry(text):
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry validation failed: length must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry validation failed: entry must be a single line (no newline character inside)")
    if text != text.strip():
        raise SystemExit("entry validation failed: entry must have no leading/trailing whitespace")
    if "  " in text:
        raise SystemExit("entry validation failed: entry must have no double spaces")

def write_entry(path, text):
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)

def main():
    validate_entry(LINE)
    text = LINE + "\n"
    write_entry(resolve_output_path(), text)
    try:
        write_entry(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), text)
    except OSError:
        pass

if __name__ == "__main__":
    main()
