def main():
    scores = [50, 55, 60, 65, 70]
    total = sum(scores)
    average = total / len(scores)

    print("-- main/master branch output --")
    print(f"total: {total}")
    print(f"average: {average}")
    print(f"scores: {scores}")


if __name__ == "__main__":
    main()
