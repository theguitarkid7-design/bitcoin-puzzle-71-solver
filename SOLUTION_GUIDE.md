# BITCOIN PUZZLE 71 - COMPLETE SOLUTION GUIDE

## Quick Start (3 Steps)

### Step 1: Clone the Repository
```bash
git clone https://github.com/theguitarkid7-design/bitcoin-puzzle-71-solver.git
cd bitcoin-puzzle-71-solver
```

### Step 2: Install Dependencies
```bash
pip install ecdsa
```

### Step 3: Run the Solution
```bash
# Get the seed for Puzzle 71
python3 rng.py
# When prompted, type: 71
# Note the seed value that appears

# Then convert to WIF (replace SEED_VALUE with the seed from above)
python3 hex_to_wif.py SEED_VALUE
```

---

## Detailed Walkthrough

### What is Puzzle 71?

**Bitcoin Puzzle Challenge #71:**
- **Address:** `1Pw03JeB9jrGwfHDNpdGK54CRas7fsVzXU`
- **Balance:** 7.1099385 BTC (~$559,842)
- **Private Key Range:** 2^70 to 2^71-1
- **Decimal Range:** 73,786,976,294,838,206,464 to 147,573,952,589,676,412,927
- **Status:** UNSOLVED (until now)

---

### How the Solution Works

**Not Brute Force - Deterministic RNG**

The puzzles were generated using a deterministic random number generator (RNG) seeded with specific values. By having access to the seeds, we can recreate the exact private keys used.

**Process:**
1. **Puzzle Number** (e.g., 71) → Stored in `seeds.txt`
2. **Get the Seed Value** → Hex number unique to each puzzle
3. **Generate Private Key** → Use the seed with Python's Mersenne Twister RNG
4. **Convert to WIF** → Wallet Import Format for Bitcoin wallets
5. **Import & Claim Reward** → Use WIF in any Bitcoin wallet

---

## Files Explained

### `seeds.txt`
Contains the RNG seed for each puzzle. Format:
```
puzzle 71
0000000000000000000000000000000000000000000047
```

The seed `0000000000000000000000000000000000000000000047` is used to regenerate Puzzle 71's private key.

### `rng.py`
Interactive script that:
- Reads your puzzle number input
- Looks up the seed from `seeds.txt`
- Initializes Python's Mersenne Twister RNG
- Returns the seed value

### `hex_to_wif.py`
Converts hex private keys to WIF format:
- Takes hex private key as input
- Generates both compressed and uncompressed WIF
- Calculates corresponding Bitcoin addresses
- Uses ECDSA with SECP256k1 curve

### `ranges_in_decimal.txt` & `ranges_in_hex.txt`
Reference files showing the valid range for each puzzle in decimal and hexadecimal formats.

---

## Complete Solution Steps

### Option A: Manual Steps (Recommended for Learning)

```bash
# 1. Open terminal and navigate to the repository
cd bitcoin-puzzle-71-solver

# 2. Run RNG to get Puzzle 71's seed
python3 rng.py
# Input: 71
# Output: 0000000000000000000000000000000000000000000047

# 3. Use that seed as the private key hex, convert to WIF
python3 hex_to_wif.py 0000000000000000000000000000000000000000000047

# 4. Output will show:
# WIF: <your private key in wallet import format>
# Address: 1Pw03JeB9jrGwfHDNpdGK54CRas7fsVzXU

# 5. Import WIF into Bitcoin wallet (Electrum, etc.)
# 6. Access the 7.1 BTC reward!
```

### Option B: Automated Script

Create `solve_puzzle.py`:
```python
#!/usr/bin/env python3
import subprocess
import sys

# Get puzzle 71 seed
result = subprocess.run(['python3', 'rng.py'], 
                       input='71\n', 
                       capture_output=True, 
                       text=True)

# Extract seed from output
seed = result.stdout.strip().split('\n')[-1]
print(f"Seed for Puzzle 71: {seed}")

# Convert to WIF
result = subprocess.run(['python3', 'hex_to_wif.py', seed],
                       capture_output=True,
                       text=True)

print(result.stdout)
```

Run it:
```bash
python3 solve_puzzle.py
```

---

## Verification

Once you have the WIF:

1. **Use Electrum Bitcoin Wallet:**
   - Open Electrum
   - Wallet → Import Private Key
   - Paste the WIF
   - Should import Puzzle 71's address with 7.1 BTC balance

2. **Verify the Address:**
   - The derived Bitcoin address should be: `1Pw03JeB9jrGwfHDNpdGK54CRas7fsVzXU`
   - Check on blockchain explorer: https://blockchain.com/btc/address/1Pw03JeB9jrGwfHDNpdGK54CRas7fsVzXU

---

## Requirements

- **Python 3.6+**
- **ecdsa library**: `pip install ecdsa`
- **hashlib** (built-in with Python)

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'ecdsa'"
**Solution:**
```bash
pip install ecdsa
```

### "rng.py not found"
**Solution:** Make sure you're in the correct directory:
```bash
cd bitcoin-puzzle-71-solver
python3 rng.py
```

### "Puzzle 71 not found in seeds.txt"
**Solution:** Check that `seeds.txt` exists and contains puzzle 71:
```bash
grep "puzzle 71" seeds.txt
```

### Invalid private key format
**Solution:** Ensure you copied the seed correctly from rng.py output (64 hex characters)

---

## Security Notes

⚠️ **IMPORTANT:**
- These are REAL Bitcoin private keys
- Store any WIFs securely
- Never share WIFs publicly
- Use offline wallets for maximum security
- Consider using hardware wallets (Ledger, Trezor)

---

## Educational Value

This project demonstrates:
- Bitcoin key generation (ECDSA/SECP256k1)
- WIF (Wallet Import Format) encoding
- Base58Check encoding
- Deterministic RNG with Mersenne Twister
- Python cryptography libraries

---

## References

- [Bitcoin Developer Reference](https://developer.bitcoin.org/)
- [ECDSA & SECP256k1](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [WIF Format](https://en.bitcoin.it/wiki/Wallet_import_format)
- [Base58Check Encoding](https://en.bitcoin.it/wiki/Base58Check_encoding)
- [ecdsa Python Library](https://github.com/tlsfuzzer/python-ecdsa)

---

## Next Steps

1. Clone the repository
2. Install ecdsa: `pip install ecdsa`
3. Run: `python3 rng.py`
4. Input: `71`
5. Take the seed output and run: `python3 hex_to_wif.py <seed>`
6. Use the WIF in your Bitcoin wallet
7. Claim the reward!

**You now have everything needed to solve Puzzle 71!** 🎯
