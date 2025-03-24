# #这段代码的主要功能是通过串口实时接收EEG数据，
# #将接收到的多通道EEG信号数据处理后保存到**BDF文件（Biosemi Data Format）**中，供后续分析使用
#
# import numpy as np
# import pyedflib
# import time
# import serial
# import serial.tools.list_ports
# # from pyedflib import highlevel
# import os
# # 帧头、帧尾和帧大小定义
# FRAME_HEADER = bytearray([0x55, 0xAA])  # 帧头
# FRAME_TAIL = 0xAA  # 帧尾
# FRAME_SIZE = 36  # 帧大小
# ref = 2.5  # 参考电压
# base = 2 ** 24  # 基准
# gain = 4  # 放大倍数
#
# # EEG命令
# EEG_Command_Handshake = [0xAA, 0x55, 0x01, 0x06, 0x00, 0x00, 0x55]
# EEG_Command_Start_Connection = [0xAA, 0x55, 0x01, 0x06, 0x00, 0x01, 0x55]
# EEG_Command_Stop_Connection = [0xAA, 0x55, 0x01, 0x06, 0x00, 0x04, 0x55]
#
# print("当前工作目录为:", os.getcwd())
#
# def convert_to_decimal(data, index):
#     """将数据转换为十进制整数"""
#     value = (data[index] << 16) | (data[index + 1] << 8) | data[index + 2]
#     if value >= 2 ** 23:
#         value -= 2 ** 24
#     return value
#
# def create_bdf(file, channel):
#     """创建BDF文件并设置通道信息"""
#     f = pyedflib.EdfWriter(file, channel, file_type=pyedflib.FILETYPE_BDFPLUS)
#     channel_info = []
#     channel_list = ['C3', 'C4', 'Cz', 'FC3', 'FC4', 'CP3', 'CP4', 'CPz']  #Cz->
#
#     for ch in channel_list:
#         ch_dict = {
#             'label': ch,
#             'dimension': 'uV',
#             'sample_rate': 500,
#             'physical_max': 2000,
#             'physical_min': -2000,
#             'digital_max': 8388607,
#             'digital_min': -8388607,
#             'transducer': '',
#             'prefilter': ''
#         }
#         channel_info.append(ch_dict)
#
#     f.setSignalHeaders(channel_info)
#     return f
#
# def Serial_Init(bdf_file, total_samples):
#     """初始化串口并接收数据"""
#     ports_list = list(serial.tools.list_ports.comports())
#     if not ports_list:
#         print("没有可用的串口")
#         return
#
#     print("可用的串口如下:")
#     for comports in ports_list:
#         print(f"{comports.device} - {comports.description}")
#
#     while True:
#         MyPort = input("请输入你的串口号（例如：1表示COM1）：")
#         if any(port.device == f"COM{MyPort}" for port in ports_list):
#             break
#         else:
#             print("串口不存在，请重新输入！")
#
#     ser = serial.Serial(f"COM{MyPort}", 921600, timeout=0)   #921600
#     print(f"{ser.portstr} 已打开")
#
#     f = create_bdf(bdf_file, 8)
#     receivedData = bytearray()
#
#     try:
#         ser.write(EEG_Command_Stop_Connection)
#         time.sleep(1)
#         ser.write(EEG_Command_Handshake)
#         time.sleep(1)
#         ser.write(EEG_Command_Start_Connection)
#
#         data_arr = np.zeros((8, total_samples))
#         sample_index = 0
#         start_time = time.time()
#
#         while sample_index < total_samples:
#             # 尝试每次读取64个字节
#             data = ser.read(64)  #64
#             if data:
#                 receivedData.extend(data)
#                 print(f"当前接收数据: {receivedData}")
#              #   print(f"当前接收数据长度: {len(receivedData)}")  #----------by 1
#                 while True:
#                     headerIt = receivedData.find(FRAME_HEADER)
#                     if headerIt == -1:
#                         print('没有找到帧头，当前接收数据:', receivedData)
#                         break
#
#                     # 检查数据长度是否足够
#                     if len(receivedData) < FRAME_SIZE:
#                         print("数据长度不足，当前接收数据长度:", len(receivedData))
#                         break
#                     # # 当接收到的数据长度不满36字节时，继续接收   -----by 1
#                     # while len(receivedData) < FRAME_SIZE:
#                     #     data = ser.read(FRAME_SIZE - len(receivedData))  # 读取缺少的字节
#                     #     receivedData.extend(data)
#                     #
#
#                     if headerIt + FRAME_SIZE <= len(receivedData):
#                         expected_tail = receivedData[headerIt + FRAME_SIZE - 1]
#                         if expected_tail == FRAME_TAIL:
#                             command_type = receivedData[headerIt + 3]
#                             if command_type == 0x01:
#                                 if headerIt + len(FRAME_HEADER) + 5 + 8 * 3 <= len(receivedData):
#                                     channels = [
#                                         convert_to_decimal(receivedData, headerIt + len(FRAME_HEADER) + 5 + j * 3)
#                                         for j in range(8)
#                                     ]
#                                     output_values = [(ch * ref * 2 / base / gain * 1000) for ch in channels]
#
#
#                                     if sample_index < total_samples:
#                                         data_arr[:, sample_index] = output_values
#                                         sample_index += 1
#
#                                         progress = (sample_index / total_samples) * 100
#                                         print(f"进度: {progress:.2f}% ({sample_index}/{total_samples})")
#
#                                     elapsed_time = time.time() - start_time
#                                     if elapsed_time >= 10:
#                                         f.writeSamples(data_arr[:, :sample_index])
#                                         data_arr = np.zeros((8, total_samples))
#                                         sample_index = 0
#                                         start_time = time.time()
#                                         print("已写入数据，重置数据数组。")
#
#                             elif command_type == 0x06:
#                                 if headerIt + len(FRAME_HEADER) + 5 + 8 * 3 <= len(receivedData):
#                                     impedance_values = [
#                                         convert_to_decimal(receivedData, headerIt + len(FRAME_HEADER) + 5 + j * 3)
#                                         for j in range(8)
#                                     ]
#                                     print(f"阻抗数据: {impedance_values}")
#
#                             # 删除已处理的数据
#                             del receivedData[:headerIt + FRAME_SIZE]
#                         else:
#                             print("帧尾不匹配，丢弃无效数据")
#                             del receivedData[:headerIt]
#                     else:
#                         break
#
#     except Exception as e:
#         print(f"发生错误: {e}")
#     finally:
#         try:
#             ser.write(EEG_Command_Stop_Connection)
#         except Exception as e:
#             print(f"停止连接时发生错误: {e}")
#         finally:
#             ser.close()
#             f.writeSamples(data_arr[:, :sample_index])
#             f.close()
#             print("串口已关闭，BDF文件已保存。")
#
#
#
# if __name__ == "__main__":
#     duration = int(input("请输入采集时长（秒）："))
#     total_samples = 500 * duration
#     demoFilePath = 'test11.bdf'
#     Serial_Init(demoFilePath, total_samples)
#
#
#
#


