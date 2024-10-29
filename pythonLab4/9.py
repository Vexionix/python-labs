def count_matching_args(*args, **keyword_args):
    keyword_arg_values = set(keyword_args.values())
    count = sum(arg in keyword_arg_values for arg in args)
    return count

print(count_matching_args(1, 2, 3, 4, x=1, y=2, z=3, w=5))
