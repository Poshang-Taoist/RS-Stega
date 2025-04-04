import bitarray

def calculate_line_length_and_bit_length(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    line_lengths = []  # 存储每一行的字符长度
    bit_lengths = []   # 存储每一行转换为 01 字符串的比特长度

    for line in lines:
        line = line.strip()  # 去掉行末的换行符和多余空格
        # 计算字符的平均长度
        line_lengths.append(len(line))

        # 将每一行通过UTF-8编码转换为比特串
        ba = bitarray.bitarray()
        ba.frombytes(line.encode('utf-8'))
        # 计算该行的比特长度（1比特对应一个 0 或 1）
        bit_lengths.append(len(ba))

    # 计算平均值
    avg_line_length = sum(line_lengths) / len(line_lengths) if line_lengths else 0
    avg_bit_length = sum(bit_lengths) / len(bit_lengths) if bit_lengths else 0

    # 打印每行的字符长度和比特长度
    print(f"Average character length: {avg_line_length}")
    print(f"Average bit length (UTF-8 encoding): {avg_bit_length}")
    
    return avg_line_length, avg_bit_length

# 使用该函数读取文件并计算平均值
file_path = r"D:\UIR\framework\code\datasets\covide.txt"  # 替换为你文件的路径
calculate_line_length_and_bit_length(file_path)
