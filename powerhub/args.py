import argparse

parser = argparse.ArgumentParser(
    description="Leverage PowerShell to load sketchy code over HTTP"
)

parser.add_argument(
    '-p',
    '--lport',
    default=8000,
    dest="LPORT",
    type=int,
    help="the local port to listen on (default: 8000)"
)

# TODO currently not supported
#  parser.add_argument(
#      '-s',
#      '--ssl',
#      default=False,
#      dest="SSL",
#      action="store_true",
#      help="use SSL"
#  )

parser.add_argument(
    '-l', '--lhost', default='0.0.0.0',
    dest="LHOST",
    type=str,
    help="the local bind address to listen on (default: '0.0.0.0')"
)

parser.add_argument(
    '-n', '--noisy', default=True, dest="NOISY",
    action="store_false",
    help="allow noisy actions like loading mimikatz"
)

parser.add_argument(
    dest="URI_HOST", type=str,
    help="the hostname where the target can reach the server"
)

parser.add_argument(
    '-c', '--disable-compression', default=False,
    dest="NO_COMPRESS", action="store_true",
    help="disables zip compression in case old powershell versions need \
        to be supported"
)

parser.add_argument(
    '-u', '--uri-port', dest="URI_PORT", type=int,
    default=0,
    help="the port where the target can reach the server (default: LPORT)"
)

parser.add_argument(
    '--uri-path', dest="URI_PATH", type=str,
    default='ps',
    help="the URI path where the target can reach the server (default: 'ps')"
)


parser.add_argument(
    '--auth', dest="AUTH", type=str,
    default="",
    help=("Define credentials for basic authentication in the form of \
          'user:pass'"))


parser.add_argument(
    '-v', '--version', action='version', version='%(prog)s 0.1'
)

args = parser.parse_args()

if args.URI_PORT == 0:
    args.URI_PORT = args.LPORT

args.PROTOCOL = 'http'
#  if args.SSL:
#      args.PROTOCOL = 'https'
#  else:
#      args.PROTOCOL = 'http'
