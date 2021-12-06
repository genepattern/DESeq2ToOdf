import os
import sys
from subprocess import call

WORKING_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
ROOT = os.path.join(WORKING_DIR, '..')
TASKLIB = os.path.join(ROOT, 'src/')
#INPUT_FILE_DIRECTORIES = os.path.join(ROOT, 'data/')
INPUT_FILE_DIRECTORIES = os.path.join(ROOT, "gpunit/input/")

# command_line = "python "+TASKLIB+"txt2odf.py "+INPUT_FILE_DIRECTORIES+"DESeq2_results_report_sample.txt"
# command_line = "python "+TASKLIB+"txt2odf.py "+INPUT_FILE_DIRECTORIES+"AA.preprocessed.DESeq2_results_report.txt"
#command_line = "python "+TASKLIB+"txt2odf.py "+INPUT_FILE_DIRECTORIES+"long_results.txt "\
#               + "True "+INPUT_FILE_DIRECTORIES+"long_gct.gct "+INPUT_FILE_DIRECTORIES+"BRCA_40_samples.cls"

## Test 1 - standard DESeq2 output
command_line = (
    "python " + TASKLIB + "txt2odf.py " +
    INPUT_FILE_DIRECTORIES + "long_results.txt id stat True " +
    INPUT_FILE_DIRECTORIES + "long_gct.gct " +
    INPUT_FILE_DIRECTORIES + "BRCA_40_samples.cls"
)

call(command_line, shell=True)

## Test 2 - tximport.DESeq2.Normalize
INPUT_FILE_DIRECTORIES = os.path.join(ROOT, "gpunit/input/82042/")

command_line = (
    "python " + TASKLIB + "txt2odf.py " +
    INPUT_FILE_DIRECTORIES + "Merged.Data.Differential.Expression.txt " +
    "Gene_ID 'Wald statistic: Factor EPZ6438 vs DMSO' True " +
    INPUT_FILE_DIRECTORIES + "Merged.Data.Normalized.Counts.gct " +
    INPUT_FILE_DIRECTORIES + "Merged.Data.cls"
)

call(command_line, shell = True)
