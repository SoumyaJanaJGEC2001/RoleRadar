from pathlib import Path
import csv


def create_source_registry() -> None:
    project_root = Path(__file__).resolve().parent
    config_directory = project_root / "configs"
    output_file = config_directory / "source_registry.csv"

    columns = [
        "source_id",
        "company_name",
        "careers_url",
        "ats_provider",
        "board_identifier",
        "source_tier",
        "geography",
        "relevant_roles",
        "public_access",
        "login_required",
        "terms_reviewed_date",
        "collection_frequency",
        "approval_status",
        "notes",
    ]

    config_directory.mkdir(parents=True, exist_ok=True)

    if output_file.exists():
        print(f"File already exists: {output_file}")
        return

    with output_file.open(
        mode="w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()

    print(f"Created source registry: {output_file}")


if __name__ == "__main__":
    create_source_registry()