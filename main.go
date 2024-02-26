package main

import (
	"context"
	"log"

	"github.com/matoravec/pymodel/proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	modelServerAddress := "localhost:8090"

	connection, err := grpc.DialContext(
		context.Background(),
		modelServerAddress,
		grpc.WithBlock(),
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)

	if err != nil {
		log.Fatalln("Failed to dial server:", err)
	}

	client := proto.NewPredictServiceClient(connection)

	features := []*proto.Features{
		{Id: 123, F1: 1.2, F2: 3.4},
	}

	request := proto.PredictRequest{
		Features: features,
	}

	response, err := client.Predict(context.Background(), &request)
	if err != nil {
		log.Fatalln(err)
	}

	log.Printf("Here are your predictions: %v", response)
}
