"""Word Co-Occurrence Matrix"""
from collections import defaultdict

def build_cooccurrence(tokens, window=2):
    matrix = defaultdict(Counter if 'Counter' in globals() else dict)
    for i, w in enumerate(tokens):
        for j in range(max(0, i - window), min(len(tokens), i + window + 1)):
            if i != j:
                matrix[w][tokens[j]] = matrix[w].get(tokens[j], 0) + 1
    return dict(matrix)

if __name__ == "__main__":
    print("[RUN] Word Co-Occurrence Matrix...")
    toks = ["deep", "learning", "neural", "networks"]
    m = build_cooccurrence(toks, window=1)
    print(f"[OK] Co-Occurrence Pairs for 'learning': {m.get('learning')}")
