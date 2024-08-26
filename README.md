# MEMEFI AUTO

## Persiapan

Pastikan kamu sudah install:

- [Python](https://www.python.org/downloads/release/python-31014/) **version 3.10**

## Cara Ambil Query ID

<https://irhamdz.notion.site/Tutorial-ambil-Query-ID-f415621d4a9843d2a7a9ad2cfb9abeb4?pvs=4>

## Request API KEY

Kamu bisa request API KEY di private channel telegram dzuhri-auto. (limited)

## Install

git clone ke pc / vps kamu:

```shell
git clone https://github.com/dzuhri-auto/memefi
```

Masuk ke folder nya

```shell
cd memefi
```

Lalu bisa pake command dibawah untuk otomatis install:

**Windows** :

```shell
install.bat
```

**Mac / Linux / VPS** :

```shell
. ubuntu/install.sh
```

## update API KEY

Setelah install lalu kita update API KEY kita:

**Windows** :

```shell
$filePath = ".env"
$searchPattern = "^API_KEY="
$replacement = 'API_KEY="GANTI PAKE API KEY KAMU"'

(Get-Content $filePath) -replace $searchPattern + '.*', $replacement | Set-Content $filePath
```

**Mac / Linux / VPS** :

```shell
sed -i~ '/^API_KEY=/s/=.*/="GANTI PAKE API KEY KAMU"/' .env

# contoh misalkan API KEY kamu "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Start Bot

Untuk menjalankan bot bisa pake command dibawah ini:

**Windows** :

```shell
run.bat
```

**Mac / Linux / VPS** :

```shell
. ubuntu/run.sh
```

## Update Bot

Untuk update bot bisa pake command dibawah ini:

**Windows** :

```shell
update.bat
```

**Mac / Linux / VPS** :

```shell
. ubuntu/update.sh
```
