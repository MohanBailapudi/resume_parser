import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import OrderedDict

def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from keras_en_parser_and_analyzer.library.dl_based_parser import ResumeParser
    from keras_en_parser_and_analyzer.library.utility.io_utils import read_pdf_and_docx

    current_dir = os.path.dirname(__file__)
    current_dir = current_dir if current_dir is not '' else '.'
    data_dir_path = current_dir + '/data/resume_samples'  # directory to scan for any pdf and docx files

    def parse_resume(file_path, file_content):
        print('parsing file: ', file_path)

        parser = ResumeParser()
        parser.load_model(current_dir + '/models')
        parser.parse(file_content)

        if parser.unknown is False:
            summary, expertise, experience, knowledge, project = parser.summary()
            # print("Condition Success")
            #
            # print(summary.encode('utf-8'))
            # vocabulary = []
            # for i in experience:
            #     vocabulary.append(i.encode("utf-8"))
            # print(vocabulary)

            experience_vocabulary = []
            for i in experience:
                j = i.encode('ascii', 'ignore').decode("utf-8").split(':')
                print(j)
                if len(j) != 1:
                    for k in j[1:]:
                        l = k.split(',')
                        experience_vocabulary.extend(l)
                else:
                    for k in j:
                        l = k.split(',')
                        experience_vocabulary.extend(l)
                        print(l)
            experience_vocabulary = list(filter(None, experience_vocabulary))
            experience_vocabulary = list(OrderedDict.fromkeys(experience_vocabulary))
            print(experience_vocabulary)
            expertise_vocabulary = []
            for i in expertise:
                expertise_vocabulary.append(i.encode('ascii', 'ignore').decode("utf-8"))
            knowledge_vocabulary = []
            for i in knowledge:
                knowledge_vocabulary.append(i.encode('ascii', 'ignore').decode("utf-8"))
            project_vocabulary = []
            for i in project:
                project_vocabulary.append(i.encode('ascii', 'ignore').decode("utf-8"))
            # print(summary.encode('utf-8'))
            document1 = "".join(experience_vocabulary)
            document2 = "".join(knowledge_vocabulary)
            document3 = "".join(project_vocabulary)
            corpus = dict([('expertise',document1),('knowledge',document2),('project',document3)])
            tfidf = TfidfVectorizer(vocabulary=experience_vocabulary, stop_words='english', ngram_range=(1, 2))
            tfs = tfidf.fit_transform(corpus.values())
            feature_names = tfidf.get_feature_names()
            corpus_index = [n for n in corpus]
            # rows, cols = tfs.nonzero()
            # for row, col in zip(rows, cols):
            #     print((feature_names[col], corpus_index[row]), tfs[row, col])
            import pandas as pd
            df = pd.DataFrame(tfs.T.todense(), index=feature_names, columns=corpus_index)
            print(df)
            # print(experience_vocabulary)
            # print(expertise_vocabulary)
            # print(knowledge_vocabulary)
            # print(project_vocabulary)
        print('++++++++++++++++++++++++++++++++++++++++++')

    collected = read_pdf_and_docx(data_dir_path, command_logging=True, callback=lambda index, file_path, file_content: {
        parse_resume(file_path, file_content)
    })
    print('count: ', len(collected))


if __name__ == '__main__':
    main()
