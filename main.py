from liste import (
    suma_elementelor,
    suma_elementelor_py,
)


def main() -> None:
    v = [int(x) for x in input().split()]
    print(suma_elementelor(v), suma_elementelor_py(v))


if __name__ == "__main__":
    main()
