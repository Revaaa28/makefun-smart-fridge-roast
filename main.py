"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast of the smart fridge to /output/entry.txt.
The line roasts a real behaviour of the gadget: a smart fridge whose
ice dispenser refuses to work while the Wi-Fi is down, so the ice
cubes sit hostage until the router cooperates.
"""

import os

LINE = (
    "My smart fridge needs Wi-Fi to dispense ice, so my ice cubes "
    "are held hostage until the router feels like working."
)


def main() -> None:
    # Gate self-check: the sealed scorer wants 1-160 UTF-8 chars,
    # not only white space. Refuse to write a line that would fail it.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert LINE.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
