from pathlib import Path

def self_path():
    path = Path(__file__)
    return path

def concat_path():
    resource_path = Path('resources').absolute()
    book_path = resource_path / 'books/1强化学习入门指南.txt'
    return book_path



if __name__ == '__main__':
    print(concat_path())