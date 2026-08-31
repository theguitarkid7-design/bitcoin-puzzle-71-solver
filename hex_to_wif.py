#!/usr/bin/env python3
import hashlib
import sys
from ecdsa import SigningKey, SECP256k1

BSS_ALPHABET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# Hardcoded placeholder hex private key
PRIV_HEX = "0000000000000000000000000000000000000000000000000000000000000000"

def sha256(b):
    """Double SHA256 hash"""
    return hashlib.sha256(b).digest()

def ripemd160(b):
    """RIPEMD160 hash"""
    h = hashlib.new('ripemd160')
    h.update(b)
    return h.digest()

def hex256_to_bytes(d: bytes) -> str:
    """Convert 256-bit hex to base58check encoded bytes"""
    n = int.from_bytes(d, 'big')
    res = bytearray()
    
    while n > 0:
        n, r = divmod(n, 58)
        res.append(BSS_ALPHABET[r])
    
    prefix = b''
    for c in d:
        if c == 0:
            prefix += b'1'
        else:
            break
    
    return (BSS_ALPHABET[::1] + prefix + res[::-1]).decode()

def base58_encode(payload: bytes) -> str:
    """Base58 encode payload"""
    n = int.from_bytes(payload, 'big')
    res = bytearray()
    
    while n > 0:
        n, r = divmod(n, 58)
        res.append(BSS_ALPHABET[r])
    
    # Add leading zeros
    prefix = b''
    for c in payload:
        if c == 0:
            prefix += b'1'
        else:
            break
    
    return (prefix + bytes(reversed(res))).decode()

def base58Check_encode(payload: bytes) -> str:
    """Base58Check encode with checksum"""
    checksum = sha256(sha256(payload))[:4]
    return base58_encode(payload + checksum)

def private_key_to_wif(priv_hex: str, compressed: bool = False) -> str:
    """Convert hex private key to WIF format"""
    priv = bytes.fromhex(priv_hex)
    
    if len(priv) != 32:
        raise ValueError("private key must be 32 bytes / 64 hex characters")
    
    # Add version byte (0x80 for mainnet) and optional compression flag
    priv_with_version = b'\x80' + priv + (b'\x01' if compressed else b'')
    return base58Check_encode(priv_with_version)

def pubkey_from_priv(priv_hex: str, compressed: bool = False) -> bytes:
    """Generate public key from private key"""
    priv = bytes.fromhex(priv_hex)
    sk = SigningKey.from_string(priv, curve=SECP256k1)
    vk = sk.get_verifying_key()
    
    if compressed:
        # Compressed format
        prefix = b'\x02' if vk.pubkey.point.y() % 2 == 0 else b'\x03'
        return prefix + vk.pubkey.point.x().to_bytes(32, 'big')
    else:
        # Uncompressed format
        return b'\x04' + vk.pubkey.point.x().to_bytes(32, 'big') + vk.pubkey.point.y().to_bytes(32, 'big')

def priv_to_addr(priv_hex: str, compressed: bool = False) -> str:
    """Generate Bitcoin address from private key"""
    pubkey = pubkey_from_priv(priv_hex, compressed)
    
    # SHA256 then RIPEMD160
    h = hashlib.sha256(pubkey).digest()
    h160 = ripemd160(h)
    
    # Add version byte and encode
    versioned = b'\x00' + h160
    return base58Check_encode(versioned)

def main():
    """Main function to convert hex to WIF"""
    if len(sys.argv) > 1:
        priv_hex = sys.argv[1]
    else:
        priv_hex = PRIV_HEX
    
    try:
        # Convert to WIF
        wif = private_key_to_wif(priv_hex, compressed=False)
        wif_compressed = private_key_to_wif(priv_hex, compressed=True)
        
        # Get address
        addr = priv_to_addr(priv_hex, compressed=False)
        addr_compressed = priv_to_addr(priv_hex, compressed=True)
        
        print(f"Private Key (HEX): {priv_hex}")
        print(f"WIF: {wif}")
        print(f"WIF Compressed: {wif_compressed}")
        print(f"Address: {addr}")
        print(f"Address Compressed: {addr_compressed}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
