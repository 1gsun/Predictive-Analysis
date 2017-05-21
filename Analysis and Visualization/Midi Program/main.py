"""
Main program

@author: Wenjie Sun 
"""

from path_list import *
from process_master import *
from midi_to_dataframe import *
from plot import *
import pandas as pd
import sys

print ("Pre-loading Data...")
# pre-load data of a file
master_folder = process_master("/Users/sunevan/Dropbox/Fall 2016/Programming for Data Science/Midi Program My Contribution/Classified Midis",1)
masterdata = master_folder.result()

print ("Data is now loaded")

while True:
    try:
        input_choice = input("Type 1 to use an existing preloaded database \nType 2 to input your new midi file \nType 0 to exit the program \nInput: ")
        if input_choice == "0":
            break
        elif input_choice == "2":
            input_midi = input("Please input a midi file: ")
            try:
                midi_ind = midi_to_dataframe(input_midi)
            except:
                print ("Not Valid Midi Path")
                continue

            midi_df = midi_ind.result()

            try:
                plot(midi_df).plot1()
            except:
                pass
            try:
                plot(midi_df).plot2()
            except:
                pass
            try:
                plot(midi_df).plot3()
            except:
                pass
            try:
                plot(midi_df).plot4()
            except:
                pass

        elif input_choice == "1":
            df_lib = pd.DataFrame(masterdata[["Song_Seq", "Genre", "Artist", "MidiName"]])
            df_lib = df_lib.drop_duplicates(['Song_Seq'])
            df_lib = df_lib.set_index(['Song_Seq'])
            print (df_lib.to_string())

            song_seq = input("Please choose # of the song: ")
            try:
                song_seq = int(song_seq)
            except:
                print("Not Valid")
                continue

            Genre_value = df_lib.iloc[song_seq]["Genre"]
            Artist_value = df_lib.iloc[song_seq]["Artist"]
            MidiName_value = df_lib.iloc[song_seq]["MidiName"]
            df1 = masterdata[(masterdata["Genre"] == Genre_value) & (masterdata["Artist"] == Artist_value) & (masterdata["MidiName"] == MidiName_value)]
            try:
                plot(df1).plot1()
            except:
                pass
            try:
                plot(df1).plot2()
            except:
                pass
            try:
                plot(df1).plot3()
            except:
                pass
            try:
                plot(df1).plot4()
            except:
                pass

        else:
            print ("Wrong Number")
            continue
    except ValueError:
        print ("Error")
        continue
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)


