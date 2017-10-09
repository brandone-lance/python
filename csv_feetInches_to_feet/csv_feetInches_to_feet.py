def csv_feetInches_to_feet(file, output, heading):
    #   Using dataframes so lets import pandas
    import pandas as pd

    #   the csv file is read in as dataframe
    df = pd.read_csv(file)

    #   We're going to iterate over all rows of the chosen heading
    #   So first initialize an index...
    n_row = 0
    for row in df[heading]:
##        print(row)
        #   now we will initialize some indices for iterating over characters
        #   in the rows. Also assume no quote marks exist until they're found.
        n_char_s_try = 0
        n_char_d_try = 0
        n_char_s_true = 0
        n_char_d_true = 0
        exist_s = False
        exist_d = False

        #   Now test for the quotes, and mark their existence if need be
        if '\'' in row:
            exist_s = True
        if '\"' in row:
            exist_d = True

        #   Now we iterate over the row's characters iff the quotes exist
        #   The index of that quote character will be recorded in the _true
        #   variable after being _try'd and passing test.
        for char in row:
            if exist_s:
                if char == '\'':
                    n_char_s_true = n_char_s_try
                else:
                    n_char_s_try += 1
            if exist_d:
                if char == '\"':
                    n_char_d_true = n_char_d_try
                else:
                    n_char_d_try += 1
                    
        #   Here we convert the slice of string containing height data to float
        #   If either the feet or inches do not exist, they're associated
        #   values are merely set to 0.
        if exist_s:
##            print('Single quote loc: ', n_char_s_true)
##            print('Feet: ',row[0:n_char_s_true])
            height_feet = float(row[0:n_char_s_true])
        else:
            height_feet = 0
        if exist_d:
##            print('Double quote loc: ', n_char_d_true)
##            print('inches: ',row[n_char_s_true+1:n_char_d_true])
            if exist_s:
                height_inches = float(row[n_char_s_true+1:n_char_d_true])
            else:
                height_inches = float(row[0:n_char_d_true])
        else:
            height_inches = 0
            
        #   now throw feet and inches (converted) together as height
        height = height_feet + height_inches/12

##        print('Total height is ', height, ' ft.')
##        print()

        #   Record the individual rows under the heading
        df[heading][n_row] = height
        n_row += 1

    #   output to csv file
    df.to_csv(output)

