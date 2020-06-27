package main

import (
	"fmt"
)

func f(n int) int {
	i := 1
	cnt := 0
	if n == 1 {
		return 1
	}
	for i*i <= n {
		if n%i == 0 {
			cnt++
			if i != int(n/i) {
				cnt++
			}
		}
		i++
	}
	return cnt
}

func main() {
	var n int
	fmt.Scan(&n)
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i * f(i)
	}
	fmt.Println(sum)
}
