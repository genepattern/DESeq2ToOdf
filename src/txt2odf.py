from gp.data import ODF
import pandas as pd

def txt2odf(txt_file:'URL to the TXT file',
            name_of_file:'Name of output file.' = 'Default',
            verbose:'Whether or not to print the gene list'=True):

#     # Get the job number and name of the file
#     temp = txt_file.split('/')
#     # programatically access that job to open the txt file
#     GP_txt = eval('job'+temp[5]+'.get_file("'+temp[6]+'")')

#     if name_of_file == 'Default':
#         name_of_file = temp[6].strip('txt') + 'odf'

    if name_of_file == 'Default':
        name_of_file = txt_file.strip('txt') + 'odf'
    data_df = pd.read_table(txt_file)
    data_df.insert(1,'Description', data_df['id'])
#     data_df['Description'] = data_df['id']

    vals = {}
    vals['gct'] = txt_file
    vals['cls'] = 'TBD'
    vals['n_perm'] = 'TBD'
    vals['class_0'] = 'Class 0'
    vals['class_1'] = 'Class 1'
    vals['func'] = 'Function'
    vals['rand_seed'] = 'TBD'
    vals['dat_lines'] = 'TBD'

    df2odf(data_df=data_df, vals=vals, file_name=name_of_file)

    if verbose:
        print('File', name_of_file, "has been written!")
        print(data_df)
#     return f


genepattern.GPUIBuilder(txt2odf,
                        name="txt2odf",
                        parameters={
                                    "txt_file": {
                                                 "type": "file",
                                                 "kinds": ["txt", "Comparative Marker Selection"],
                                    }
                        })

def df2odf(data_df, vals, file_name='noname.odf'):
    f = open(file_name, 'w')
    f.write("ODF 1.0\n")  # Hard-coding spance, not tab here.
    f.write("HeaderLines=18\n")  # hard-coding lines here. Needs to change.
    f.write("COLUMN_NAMES:"+"\t".join(list(data_df))+"\n")
    f.write("COLUMN_TYPES:"+"\t".join(['String','String', 'double', 'double', 'double', 'double', 'double', 'double'])+"\n")  # TODO: automate this.
    f.write("Model=Comparative Marker Selection\n")
    f.write("Dataset File="+vals['gct']+"\n")
    f.write("Class File="+vals['cls']+"\n")
    f.write("Permutations="+str(vals['n_perm'])+"\n")
    f.write("Class 0="+vals['class_0']+"\n")
    f.write("Class 1="+vals['class_1']+"\n")
    f.write("Test Statistic="+vals['func']+"\n")
    f.write("pi0=\n")
    f.write("lambda=\n")
    f.write("pi0(lambda)=\n")
    f.write("cubic spline(lambda)=\n")
    f.write("Random Seed="+str(vals['rand_seed'])+"\n")
    f.write("Smooth p-values=\n")
    f.write("DataLines="+str(vals['dat_lines'])+"\n")
    f.write("RowNamesColumn=0\n")
    f.write("RowDescriptionsColumn=1\n")
    f.write(data_df.to_csv(sep='\t', index=False, header=False))
