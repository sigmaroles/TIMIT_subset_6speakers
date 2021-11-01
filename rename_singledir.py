import os

fflist = [x for x in filter(lambda fn: fn.endswith(".WAV"), [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(".")) for f in fn])]


for fpath in fflist:
    parts = fpath.split('/')
    newname = parts[1] + "_" + parts[2]
    print(f"mv {fpath} ./{newname}")