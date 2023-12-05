package main

import "fmt"

func main() {
	v := fmt.Sprintf("I am %v years old", 10)
	// I am 10 years old

	v2 := fmt.Sprintf("I am %v years old", "way too many")
	// I am way too many years old

	fmt.Println(v)
	fmt.Println(v2)

	// INTERPOLATE A STRING
	str := fmt.Sprintf("I am %s years old", "way too many")
	fmt.Println(str)

	// INTERPOLATE AN INTEGER IN DECIMAL FORM
	d := fmt.Sprintf("I am %d years old", 10)
	fmt.Println(d)

	// INTERPOLATE A DECIMAL
	de := fmt.Sprintf("I am %f years old", 10.523)

	// The ".2" rounds the number to 2 decimal places
	de2 := fmt.Sprintf("I am %.2f years old", 10.523)

	fmt.Println(de)
	fmt.Println(de2)

	/* ASSIGNMENT
	   Create a new variable called msg on line 9. It's a string that contains the following:

	   Hi NAME, your open rate is OPENRATE percent
	   Copy icon
	   Where NAME is the given name, and OPENRATE is the openRate rounded to the nearest "tenths" place.
	*/

	const name = "Saul Goodman"
	const openRate = 30.5
	msg := fmt.Sprintf("Hi %s, your open rate is %.1f  percent", name, openRate)

	// don't edit below this line

	fmt.Println(msg)

}
