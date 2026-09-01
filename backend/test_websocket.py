import asyncio
import websockets


async def test_websocket():
    uri = "ws://127.0.0.1:8000/ws/threats"

    async with websockets.connect(uri) as websocket:
        print("WebSocket connected successfully!")

        await websocket.send("test")

        print("WebSocket test completed successfully.")


asyncio.run(test_websocket())