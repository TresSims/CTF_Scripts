def convert_to_lowercase(input_file, output_file):
    try:
        # read all contents of input_file to data variable
        with open(input_file, 'r') as f_input:
            data = f_input.read()

        # convert all characters in data to lowercase
        data_lower = data.lower()

       # write all lowercase data to output file
        with open(output_file, 'w') as f_output:
            f_output.write(data_lower)

        print(f"Conversion successful. Lowercase content saved to {output_file}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# If we're running the script from the command line prompt for in and out files
if __name__ == "__main__":
    input_file_path = input("Enter the input file path: ")
    output_file_path = input("Enter the output file path: ")

    convert_to_lowercase(input_file_path, output_file_path)