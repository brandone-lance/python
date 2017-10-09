When heights or distances in imperial units are given in the convention of, say, 6'3" to represent 6.25 ft, it can be a pain to do any kind of analytics or math with the figures.

This simple and hastily written function converts columns of those troublesome figures directly to units of feet. Any further conversions to, say, SI units are made much easier.

USAGE:
csv_feetInches_to_feet(file, output, heading)
  file:     CSV file with column to convert
  out:      Name of file to output
  heading:  Heading of column to convert

Example:
csv_feetInches_to_feet('foo.csv', 'bar.csv', 'Height')
  Will take the column labeled "Height" in foo.csv, convert the quote-convention style to floating point feet, and output into bar.csv with no output given (save for errors).

KNOWN ISSUES:
  1.  Figures with only inches (e.g. 12") have an issue where the first digit (here, the 1) is dropped. It's an indexing issue.
  2.  The output CSV file has a prepended column of index values. This is probably something I can fix with the parameters of to_csv()
  3.  There's no manner of error handling.
  
Use at your own risk!
