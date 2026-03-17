# Lobster Binance OS

A unified intent control and task orchestration layer for the Binance ecosystem.

Lobster Binance OS is an ecosystem-level intent router and task orchestration agent for Binance.

It does not merely summarize announcements.  
It reorganizes fragmented activities, assets, tasks, risks, and execution paths into a unified action view based on the user's goal.

## Core Modules

- Opportunity Scanner
- Asset & Eligibility Mapper
- Conflict Resolver
- Priority Engine
- Action Checklist Generator

## What It Solves

Binance does not lack products, campaigns, or opportunities.  
What users often lack is a unified layer that tells them what to do now, in what order, and what not to touch.

Lobster Binance OS addresses:

- Fragmented ecosystem entry points
- Conflicts between assets and opportunity paths
- Poor action prioritization across campaigns, Earn, Launchpool, and tasks
- High decision cost for ordinary users
- Lack of a unified action view based on the user's real goal

## Workflow

1. Parse the user's goal, link, text, screenshot, or account context
2. Scan current opportunities in the ecosystem
3. Map assets, eligibility, and path constraints
4. Detect conflicts between actions, assets, and existing paths
5. Rank actions based on user goal, risk, efficiency, and timing
6. Generate a final action checklist

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
Local API docs will be available at:

- `http://127.0.0.1:8000/docs`
Example API

POST /analyze
{
  "user_goal": "I only want to do the most worthwhile low-risk thing on Binance today",
  "assets": [
    {
      "symbol": "USDT",
      "amount": 500,
      "locked": false,
      "current_path": "flexible_earn"
    },
    {
      "symbol": "BNB",
      "amount": 3,
      "locked": false,
      "current_path": null
    }
  ],
  "opportunities": [
    {
      "id": "launchpool_alpha",
      "name": "Launchpool Alpha",
      "type": "launchpool",
      "required_asset": "USDT",
      "min_amount": 100,
      "reward_score": 85,
      "risk_score": 25,
      "time_sensitive": true
    },
    {
      "id": "earn_bonus",
      "name": "Simple Earn Bonus",
      "type": "earn",
      "required_asset": "USDT",
      "min_amount": 50,
      "reward_score": 60,
      "risk_score": 10,
      "time_sensitive": false
    },
    {
      "id": "trade_competition",
      "name": "Spot Trading Challenge",
      "type": "trading_competition",
      "required_asset": "USDT",
      "min_amount": 200,
      "reward_score": 78,
      "risk_score": 60,
      "time_sensitive": true
    }
  ]
}
