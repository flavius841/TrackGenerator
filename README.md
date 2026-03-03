#  TrackGenerator

##  Overview

**TrackGenerator** is a command-line music discovery tool that fetches recordings based on genre or tag using the :contentReference[oaicite:0]{index=0} API.

If you feel stuck during travel or just want vibe-matching music, simply type a genre, country, or random tag and explore tracks instantly.

---

## Note

* This project is made for **TransitTime**.

##  Features

- Search music recordings by genre/tag  
- Interactive CLI mode  
- Pagination support (`more` command)  
- Random discovery using uncommon tags  
- Terminal colored output  
- Network-safe API requests with throttling protection  

---

## Prerequisites

To run this project, you need to have **Python** and **Git** installed on your system.

---
If you already have Python and Git, you can jump to the Running the CLI section.


---

## Installing Python

### **macOS**

1. Go to the official site: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. Download the `.pkg` installer.
3. Open it and follow the instructions.

Then, install **pipx**:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Restart your terminal after running `ensurepath`.

---

### **Linux (Ubuntu/Debian)**

Install Python:

```bash
sudo apt update
sudo apt install python3
```

Then, install pip and pipx:

```bash
sudo apt install python3-pip
sudo apt update
sudo apt install pipx
```

---

### **Windows**

1. Download Python from: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Run the installer.
   **Important:** Check the box **“Add Python to PATH”** before clicking “Install Now.”
3. After installation, install pipx:

```cmd
python -m pip install --user pipx
python -m pipx ensurepath
```

Restart Command Prompt after running `ensurepath`.

---

## Installing Git

### **macOS**

If you have Homebrew:

```bash
brew install git
```

### **Linux (Ubuntu/Debian)**

```bash
sudo apt update
sudo apt install git
```

### **Windows**

1. Go to: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the installer and follow the prompts (default options are fine).

---

## Running the CLI

After installing Python, pipx, and Git, you can install the CLI project:

```bash
pipx install git+https://github.com/flavius841/TrackGenerator.git
```

Now, you can run the CLI by typing:

```bash
trackgen
```

in your terminal or Command Prompt.

---
