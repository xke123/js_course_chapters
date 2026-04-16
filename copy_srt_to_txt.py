from pathlib import Path


def main() -> None:
    base_dir = Path.cwd()
    srt_files = sorted(base_dir.glob("*.srt"))

    if not srt_files:
        print("No .srt files found in the current directory.")
        return

    created = 0
    for srt_file in srt_files:
        txt_file = srt_file.with_suffix(".txt")
        txt_file.write_text(srt_file.read_text(encoding="utf-8"), encoding="utf-8")
        created += 1
        print(f"Created: {txt_file.name}")

    print(f"Done. Created {created} .txt files.")


if __name__ == "__main__":
    main()
