import shlex

cmd = 'QueryCluster uuid'

pairs = shlex.split(cmd)

print pairs

for param_str in pairs[1:]:
    print param_str

    params = param_str.split('=', 1)
    if len(params) != 2:
        raise Exception


