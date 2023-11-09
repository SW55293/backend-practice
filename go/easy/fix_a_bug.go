package main

import "fmt"

func main() {
	messagesFromDoris := []string{
		"You doing anything later??",
		"Did you get my last message?",
		"Don't leave me hanging...",
		"Please respond I'm lonely!",
		"Another line",
	}
	numMessages := float64(len(messagesFromDoris))
	costPerMessage := .02

	// don't touch above this line

	// there was an arithmetic bug on line 17, just changed to *
	totalCost := costPerMessage * numMessages

	// don't touch below this line

	fmt.Printf("Doris spent %.2f on text messages today\n", totalCost)
}
