from typing import List
from models import MappedOpportunity, RankedAction


def _goal_prefers_low_risk(user_goal: str) -> bool:
    text = user_goal.lower()
    return "low-risk" in text or "low risk" in text or "稳健" in text or "低风险" in text


def rank_actions(user_goal: str, mapped: List[MappedOpportunity]) -> List[RankedAction]:
    ranked: List[RankedAction] = []
    prefer_low_risk = _goal_prefers_low_risk(user_goal)

    for item in mapped:
        if not item.feasible:
            score = -1
            reason = "Not feasible under current asset or eligibility constraints."
        else:
            score = float(item.reward_score)

            if prefer_low_risk:
                score -= item.risk_score * 0.8
            else:
                score -= item.risk_score * 0.3

            if item.time_sensitive:
                score += 8

            if item.type == "trading_competition" and prefer_low_risk:
                score -= 15

            reason = (
                f"Reward score={item.reward_score}, risk score={item.risk_score}, "
                f"time_sensitive={item.time_sensitive}, feasible={item.feasible}."
            )

        ranked.append(
            RankedAction(
                id=item.id,
                name=item.name,
                score=round(score, 2),
                reason=reason,
                feasible=item.feasible,
            )
        )

    ranked.sort(key=lambda x: x.score, reverse=True)
    return ranked
