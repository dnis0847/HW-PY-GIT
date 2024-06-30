""" Домашнее задание от 8.06.2024. Задача: Анализ текстовых данных с использованием функционального подхода

Вам необходимо разработать программу для анализа текстовых данных из нескольких файлов. Каждый файл содержит
текстовую информацию о продажах определенного товара в разные периоды времени. Вам нужно выполнить следующие шаги
с помощью функционального подхода:"""

from my_modules.read_file import read_file
from my_modules.process_data import process_data
from my_modules.filter_data import filter_data
from my_modules.aggregate_data import aggregate_data
from my_modules.visualize_data import visualize_data


def main():
    file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
    for file_path in file_paths:
        try:
            data = read_file(file_path)
            processed_data = process_data(data)
            filtered_data = filter_data(processed_data, 2000)
            aggregated_data = aggregate_data(filtered_data)
            visualize_data(aggregated_data)
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")


if __name__ == '__main__':
    main()
