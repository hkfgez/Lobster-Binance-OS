# Lobster Binance OS

Lobster Binance OS is an ecosystem-level intent router and task orchestration agent for Binance.

It does not merely summarize announcements.  
It reorganizes fragmented activities, assets, tasks, risks, and execution paths into a unified action view based on the user's goal.

## Core Modules

- Opportunity Scanner
- Asset & Eligibility Mapper
- Conflict Resolver
- Priority Engine
- Action Checklist Generator

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
Open Swagger UI: http://127.0.0.1:8000/docs

Example API
POST /analyze{
  "user_goal": "I only want to do the most worthwhile low-risk thing on Binance today",
  "assets": [
    {
      "symbol": "USDT",
      "amount": 500,
      "locked": false,
      "current_path": "flexible_earn"
    }
  ],
  "opportunities": [
    {
      "id": "launchpool_1",
      "name": "Launchpool Alpha",
      "type": "launchpool",
      "required_asset": "USDT",
      "min_amount": 100,
      "reward_score": 85,
      "risk_score": 25,
      "time_sensitive": true
    },
    {
      "id": "earn_campaign_1",
      "name": "Simple Earn Bonus",
      "type": "earn",
      "required_asset": "USDT",
      "min_amount": 50,
      "reward_score": 60,
      "risk_score": 10,
      "time_sensitive": false
    }
  ]
}
