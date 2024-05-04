import asyncio

# Coroutine function to simulate I/O-bound task
async def fetch_data(url):
    print("Fetching data from:", url)
    await asyncio.sleep(1)
    print("Data fetched successfully from:", url)

# Main function to run coroutines concurrently
async def main():
    await asyncio.gather(
        fetch_data("https://example.com/1"),
        fetch_data("https://example.com/2"),
        fetch_data("https://example.com/3")
    )

# Run the main function asynchronously
asyncio.run(main())
