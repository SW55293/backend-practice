package main

import "fmt"

func main() {
	// if statements in Go don't use parentheses around the condition:
	height := 5

	if height > 4 {
		fmt.Println("You are tall enough!")
	}

	// else if and else are supported as you would expect:
	if height > 6 {
		fmt.Println("You are super tall!")
	} else if height > 4 {
		fmt.Println("You are tall enough!")
	} else {
		fmt.Println("You are not tall enough!")
	}

	/*
		THE INITIAL STATEMENT OF AN IF BLOCK
		An if conditional can have an "initial" statement. The variable(s) created in the initial
		statement are only defined within the scope of the if body.

		EX:
		if INITIAL_STATEMENT; CONDITION {
			}

	*/

	// instead of writing
	/*
			length := getLength(email)
			if length < 1 {
		    fmt.Println("Email is invalid")
			}
	*/
	// We can do
	/*
		if length := getLength(email); length < 1 {
	    fmt.Println("Email is invalid")
	}

	*/

}