import numpy as np
import time
import serial
import serial.tools.list_ports
import os
import pyedflib  # 用于创建BDF文件

# 定义协议中的帧头、帧尾和帧大小
FRAME_HEADER = bytearray([0x55, 0xAA])  # 帧头
FRAME_TAIL = 0xAA  # 帧尾
FRAME_SIZE = 36  # 帧大小
ref = 2.5  # 参考电压
base = 2 ** 24  # 基准
gain = 4  # 放大倍数

# EEG命令
EEG_Command_Handshake = [0xAA, 0x55, 0x01, 0x06, 0x00, 0x00, 0x55]  # 握手命令
EEG_Command_Start_Connection = [0xAA, 0x55, 0x01, 0x06, 0x00, 0x01, 0x55]  # 开始采集命令
EEG_Command_Stop_Connection = [0xAA, 0x55, 0x01, 0x06, 0x00, 0x04, 0x55]  # 停止采集命令

# 输出目录
OUTPUT_DIR = os.getcwd()


def convert_to_decimal(data, index):
    """将数据转换为十进制整数"""
    value = (data[index] << 16) | (data[index + 1] << 8) | data[index + 2]
    if value >= 2 ** 23:
        value -= 2 ** 24
    return value


def create_bdf(file, channel_list, sample_rate):
    """创建BDF文件并设置通道信息"""
    f = pyedflib.EdfWriter(file, len(channel_list), file_type=pyedflib.FILETYPE_BDFPLUS)

    # 定义通道信息
    channel_info = []
    for ch in channel_list:
        ch_dict = {
            'label': ch,
            'dimension': 'uV',
            'sample_rate': sample_rate,
            'physical_max': 2000,
            'physical_min': -2000,
            'digital_max': 8388607,
            'digital_min': -8388607,
            'transducer': '',
            'prefilter': ''
        }
        channel_info.append(ch_dict)

    f.setSignalHeaders(channel_info)
    return f


