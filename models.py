from typing import List, Optional
from pydantic import BaseModel, Field


class Asset(BaseModel):
    symbol: str
    amount: float
    locked: bool = False
    current_path: Optional[str] = None


class Opportunity(BaseModel):
    id: str
    name: str
    type: str
    required_asset: str
    min_amount: float
    reward_score: int = Field(ge=0, le=100)
    risk_score: int = Field(ge=0, le=100)
    time_sensitive: bool = False


class AnalyzeRequest(BaseModel):
    user_goal: str
    assets: List[Asset]
    opportunities: List[Opportunity]


class MappedOpportunity(BaseModel):
    id: str
    name: str
    type: str
    feasible: bool
    matched_asset: Optional[str] = None
    available_amount: float = 0.0
    reward_score: int
    risk_score: int
    time_sensitive: bool
    notes: List[str] = []


class ConflictItem(BaseModel):
    opportunity_id: str
    level: str
    message: str


class RankedAction(BaseModel):
    id: str
    name: str
    score: float
    reason: str
    feasible: bool


class AnalyzeResponse(BaseModel):
    user_goal_recognition: str
    best_action: Optional[RankedAction]
    second_best_action: Optional[RankedAction]
    not_recommended_actions: List[RankedAction]
    conflicts: List[ConflictItem]
    asset_restrictions: List[str]
    action_checklist: List[str]
