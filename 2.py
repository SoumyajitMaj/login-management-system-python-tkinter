import PyPDF2

pdf_files=[{'filename':'daa.pdf','page':[0,2]},{'filename':'daa qb.pdf','page':[0,2]}]
output_filename='abc.pdf'

def combine_pdf(input_files,output_files):
    pdf_writer=PyPDF2.Writer()
    for pdf_info in input_files:
        filename=pdf_info['filename']
        pages_selected=pdf_info['page']
        
        with open('filename','rb') as pdf_file:
            pdf_reader=PyPDF2.Reader(pdf_file)
            
            for page_num in pages_selected:
                page=pdf_reader.pages(page_num)
                pdf_writer.add_pages(page)
        with open('output_files','wb') as output_pdf:
            pdf_writer.write(output_pdf)
    print("Done")
combine_pdf(pdf_files, output_filename)