from fileinput import filename

import pandas as pd
import glob
import os
import csv
from os.path import exists

#declarations/var's
files = glob.glob('fixtures/*.csv')


def test_data():
    assert filename == filename
    assert files == files
    assert files == glob.glob('fixtures/*.csv')

def test_column():
    assert "clothing.csv" == "clothing.csv"
    assert "accessories.csv" == "accessories.csv"
    assert "household_cleaners.csv" == "household_cleaners.csv"

def test_my_files(file_exists=None):
    assert file_exists = exists("/Users/austinpete/Documents/GitHub/ProgrammingChallenges/csv-combiner/fixtures/accessories.csv")
    assert file_exists = exists("/Users/austinpete/Documents/GitHub/ProgrammingChallenges/csv-combiner/fixtures/clothing.csv")
    assert file_exists = exists("/Users/austinpete/Documents/GitHub/ProgrammingChallenges/csv-combiner/fixtures/household_cleaners.csv")
    path.is_file()
    #files = glob.glob('fixtures/*.csv')
    #assert files.__contains__("clothing")
    #assert files.__contains__("clothing.csv")



# https://www.youtube.com/watch?v=ZyKTrFLlMR0