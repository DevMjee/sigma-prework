import sys

try:
    # ignore 'maxmin.py' arg[0] and sort all other args into list
    nums = sorted(list(int(num) for num in sys.argv[1::]))

    if not nums:  # if empty args
        print("Run with 'python3 maxmin.py [int_1] [int_2] [int_3]...'")
    else:  # else args given
        print([nums[0], nums[-1]])

except ValueError as err:
    print(f'[ERROR: {err}] Please run with integer arguments only.')
