package main

import (
	terminalsdk "./terminal"
)

func main() {
	terminal := terminalsdk.NewTerminal()
	terminal.UpdateStatus()
	panic(terminal.Run())
}