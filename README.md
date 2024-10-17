# npbot

New version of a Neopets bot that uses multiple accounts to trade with itself and get money.

- Changes from previous version
    - Clientless architecture
    - Workers deal with account data

## Architecture Design

- API
    - Data Classes
        - Account -- stores immutable account data
        - Session -- stores mutable session data
    - Action Classes
        - Worker -- executes web requests
    - Helper Classes
        - DB -- helps store data

## Setup

#### Installation
```bash
git clone https://github.com/esgameco/npbot.git
pip install -r requirements.txt
```

#### Secrets
```bash
cp .env.template .env
```