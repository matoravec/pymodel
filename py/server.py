from concurrent.futures import ThreadPoolExecutor

import grpc
import joblib
from loguru import logger
from proto.pymodel_pb2 import Prediction, PredictResponse
from proto.pymodel_pb2_grpc import (
    PredictServiceServicer,
    add_PredictServiceServicer_to_server,
)
from sklearn.linear_model import LinearRegression


class PredictServer(PredictServiceServicer):
    def __init__(self) -> None:
        super().__init__()

        self._model: LinearRegression = joblib.load("py/model.joblib")

    def Predict(self, request, context):
        logger.info(f"Got request {request}")
        return PredictResponse(
            predictions=[
                Prediction(
                    id=features.id,
                    prediction=self._model.predict([[features.f1, features.f2]])[0],
                )
                for features in request.features
            ]
        )


def start() -> None:
    server = grpc.server(ThreadPoolExecutor())
    add_PredictServiceServicer_to_server(PredictServer(), server=server)

    port = 8090

    server.add_insecure_port(f"[::]:{port}")

    server.start()
    logger.info(f"Python model server started on http://0.0.0.0:{port}")
    server.wait_for_termination()


if __name__ == "__main__":
    start()
