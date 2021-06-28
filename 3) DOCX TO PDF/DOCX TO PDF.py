# pip install docx2pdf
from docx2pdf import convert
print('Converting..')
source = r"E:\\#madhu\\VS CODE\\3) docx to pdf\\Resume EDITED 14TH MAY.docx"  # docx file location 
#print(source)

destination = source.replace('.docx','.pdf')

convert(source , destination)
print('\nConverted Successfully!!\n')
print(f'File Sucessfully Saved at {destination}')