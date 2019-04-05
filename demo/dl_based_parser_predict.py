import sys
import os
from sklearn.feature_extraction.text import CountVectorizer

def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from keras_en_parser_and_analyzer.library.dl_based_parser import ResumeParser
    from keras_en_parser_and_analyzer.library.utility.io_utils import read_pdf_and_docx

    current_dir = os.path.dirname(__file__)
    current_dir = current_dir if current_dir is not '' else '.'
    data_dir_path = current_dir + '/data/resume_samples' # directory to scan for any pdf and docx files

    def parse_resume(file_path, file_content):
        print('parsing file: ', file_path)

        parser = ResumeParser()
        parser.load_model(current_dir + '/models')
        parser.parse(file_content)
        # print(parser.raw.encode("utf-8"))  # print out the raw contents extracted from pdf or docx files
        
        if parser.unknown is False:
            summary, expertise, experience, knowledge, project = parser.summary()
            # print(parser.summary().encode("utf-8"))
            print(summary.encode('utf-8'))
            vocabulary = []
            for i in experience:
                vocabulary.append(i.encode("utf-8"))
            print(vocabulary)
            # prefinal_vocabulary = []
            # for i in vocabulary:
            #     try:
            #         prefinal_vocabulary.append(i.decode("utf-8"))
            #     except:
            #         prefinal_vocabulary.append(str(i,"utf-8"))
            # print(prefinal_vocabulary[9])
            final_vocabulary = []
            # for i in prefinal_vocabulary:
            #     print(i)
                # try:
                #     j = i.split(',')
                # except:
                #     pass
                # print(j)
        print('++++++++++++++++++++++++++++++++++++++++++')

    collected = read_pdf_and_docx(data_dir_path, command_logging=True, callback=lambda index, file_path, file_content: {
        parse_resume(file_path, file_content)
    })
    print('count: ', len(collected))


if __name__ == '__main__':
    main()
