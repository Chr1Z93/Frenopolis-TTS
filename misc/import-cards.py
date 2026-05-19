import csv
import json
from pathlib import Path

# Config
OUTPUT = Path(r"C:\git\Frenopolis-TTS\objects\AllCards.144e8e")
DATA_CSV = "frenopolis-card-data.csv"


class TTSCardGenerator:
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def build_individual_cards(self, csv_path):
        print(f"Reading data from {csv_path}...")

        with open(csv_path, mode="r", encoding="utf-8-sig") as f:
            # Assumes the CSV has a header row
            reader = csv.DictReader(f)

            for i, row in enumerate(reader):
                if "NAME" not in row:
                    print(f"Skipped Row {i}: Missing Name")
                    continue

                card_name = row.get("NAME", "")

                # Create Card
                card = {}
                card["Name"] = "Card"
                card["Transform"] = {"rotY": 270, "scaleX": 1, "scaleY": 1, "scaleZ": 1}
                card["Nickname"] = card_name
                card["GUID"] = f"FREN{i:03}"

                # Add metadata
                card["GMNotes"] = json.dumps(
                    {
                        "type": row.get("TYPE", ""),
                        "subType": row.get("SUB TYPE", ""),
                        "stat": row.get("STAT", ""),
                        "colorCost": row.get("COLOR COST", ""),
                        "colorlessCost": row.get("COLORLESS COST", ""),
                        "color": row.get("COLOR", ""),
                        "deck": row.get("DECK", ""),
                    },
                    ensure_ascii=False,
                )

                # Determine file name
                owner = f"{row.get("DECK",'').lower()} deck"
                img_file = f"{owner}\\{card_name}"

                # Custom Deck / URL handling
                deck_id = str(i + 1)
                card["CardID"] = f"{deck_id}00"
                card["CustomDeck"] = {
                    deck_id: {
                        "FaceURL": img_file,
                        "BackURL": "https://steamusercontent-a.akamaihd.net/ugc/9621278958948081727/F5E1D3F37F160C70F8D55986CDE569A329C17191/",
                        "NumWidth": 1,
                        "NumHeight": 1,
                        "BackIsHidden": True,
                        "UniqueBack": False,
                        "Type": 0,
                    }
                }

                # Save as an individual JSON file
                safe_filename = "".join(c for c in card_name if c.isalnum()).rstrip()
                out_name = f"{safe_filename}.FREN{i:03}.json"
                out_path = self.output_folder / out_name

                with open(out_path, "w", encoding="utf-8") as out_f:
                    json.dump(card, out_f, indent=4, ensure_ascii=False)

                print(f"Created: {out_name}")


if __name__ == "__main__":
    generator = TTSCardGenerator(OUTPUT)
    generator.build_individual_cards(DATA_CSV)
