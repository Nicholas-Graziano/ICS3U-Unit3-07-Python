#!/usr/bin/env python3
# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if u got the right random number


def main():

    # input
    age = print("Enter your age ")
    age_as_string = input("Enter here:")
    try:
        age = int(age_as_string)
        if age >= 25 and age <= 40:
            print("You are good enough")
        else:
            print("You are not good enough")
    except Exception:
        print("This is not a age")


if __name__ == "__main__":
    main()
