from models import AnalyzeRequest, Asset, Opportunity


def get_demo_request() -> AnalyzeRequest:
    return AnalyzeRequest(
        user_goal="I only want to do the most worthwhile low-risk thing on Binance today",
        assets=[
            Asset(symbol="USDT", amount=500, locked=False, current_path="flexible_earn"),
            Asset(symbol="BNB", amount=3, locked=False, current_path=None),
        ],
        opportunities=[
            Opportunity(
                id="launchpool_alpha",
                name="Launchpool Alpha",
                type="launchpool",
                required_asset="USDT",
                min_amount=100,
                reward_score=85,
                risk_score=25,
                time_sensitive=True,
            ),
            Opportunity(
                id="earn_bonus",
                name="Simple Earn Bonus",
                type="earn",
                required_asset="USDT",
                min_amount=50,
                reward_score=60,
                risk_score=10,
                time_sensitive=False,
            ),
            Opportunity(
                id="trade_competition",
                name="Spot Trading Challenge",
                type="trading_competition",
                required_asset="USDT",
                min_amount=200,
                reward_score=78,
                risk_score=60,
                time_sensitive=True,
            ),
        ],
    )
