def bottles_of_beer_on_the_wall(n):
    # Base case
    if n == 0:
        print("No more bottles of beer on the wall")

    # Recursive case
    else:
        print(f"{n} bottles of beer on the wall")
        bottles_of_beer_on_the_wall(n - 1)


if __name__ == "__main__":
    bottles_of_beer_on_the_wall(5)
