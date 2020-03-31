import textfsm
import sys
import re
import os.path
from os import path
from collections import defaultdict

d = defaultdict(list)

# Load the input file to a variable
input_file = open(sys.argv[1], encoding='utf-8')
raw_text_data = input_file.read()
input_file.close()

# Run the text through the FSM. 
# The argument 'template' is a file handle and 'raw_text_data' is a 
# string with the content from the show_inventory.txt file
template = open("intf_couters.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)

for item in fsm_results:
   print(*item)

len_of_four_blocks = int(len(fsm_results) / 4)
 
first_sample = fsm_results[0:len_of_four_blocks] 
second_sample = fsm_results[-len_of_four_blocks*2:-len_of_four_blocks:]
 
def input_traffic_lst_packets(sample):
   inputs = []
   for item in sample:
      # print(*item)
      if item[1] == 'Input :':
         inputs.append((item[0], int(item[3])))
   return inputs
   
def output_traffic_lst_packets(sample):
   outputs = []
   for item in sample:
      # print(*item)
      if item[2] == 'Output:':
         outputs.append((item[0], int(item[3])))
   return outputs

def input_traffic_lst_bytes(sample):
   inputs = []
   for item in sample:
      # print(*item)
      if item[1] == 'Input :':
         inputs.append((item[0], int(item[5])))
   return inputs
   
def output_traffic_lst_bytes(sample):
   outputs = []
   for item in sample:
      # print(*item)
      if item[2] == 'Output:':
         outputs.append((item[0], int(item[5])))
   return outputs


def calc_in_sample(inputs):
   total_input = 0
   for interface, input in inputs:
      total_input += input
   return total_input

def calc_out_sample(outputs):
   total_output = 0
   for interface, output in outputs:
      total_output += output
   return total_output

input_values_fs_packets = input_traffic_lst_packets(first_sample)
input_values_ss_packets = input_traffic_lst_packets(second_sample)

output_values_fs_packets = output_traffic_lst_packets(first_sample)
output_values_ss_packets = output_traffic_lst_packets(second_sample)

input_values_fs_bytes = input_traffic_lst_bytes(first_sample)
input_values_ss_bytes = input_traffic_lst_bytes(second_sample)

output_values_fs_bytes = output_traffic_lst_bytes(first_sample)
output_values_ss_bytes = output_traffic_lst_bytes(second_sample)

"""
print("input traffic list first sample  ", input_values_fs)
print("output traffic list first sample ", output_values_fs)
print("input traffic list second sample ", input_values_ss)
print("output traffic list second sample", output_values_ss)
"""

total_input_fs_packets = calc_in_sample(input_values_fs_packets)
# print(total_input_fs)

total_output_fs_packets = calc_in_sample(output_values_fs_packets)
# print(total_output_fs)

total_input_ss_packets = calc_in_sample(input_values_ss_packets)
# print(total_input_ss)

total_output_ss_packets = calc_in_sample(output_values_ss_packets)
# print(total_output_ss)

#####

total_input_fs_bytes = calc_in_sample(input_values_fs_bytes)
# print(total_input_fs)

total_output_fs_bytes = calc_in_sample(output_values_fs_bytes)
# print(total_output_fs)

total_input_ss_bytes = calc_in_sample(input_values_ss_bytes)
# print(total_input_ss)

total_output_ss_bytes = calc_in_sample(output_values_ss_bytes)

print("Input traffic in 1 hour (packets) ", total_input_ss_packets - total_input_fs_packets)
print("Output traffic in 1 hour (packets)", total_output_ss_packets - total_output_fs_packets)

print("Input traffic in 1 hour (bytes) ", total_input_ss_bytes - total_input_fs_bytes)
print("Output traffic in 1 hour (bytes)", total_output_ss_bytes - total_output_fs_bytes)