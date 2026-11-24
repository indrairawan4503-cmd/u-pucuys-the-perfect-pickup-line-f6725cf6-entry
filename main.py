import os

LINE = ("Before you finished saying 'coffee?', I'd already said yes. I've been autocompleting you since hello — care to test me over coffee and see what I predict next?")

def resolve_output_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    if os.path.isdir(out):
        return os.path.join(out, "entry.txt")
    return out

def write_entry(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    text = LINE + "\n"
    write_entry(resolve_output_path(), text)
    try:
        write_entry(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), text)
    except OSError:
        pass

if __name__ == "__main__":
    main()
