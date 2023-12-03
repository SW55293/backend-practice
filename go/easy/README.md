#### Go is generally faster and more lightweight than interpreted or VM-powered languages like:

- Python
- JavaScript
- PHP
- Ruby
- Java

#### However, in terms of execution speed, Go does lag behind some other compiled languages like:

- C
- C++
- Rust


```go
package main 
// lets the Go compiler know that we want this code to compile and run as a standalone program, as opposed to being a library that's imported by other programs.

import fmt 
// imports the fmt (formatting) package. The formatting package exists in Go's standard library and lets us do things like print text to the console.

func main() 
// defines the main function. main is the name of the function that acts as the entry point for a Go program.
```

```go
// Go's variable types
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128

```

> var empty string == empty := ""


#### Types

```go
int  int8  int16  int32  int64 // whole numbers

uint uint8 uint16 uint32 uint64 uintptr // positive whole numbers

float32 float64 // decimal numbers

complex64 complex128 // imaginary numbers (rare)

```