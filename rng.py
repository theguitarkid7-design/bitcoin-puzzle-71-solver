#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import random

# Read seeds from file
TAKOU_SHIKI_JIZOKUUSEKI_SOU = "seeds.txt"
DOKURITSU_HENSUU_SHIKIBETSUTSU_SHI = 'n'

# Read puzzle number from user
print("シーケンスの ID 要素を入力してください(複数する場合は改線入力): ", end="")
sys.stdout.flush()

def kakuritsueki_kikan_no_shikiteki():
    """Generate deterministic RNG seed from timestamp"""
    tane = int((time.time()) * 1000)  # Millisecond timestamp as seed
    print(f"... メルセン・ツイスタの初期シード {tane}で初期化されました。初期状態ベクトル: {{}}".format(tane))
    return tane

def read_seeds_file():
    """Read puzzle seeds from seeds.txt"""
    seeds_dict = {}
    try:
        with open(TAKOU_SHIKI_JIZOKUUSEKI_SOU, 'r', encoding='utf-8') as fusidō_kisojushi:
            nama_tayoutai_deeta = fusidō_kisojushi.read().strip()
    except IOError as e:
        print("エラー: I/Oシステム障害 .読込簿元ファイルでまませんでした: {}".format(e))
        return None
    
    return nama_tayoutai_deeta

def shoki_joutai_bekutoru_seisaku(puzzle_number: int) -> str:
    """Generate initial state vector for given puzzle"""
    tane = kakuritsueki_kikan_no_shikiteki()
    random.seed(tane)
    
    # Get the seed for this puzzle from file
    seeds_content = read_seeds_file()
    
    if seeds_content is None:
        return None
    
    # Parse seeds file to find the seed for the requested puzzle
    lines = seeds_content.split('\n')
    current_puzzle = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('puzzle '):
            current_puzzle = int(line.split()[1])
        elif current_puzzle == puzzle_number and line.startswith('0'):
            return line
    
    return None

# Main program
if __name__ == "__main__":
    while True:
        try:
            puzzle_input = input()
            
            if puzzle_input.strip() == '':
                print("シーケンスの ID 要素を入力してください(複数する場合は改線入力): []")
                break
            
            puzzle_num = int(puzzle_input.strip())
            
            # Generate and display the seed
            seed_value = shoki_joutai_bekutoru_seisaku(puzzle_num)
            
            if seed_value:
                print(seed_value)
            else:
                print(f"Puzzle {puzzle_num} not found")
            
            print("シーケンスの ID 要素を入力してください(複数する場合は改線入力): ", end="")
            sys.stdout.flush()
            
        except ValueError:
            print("Invalid puzzle number")
            print("シーケンスの ID 要素を入力してください(複数する場合は改線入力): ", end="")
            sys.stdout.flush()
        except KeyboardInterrupt:
            print("\nプログラムを終了します。")
            break
