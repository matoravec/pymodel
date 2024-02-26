//go:build mage

package main

// notest // task orchestrator, not part of the service code

import (
	"context"
	"fmt"
	"os"
	"os/exec"
	"strings"

	"github.com/fatih/color"
)

func GenerateProtoGo(ctx context.Context) error {
	return run(ctx, "buf", "generate")
}

func GenerateProtoPy(ctx context.Context) error {
	os.Chdir("py")
	defer os.Chdir("..")

	return run(ctx, "buf", "generate", "../proto/pymodel.proto")
}

func RunPyServer(ctx context.Context) error {
	return run(ctx, "python", "py/server.py")
}

func GetPredictions(ctx context.Context) error {
	return run(ctx, "go", "run", "main.go")
}

func cmd(ctx context.Context, program string, args ...string) *exec.Cmd {
	command := exec.CommandContext(ctx, program, args...)
	command.Stdout = os.Stdout
	command.Stderr = os.Stderr

	return command
}

func run(ctx context.Context, program string, args ...string) error {
	command := cmd(ctx, program, args...)
	fmt.Printf(
		"%s %s\n",
		color.MagentaString(">"),
		color.New(color.Bold).Sprint(program, " ", strings.Join(args, " ")),
	)

	return command.Run()
}
