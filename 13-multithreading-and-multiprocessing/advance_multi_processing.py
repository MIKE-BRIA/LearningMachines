## Multiprocessing with ProcessPoolExecutor

# from concurrent.futures import ProcessPoolExecutor
# import time

# def square_number(number):
#     time.sleep(1)
#     return f'Square: {number * number}'


# numbers=[1,2,3,4,5,6,7,8,9]


# if __name__ == "__main__":

#     with ProcessPoolExecutor(max_workers=5) as executor:
#         results = executor.map(square_number,numbers)

#     for result in results:
#         print(result)



from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(processName)s - %(message)s")
logger = logging.getLogger(__name__)

def square_number(number: int) -> dict:
    try:
        time.sleep(1)
        result = number * number
        logger.info(f"Computed square of {number}")
        return {"number": number, "square": result, "error": None}
    except Exception as e:
        return {"number": number, "square": None, "error": str(e)}


def run_parallel(numbers: list[int], max_workers: int = None) -> list[dict]:
    results = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(square_number, n): n for n in numbers}

        for future in as_completed(futures):
            number = futures[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                logger.error(f"Task for number {number} failed: {e}")
                results.append({"number": number, "square": None, "error": str(e)})

    return sorted(results, key=lambda x: x["number"])


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    start = time.perf_counter()
    results = run_parallel(numbers, max_workers=5)
    elapsed = time.perf_counter() - start

    for r in results:
        if r["error"]:
            print(f"  Number {r['number']} failed: {r['error']}")
        else:
            print(f"  {r['number']}² = {r['square']}")

    print(f"\nCompleted {len(numbers)} tasks in {elapsed:.2f}s")
