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
is_gerrt = False

if len(sys.argv) > 2:
    if sys.argv[2] == '-g':
        is_gerrt = True
        print('Switch to gerrit !')
    else:
        is_gerrt = False

if len(sys.argv) < 2:
    print('optional arguments:')
    print('-s, shenzhen')
    print('-x, xian')
    print('-g, gerrit')
    exit()

if len(sys.argv) > 2 and sys.argv[2] == '-g':
    in_file = in_sz
    out_file = out_gerrit
    where = 'sz'
elif sys.argv[1] == '-s':
    in_file = in_xa
    out_file = out_sz
    where = 'sz'
elif sys.argv[1] == '-x':
    in_file = in_sz
    out_file = out_xa
    where = 'xa'
else:
    print('Pls input city !')
    exit()

with open(in_file, encoding='utf-8') as file_object:
    lines_in = file_object.readlines()
    with open(out_file, 'w', encoding='utf-8') as file_object:
        for line_in in lines_in:
            line_in = line_in.lstrip()
            if is_gerrt == True:
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
            file_object.write(line_out)
print(f'output: {out_file}')

