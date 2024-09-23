# Memefi AUTO

Memefi Telegram Mini App Bot Auto

For README in English: [![en](https://img.shields.io/badge/README-en-red.svg)](https://github.com/dzuhri-auto/memefi/blob/master/README.md)

## Feature

- Auto Tap
- Auto Use Booster
- Auto Refill Energy
- Auto Upgrade Boost
- Auto Play Slot Machine
- Auto Use Bot Tap

## .env Settings

| Name                 | Description                             | Default  |
| -------------------- | --------------------------------------- | -------- |
| API_KEY              | Custom API KEY                          |          |
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

## Persiapan

Pastikan kamu sudah menginstal:

- [Python](https://www.python.org/downloads/release/python-31014/) **versi 3.10**

## Cara Mendapatkan Query ID

<https://irhamdz.notion.site/Tutorial-Get-Query-ID-f415621d4a9843d2a7a9ad2cfb9abeb4?pvs=74>



## Mendapatkan API KEY

Script ini menggunakan kustom API KEY, API KEY nya hanya tersedia untuk disewa.

Kamu bisa chat saya, [Irham](https://t.me/irhamdz) untuk menanyakan harga sewanya!

## Install

Clone ke PC / VPS kamu:

```shell
git clone https://github.com/dzuhri-auto/depin-alliance.git
```

Masuk ke folder:

```shell
cd depin-alliance
```

Kemudian gunakan perintah ini untuk instal otomatis:

**Windows** :

```shell
windows\install.bat
```

**Mac / Linux / VPS** :

```shell
sudo chmod +x ubuntu/install.sh ubuntu/run.sh
```

```shell
source ./ubuntu/install.sh
```

***note : Jangan lupa untuk mengedit file `.env`***

## Update API KEY

Setelah instalasi, kita bisa memperbarui menggunakan API KEY:

**Windows** :

```shell
$filePath = ".env"
$searchPattern = "^API_KEY="
$replacement = 'API_KEY="YOUR API KEY"'

(Get-Content $filePath) -replace $searchPattern + '.*', $replacement | Set-Content $filePath
```

**Mac / Linux / VPS** :

```shell
sed -i~ '/^API_KEY=/s/=.*/="YOUR API KEY"/' .env

# contoh jika API KEY kamu = "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Menjalankan Bot

Untuk menjalankan bot:

**Windows** :

```shell
windows\run.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/run.sh
```