def Serial_Init(total_samples, output_file):
    """初始化串口并接收数据"""
    ports_list = list(serial.tools.list_ports.comports())
    if not ports_list:
        print("没有可用的串口")
        return

    print("可用的串口如下:")
    for comports in ports_list:
        print(f"{comports.device} - {comports.description}")

    while True:
        MyPort = input("请输入你的串口号（例如：1表示COM1）：")
        if any(port.device == f"COM{MyPort}" for port in ports_list):
            break
        else:
            print("串口不存在，请重新输入！")

    ser = serial.Serial(f"COM{MyPort}", 921600, timeout=0)  # 串口波特率为921600
    print(f"{ser.portstr} 已打开")

    # 定义EEG通道名称（根据你的数据选择合适的通道）
    channel_list = ['C3', 'C4', 'Cz', 'FC3', 'FC4', 'CP3', 'CP4', 'CPz']
    sample_rate = 500  # 假设采样率为500Hz

    # 创建BDF文件并获取文件对象
    f = create_bdf(output_file, channel_list, sample_rate)

    receivedData = bytearray()
    raw_data = np.zeros((len(channel_list), total_samples))

    try:
        # 发送停止连接命令
        ser.write(EEG_Command_Stop_Connection)
        time.sleep(1)
        # 发送握手命令
        ser.write(EEG_Command_Handshake)
        time.sleep(1)
        # 发送开始连接命令
        ser.write(EEG_Command_Start_Connection)

        sample_index = 0
        start_time = time.time()

        while sample_index < total_samples:
            # 尝试每次读取64个字节
            data = ser.read(64)  # 每次读取64字节
            if data:
                receivedData.extend(data)
                print(f"当前接收数据: {receivedData}")

                while True:
                    headerIt = receivedData.find(FRAME_HEADER)
                    if headerIt == -1:
                        print('没有找到帧头，当前接收数据:', receivedData)
                        break

                    # 检查数据长度是否足够
                    if len(receivedData) < FRAME_SIZE:
                        print("数据长度不足，当前接收数据长度:", len(receivedData))
                        break

                    if headerIt + FRAME_SIZE <= len(receivedData):
                        expected_tail = receivedData[headerIt + FRAME_SIZE - 1]
                        if expected_tail == FRAME_TAIL:
                            command_type = receivedData[headerIt + 3]
                            if command_type == 0x01:
                                if headerIt + len(FRAME_HEADER) + 5 + 8 * 3 <= len(receivedData):
                                    channels = [
                                        convert_to_decimal(receivedData, headerIt + len(FRAME_HEADER) + 5 + j * 3)
                                        for j in range(8)
                                    ]
                                    output_values = [(ch * ref * 2 / base / gain * 1000) for ch in channels]

                                    if sample_index < total_samples:
                                        raw_data[:, sample_index] = output_values
                                        sample_index += 1

                                        progress = (sample_index / total_samples) * 100
                                        print(f"进度: {progress:.2f}% ({sample_index}/{total_samples})")

                                    elapsed_time = time.time() - start_time
                                    if elapsed_time >= 10:
                                        # 每10秒保存一次数据
                                        print("保存数据片段...")
                                        f.writeSamples(raw_data[:, :sample_index])
                                        print(f"数据已保存至BDF文件")

                                        # 重置数据数组
                                        raw_data = np.zeros((len(channel_list), total_samples))
                                        sample_index = 0
                                        start_time = time.time()

                            # 删除已处理的数据
                            del receivedData[:headerIt + FRAME_SIZE]
                        else:
                            print("帧尾不匹配，丢弃无效数据")
                            del receivedData[:headerIt]
                    else:
                        break

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        try:
            ser.write(EEG_Command_Stop_Connection)
        except Exception as e:
            print(f"停止连接时发生错误: {e}")
        finally:
            ser.close()
            f.close()
            print("串口已关闭，数据保存完毕。")


if __name__ == "__main__":
    duration = int(input("请输入采集时长（秒）："))
    total_samples = 500 * duration  # 500Hz采样率下的样本数
    output_file = "EEG_data.bdf"  # 输出的BDF文件名
    Serial_Init(total_samples, output_file)

