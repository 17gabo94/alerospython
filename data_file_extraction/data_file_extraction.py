def execute():
    try:
        # Leer el archivo de entrada
        with open("./data_file_extraction/data.txt", "r") as file:
            numbers = file.readlines()

        # Convertir a enteros y filtrar los mayores que 50
        filtered = [int(num.strip()) for num in numbers if int(num.strip()) > 50]

        # Escribir los resultados en results.txt
        with open("./data_file_extraction/results.txt", "w") as result_file:
            for num in filtered:
                result_file.write(f"{num}\n")

        print("File processed successfully! Numbers > 50 were written to results.txt")

    except FileNotFoundError:
        print("Error: data.txt file not found.")
    except ValueError:
        print("Warning: The file contains non-numeric values.")