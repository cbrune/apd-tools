import os
import os.path
import re

import nose.tools

def test_hwmon(dir_str='/sys/class/hwmon'):

    regex_stdname = re.compile('.*:.{2,}')
    regex = re.compile('.*_label')
    norm_dir = os.path.abspath(dir_str)

    for hw_dir in os.listdir(norm_dir):
        cur_path = os.path.join(norm_dir, hw_dir)
        if os.path.islink(cur_path) and os.path.isdir(cur_path):
            for hwmon in os.listdir(cur_path):
                if regex.match(hwmon) or hwmon == 'name':
                    cur_file = os.path.join(cur_path, hwmon)
                    open_file = open(cur_file, 'r')
                    line = open_file.read()
                    open_file.close()
                    auto_gen_name = regex_stdname.match(line) is not None
                    msg = '{0} is an autogenerated name'.format(cur_file)
                    nose.tools.eq_(auto_gen_name, False, msg)
                    #print cur_path, hwmon, line, auto_gen_name

