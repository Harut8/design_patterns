"""
Imagine that you’re creating a data mining application that
analyzes corporate documents. Users feed the app documents
in various formats (PDF, DOC, CSV), and it tries to extract
meaningful data from these docs in a uniform format.
The first version of the app could work only with DOC files.
In the following version, it was able to support CSV files.
A month later, you “taught” it to extract data from PDF files.

At some point, you noticed that all three classes have a lot of similar code.
While the code for dealing with various data formats was
entirely different in all classes, the code for data processing
and analysis is almost identical. Wouldn’t it be
great to get rid of the code duplication, leaving the algorithm structure intact?
There was another problem related to client code that
used these classes. It had lots of conditionals that picked
a proper course of action depending on the class of the processing object.
If all three processing classes had a common interface or a base class,
you’d be able to eliminate the conditionals in client code and
use polymorphism when calling methods on a processing object.
"""
from abc import abstractmethod, ABC


# EXAMPLE 1
class Sushi(ABC):
    def make_sushi(self):
        self.cook_rice()
        self.add_filling()
        self.wrap()
        self.cook()
        self.serve()

    def cook_rice(self):
        print('Rice is boiled.')

    def serve(self):
        print('Served with wasabi and marinated ginger root.')

    def wrap(self):
        pass

    def cook(self):
        pass

    @abstractmethod
    def add_filling(self):
        pass


class UnagiMaki(Sushi):
    def add_filling(self):
        print('Smoked eel added.')

    def wrap(self):
        print('Wrapped in nori.')


class BakedShrimpRoll(Sushi):
    def add_filling(self):
        print('Cleaned shrimp added.')

    def wrap(self):
        print('Tempura sprinkled.')

    def cook(self):
        print('Baked in oven.')


def test():
    unagi_maki = UnagiMaki()
    unagi_maki.make_sushi()
    print("#############")

    baked_shrimp_roll = BakedShrimpRoll()
    baked_shrimp_roll.make_sushi()

    print('Done!')


# EXAMPLE 2

class ProcessFile(ABC):
    def process(self, file: str):
        self.open_file(file)
        self.scrape_url()
        self.process_file()
        self.close_file()

    @abstractmethod
    def open_file(self, file: str):
        pass

    @abstractmethod
    def process_file(self):
        pass

    @abstractmethod
    def close_file(self):
        pass

    def scrape_url(self):
        ...


class PdfFile(ProcessFile):
    def open_file(self, file: str):
        print(f'Opening PDF file: {file}')

    def process_file(self):
        print('Processing PDF file...')

    def close_file(self):
        print('Closing PDF file...')


class TxtFile(ProcessFile):
    def open_file(self, file: str):
        print(f'Opening TXT file: {file}')

    def process_file(self):
        print('Processing TXT file...')

    def close_file(self):
        print('Closing TXT file...')


class UrlFile(ProcessFile):
    def scrape_url(self):
        print('Scraping URL...')

    def open_file(self, file: str):
        print(f'Opening URL file: {file}')

    def process_file(self):
        print('Processing URL file...')

    def close_file(self):
        print('Closing URL file...')


def test2():
    pdf_file = PdfFile()
    pdf_file.process('file.pdf')

    print("#############")

    txt_file = TxtFile()
    txt_file.process('file.txt')

    print("#############")

    url_file = UrlFile()
    url_file.process('url')
