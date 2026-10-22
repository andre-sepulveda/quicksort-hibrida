import random
import time
import statistics
import matplotlib.pyplot as plt

N = 20_000
SEED = 20261022
CORTES = [1, 5, 10, 16, 20, 32, 50, 100, 200]
REPETICOES = 7

def insertion_sort(a, lo, hi):
    for i in range(lo + 1, hi):
        chave = a[i]
        j = i - 1
        while j >= lo and a[j] > chave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = chave

def quicksort_3way(a, lo=0, hi=None, corte=1):
    if hi is None:
        hi = len(a)
    while hi - lo > 1:
        if hi - lo < corte:
            insertion_sort(a, lo, hi)
            return
        pivo = a[random.randrange(lo, hi)]
        menores, atual, maiores = lo, lo, hi
        while atual < maiores:
            if a[atual] < pivo:
                a[menores], a[atual] = a[atual], a[menores]
                menores += 1
                atual += 1
            elif a[atual] > pivo:
                maiores -= 1
                a[atual], a[maiores] = a[maiores], a[atual]
            else:
                atual += 1
        if menores - lo < hi - maiores:
            quicksort_3way(a, lo, menores, corte)
            lo = maiores
        else:
            quicksort_3way(a, maiores, hi, corte)
            hi = menores

def main():
    rng = random.Random(SEED)
    dados = [rng.randrange(0, 1_000_000) for _ in range(N)]
    resultados = {}
    for corte in CORTES:
        tempos = []
        for repeticao in range(REPETICOES):
            a = dados.copy()
            random.seed(SEED + repeticao * 1009)
            inicio = time.perf_counter()
            quicksort_3way(a, corte=corte)
            tempos.append(time.perf_counter() - inicio)
            assert a == sorted(dados)
        resultados[corte] = statistics.median(tempos)

    baseline = resultados[1]
    print("| Corte | Tempo mediano (ms) | Diferença vs. corte 1 |")
    print("|---:|---:|---:|")
    for corte in CORTES:
        diff = (resultados[corte] / baseline - 1) * 100
        print(f"| {corte} | {resultados[corte]*1000:.3f} | {diff:+.2f}% |")

    melhor = min(resultados, key=resultados.get)
    ganho = (baseline - resultados[melhor]) / baseline * 100
    print(f"Melhor corte: {melhor}; ganho vs. corte 1: {ganho:.2f}%")

    plt.plot(CORTES, [resultados[c]*1000 for c in CORTES], marker="o")
    plt.axhline(baseline*1000, linestyle="--", label="Quicksort pura (corte 1)")
    plt.xlabel("Corte (elementos)")
    plt.ylabel("Tempo mediano (ms)")
    plt.title("Quicksort híbrida: tempo em função do corte")
    plt.xticks(CORTES)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafico_corte_quicksort.png", dpi=160)

if __name__ == "__main__":
    main()
