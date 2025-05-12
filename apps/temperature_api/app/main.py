import random

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


def random_temperature():
    return round(random.uniform(-10, 100), 1)


class Temperature(BaseModel):
    location: str = Field(default="Unknown", title="Название комнаты")
    sensor_id: str = Field(default="0", serialization_alias="sensorID", title="Идентификатор названия комнаты")
    temperature: float = Field(default_factory=random_temperature, title="Значение температуры")


@app.get("/temperature")
async def temperature(location: str | None = "", sensor_id: str = "") -> Temperature:
    # If no location is provided, use a default based on sensor ID
    if location == "":
        match sensor_id:
            case "1":
                location = "Living Room"
            case "2":
                location = "Bedroom"
            case "3":
                location = "Kitchen"
            case _:
                location = "Unknown"

    # If no sensor ID is provided, generate one based on location
    if sensor_id == "":
        match location:
            case "Living Room":
                sensor_id = "1"
            case "Bedroom":
                sensor_id = "2"
            case "Kitchen":
                sensor_id = "3"
            case _:
                sensor_id = "0"

    res = Temperature(location=location, sensor_id=sensor_id)
    return res


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', port=8001)
