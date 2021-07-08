import sys

in_sz = '669s.txt'
in_xa = '669s_xa.txt'
out_sz = 'shenzhen.txt'
out_xa = 'xian.txt'
out_gerrit = 'gerrit.txt'
sz_git = 'git@172.16.16.25'
xa_git = 'git@192.168.5.200'
sz_ap_postfix = 'git@172.16.16.25:/repo'
xz_ap_postfix = 'git@192.168.5.200:/repo'
sz_modem_postfix = 'git@172.16.16.25:'
xa_modem_postfix = 'git@192.168.5.200:'
gerrit_ap = 'ssh://phliu@172.16.16.25:29418'
gerrit_modem = 'ssh://phliu@172.16.16.25:29418/'
git_tools = 'git@172.16.16.25:repo'

#命令行参数解析
import argparse
parser = argparse.ArgumentParser(description='')
#store_true表示有输入时为true，否则为false
#store_false表示有输入时为false，否则为true
parser.add_argument('-s', '--shenzhen', dest='shenzhen', action='store_true', help='switch to shenzhen')
parser.add_argument('-x', '--xian', dest='xian', action='store_true', help='switch to xian')
parser.add_argument('-g', '--gerrit', dest='gerrit', action='store_true', help='switch to gerrit')
args = parser.parse_args()
if len(sys.argv) == 1:
    print(parser.print_help())
    exit(0)
#print(args)
if args.gerrit:
    is_gerrit = True
    in_file = in_sz
    out_file = out_gerrit
    where = 'sz'   
    print('Switch to gerrit')
elif args.shenzhen:
    is_gerrit = False
    in_file = in_xa
    out_file = out_sz
    where = 'sz'
    print('Switch to shenzhen')
elif args.xian:
    is_gerrit = False
    in_file = in_sz
    out_file = out_xa
    where = 'xa'
    print('Switch to xian')

with open(in_file, encoding='utf-8') as file_object:
    lines_in = file_object.readlines()
    with open(out_file, 'w', encoding='utf-8') as file_object:
        for line_in in lines_in:
            line_in = line_in.lstrip()
            if is_gerrit == True:
                line_out = line_in.replace(sz_ap_postfix, gerrit_ap)
                line_out = line_out.replace(git_tools, gerrit_ap)
                line_out = line_out.replace(sz_modem_postfix, gerrit_modem)
                line_out = line_out.replace(xa_modem_postfix, gerrit_modem)
            elif where == 'sz':
                line_out = line_in.replace(xa_git, sz_git)
                line_out = line_out.replace(xa_modem_postfix, gerrit_ap)
            elif where == 'xa':
                line_out = line_in.replace(sz_git, xa_git)
                line_out = line_out.replace(sz_modem_postfix, gerrit_ap)
            else:
                print('where are u ? git or gerrit ?')
                exit(0)
            file_object.write(line_out)
print(f'Output: {out_file}')

