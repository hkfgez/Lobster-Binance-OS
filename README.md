Lobster Binance OS

A unified intent control and task orchestration layer for the Binance ecosystem.

Lobster Binance OS is an ecosystem-level intent router and task orchestration agent for Binance.

It does not merely summarize announcements.
It reorganizes fragmented activities, assets, tasks, risks, and execution paths into a unified action view based on the user's goal.

Core Modules

Opportunity Scanner

Asset & Eligibility Mapper

Conflict Resolver

Priority Engine

Action Checklist Generator

What It Solves

Binance does not lack products, campaigns, or opportunities.
What users often lack is a unified layer that tells them what to do now, in what order, and what not to touch.

Lobster Binance OS addresses:

Fragmented ecosystem entry points

Conflicts between assets and opportunity paths

Poor action prioritization across campaigns, Earn, Launchpool, and tasks

High decision cost for ordinary users

Lack of a unified action view based on the user's real goal

Workflow

Parse the user's goal, link, text, screenshot, or account context

Scan current opportunities in the ecosystem

Map assets, eligibility, and path constraints

Detect conflicts between actions, assets, and existing paths

Rank actions based on user goal, risk, efficiency, and timing

Generate a final action checklist

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload

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
Example Output Logic

The system is designed to return:

User goal recognition

Best current action

Second-best action

Not recommended actions

Asset restrictions

Conflict analysis

Final action checklist

Repository Structure
.
├── engine/
│   ├── scanner.py
│   ├── mapper.py
│   ├── resolver.py
│   ├── priority.py
│   └── checklist.py
├── examples/
│   ├── scenario_1.json
│   ├── scenario_2.json
│   └── scenario_3.json
├── app.py
├── main.py
├── models.py
├── requirements.txt
└── sample_data.py
Demo Scenarios
Scenario 1

A goal-driven ecosystem orchestration case:
“I only want to do the most worthwhile low-risk thing on Binance today.”

Scenario 2

An asset path conflict case:
“This USDT may already be in an existing path. Should I move it to a new campaign?”

Scenario 3

A daily action prioritization case:
“Based on my account, tell me what I should do first today and what not to do.”

Notes

This repository is a prototype built for demonstration and competition submission.
It focuses on orchestration logic, prioritization, conflict detection, and action checklist generation.

It is not a blind auto-trading bot, and it does not assume unrestricted account control.
Its purpose is to provide a unified action view for users navigating a fragmented Binance ecosystem.
