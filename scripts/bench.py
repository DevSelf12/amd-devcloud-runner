#!/usr/bin/env python3
import argparse
import time


def matrix_bench(n: int, steps: int):
    a = [[1.0 for _ in range(n)] for _ in range(n)]
    b = [[1.0 for _ in range(n)] for _ in range(n)]
    c = [[0.0 for _ in range(n)] for _ in range(n)]

    times = []
    for s in range(steps):
        t0 = time.perf_counter()
        for i in range(n):
            for j in range(n):
                v = 0.0
                for k in range(n):
                    v += a[i][k] * b[k][j]
                c[i][j] = v
        dt = time.perf_counter() - t0
        times.append(dt)

    avg = sum(times) / len(times)
    return {
        "mode": "matrix",
        "n": n,
        "steps": steps,
        "avg_sec": round(avg, 6),
        "times": [round(t, 6) for t in times],
    }


def main():
    parser = argparse.ArgumentParser(description="amd-devcloud-runner bench")
    parser.add_argument("--mode", default="matrix", choices=["matrix"])
    parser.add_argument("--n", type=int, default=256)
    parser.add_argument("--steps", type=int, default=3)
    args = parser.parse_args()

    if args.mode == "matrix":
        result = matrix_bench(args.n, args.steps)

    print("[bench] result:")
    for k, v in result.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
