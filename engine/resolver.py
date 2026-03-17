from typing import List
from models import Asset, MappedOpportunity, ConflictItem


def detect_conflicts(assets: List[Asset], mapped: List[MappedOpportunity]) -> List[ConflictItem]:
    conflicts: List[ConflictItem] = []

    for item in mapped:
        if not item.feasible:
            conflicts.append(
                ConflictItem(
                    opportunity_id=item.id,
                    level="medium",
                    message=f"{item.name} is currently not feasible: {'; '.join(item.notes)}",
                )
            )

        for asset in assets:
            if (
                item.matched_asset == asset.symbol
                and asset.current_path
                and item.type != asset.current_path
            ):
                conflicts.append(
                    ConflictItem(
                        opportunity_id=item.id,
                        level="high",
                        message=(
                            f"{asset.symbol} is currently used in path '{asset.current_path}', "
                            f"switching to '{item.type}' may cause path conflict or opportunity loss."
                        ),
                    )
                )

    return conflicts


def summarize_asset_restrictions(assets: List[Asset]) -> List[str]:
    restrictions: List[str] = []

    for asset in assets:
        if asset.locked:
            restrictions.append(f"{asset.symbol} is locked and should not be moved.")
        elif asset.current_path:
            restrictions.append(
                f"{asset.symbol} is currently allocated to '{asset.current_path}', avoid moving it without checking path impact."
            )

    return restrictions
