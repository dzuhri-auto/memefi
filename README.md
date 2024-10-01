# Memefi AUTO

Memefi Telegram Mini App Bot Auto</br>
*(Requires Only Query ID)*

> [!NOTE]
> This is a paid script that requires a valid license key to operate. For more information, please visit the [Dzuhri Auto](https://irhamdz.notion.site/Dzuhri-Auto-10f53e55353080f98fbae250bd7172d1) page.

## Supported Operating Systems

- VPS
- Windows
- Mac
- Android (using Termux)

## Prerequisites

Before setting up the bot, ensure the following are installed:

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/) (version 3.10.0 - 3.11.9)

## Features

- Auto Tap
- Auto Use Booster
- Auto Refill Energy
- Auto Upgrade Boost
- Auto Play Slot Machine
- Auto Use Bot Tap
- Auto Clear missions 🔥🔥🔥 *(not all missions)*
- Can be run all days 24/7

## .env Settings

All the configurations can be set in the .env file.

| Name                 | Description                             | Default  |
| -------------------- | --------------------------------------- | -------- |
| LICENSE_KEY          | Dzuhri Auto License Key                 |          |
| MIN_AVAILABLE_ENERGY | Minimum energy to tap                   | 100      |
| SLEEP_BY_MIN_ENERGY  | Delay seconds when reach minimum energy | 1800     |
| ADD_TAPS_ON_TURBO    | Add more tap point when turbo activated | 2500     |
| AUTO_UPGRADE_TAP     | Auto upgrade tap                        | True     |
| MAX_TAP_LEVEL        | Maximum tap level to upgrade            | 5        |
| AUTO_UPGRADE_ENERGY  | Auto upgrade energy                     | True     |
| MAX_ENERGY_LEVEL     | Maximum energy level to upgrade         | 5        |
| AUTO_UPGRADE_CHARGE  | Auto upgrade charge                     | True     |
| MAX_CHARGE_LEVEL     | Maximum charge level to upgrade         | 3        |
| APPLY_DAILY_ENERGY   | Auto use daily energy potion            | True     |
| APPLY_DAILY_TURBO    | Auto use daily turbo potion             | False    |
| RANDOM_TAPS_COUNT    | Randomize point per taps                | [15, 75] |
| SLEEP_BETWEEN_TAP    | Delay seconds between each tap          | [30, 60] |
| ACTIVE_TURBO_DELAY   | Delay seconds when turbo activated      | 10       |
| USE_PROXY_FROM_FILE  | For using proxy                         | False    |
| USE_TAP_BOT          | Auto use bot tap (if already buy)       | True     |
| EMERGENCY_STOP       | Emergency stop                          | False    |
| AUTO_CLEAR_MISSION   | Auto clear mission                      | True     |
| AUTO_SPIN            | Auto Play Slot Machine                  | False    |

## How to obtain and use Query ID

To get the Query ID, [read this guide.](https://irhamdz.notion.site/Tutorial-Get-Query-ID-f415621d4a9843d2a7a9ad2cfb9abeb4?pvs=74)

Once you have the Query ID, add it to the `query_ids.txt` file.</br>
If you're using multiple accounts, simply add each query ID on a new line, like this:

```bash
query_id=xxxxxxxxx-User1
query_id=xxxxxxxxx-User2
```

## How to Use Proxy

To use proxy, [read this guide.](https://irhamdz.notion.site/Use-Proxy-11153e553530807aaa14fdfde425723c?pvs=74)

To buy cheap proxy, [buy cheap proxy here](https://proxy-seller.com/?partner=QJGZSHEU86WI9Y)

## Installation Guide

### Step 1: Clone the Repository to Your PC / VPS

Run the following command to clone the repository:

```shell
git clone https://github.com/dzuhri-auto/memefi.git
```

### Step 2: Navigate to the Project Folder

Once cloned, navigate to the project directory:

```shell
cd memefi
```

### Step 3: Install the Dependencies

Run the following commands based on your operating system:

**Windows (Using Powershell)** :

```powershell
py -m venv venv
.\venv\Scripts\Activate
pip3 install wheel
pip3 install -r requirements.txt
cp .env-example .env
```

**Mac / Linux** :

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
cp .env-example .env
```

***Note : dont forget to edit `.env` file***

## Using the License Key

After installation, you can input your license key in the .env file as follows:

```note
LICENSE_KEY="Your License Key"
```

[Buy the license key](https://irhamdz.notion.site/Dzuhri-Auto-10f53e55353080f98fbae250bd7172d1)

## Starting the Bot

Run the bot using the following commands, depending on your operating system:

**Windows (Using Powershell)** :

```powershell
.\venv\Scripts\Activate
py main.py
```

**Mac / Linux** :

```shell
source venv/bin/activate
python3 main.py
```
