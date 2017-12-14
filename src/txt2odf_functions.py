import sys


def parse_arguments(args=sys.argv):
    txt_file = None
    prune_gct = False
    gct = None
    cls = None

    arg_n = len(args)
    if arg_n == 1:
        sys.exit("Error message: No files were provided. This module needs a GCT and a CLS file to work.")
    elif arg_n == 2:
        txt_file = args[1]
        prune_gct = False
        gct = None
        cls = None

        print("Using txt_file=", txt_file)
        print("Using prune_gct=", prune_gct, '(default)')
        print("Using gct=", gct, '(default)')
        print("Using cls=", cls, '(default)')
    elif arg_n == 3:
        txt_file = args[1]
        prune_gct = eval(args[2])
        gct = None
        cls = None
        print("Using txt_file=", txt_file)
        print("Using prune_gct=", prune_gct)
        print("Using gct=", gct, '(default)')
        print("Using cls=", cls, '(default)')
    elif arg_n == 4:
        txt_file = args[1]
        prune_gct = eval(args[2])
        gct = args[3]
        cls = None
        print("Using txt_file=", txt_file)
        print("Using prune_gct=", prune_gct)
        print("Using gct=", gct)
        print("Using cls=", cls, '(default)')
    elif arg_n == 5:
        txt_file = args[1]
        prune_gct = eval(args[2])
        gct = args[3]
        cls = args[4]
        print("Using txt_file=", txt_file)
        print("Using prune_gct=", prune_gct)
        print("Using gct=", gct)
        print("Using cls=", cls)

    return txt_file, prune_gct, gct, cls


def df2odf(data_df, vals, file_name='noname.odf'):
    f = open(file_name, 'w')
    f.write("ODF 1.0\n")  # Hard-coding spance, not tab here.
    f.write("HeaderLines=19\n")  # hard-coding lines here. Needs to change.
    f.write("COLUMN_NAMES:"+"\t".join(list(data_df))+"\n")
    f.write("COLUMN_TYPES:"+"\t".join(['int', 'String', 'String', 'double', 'double', 'double', 'double', 'double', 'double', 'double'])+"\n")  # TODO: automate this.
    f.write("Model=Comparative Marker Selection\n")
    f.write("Dataset File="+vals['gct']+"\n")
    f.write("Class File="+vals['cls']+"\n")
    f.write("Permutations="+str(vals['n_perm'])+"\n")
    f.write("Balanced=false\n")
    f.write("Complete=false\n")
    f.write("Test Direction=2 Sided\n")
    f.write("Class 0="+vals['class_0']+"\n")
    f.write("Class 1="+vals['class_1']+"\n")
    f.write("Test Statistic="+vals['func']+"\n")
    f.write("pi0=TBD\n")
    f.write("lambda=TBD\n")
    f.write("pi0(lambda)=TBD\n")
    f.write("cubic spline(lambda)=TBD\n")
    f.write("Random Seed="+str(vals['rand_seed'])+"\n")
    f.write("Smooth p-values=true\n")
    f.write("DataLines="+str(vals['dat_lines'])+"\n")
    # f.write("RowNamesColumn=1\n")
    # f.write("RowDescriptionsColumn=2\n")
    f.write(data_df.to_csv(sep='\t', index=False, header=False))
