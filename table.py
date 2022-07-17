import tabula as tb
import pandas as pd

file='table1.pdf'

table=tb.read_pdf(file)

csv_table=tb.convert_into(file, 'pdf_convert.csv')
#for excel file we need to export the data to csv using pandas
df=pd.concat(table)

excel_file=df.to_excel('pdf_convert.xlsx')

file='table_2.pdf'
table= tb.read_pdf(file)

csv_table=tb.convert_into(file, 'pdf_convert_table2.csv')

df=pd.concat(table)

excel_file=df.to_excel('pdf_convert_table2.xlsx')