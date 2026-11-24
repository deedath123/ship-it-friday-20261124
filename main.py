"""Ship It Friday entry generator."""

import os


ENTRY = "feat: deploy Friday 4:58pm \u2014 Maya said never touch prod, so I renamed prod to staging. Problem solved!"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
