A = [251 219 167;216 102 116;102 155 180]
B = [135 ;129; 156]



A2 = [255 240 193; 241 195 191 ; 171, 219, 221]
B2 = [193; 193; 217]

alpha = A.'\B
alpha2 = A2.'\B2

%taking same colors from color picker
A_c_picker = [196 184 148;123 56 72;44 79 105]
B_c_picker = [73 ;68; 95]



A2_c_picker = [210 213 186; 158 141 147 ; 108, 147, 158]
B2_c_picker = [131; 136; 163]

alpha = A.'\B

alpha_c_picker = A_c_picker.'\B_c_picker
alpha2 = A2.'\B2
alpha2_c_picker = A2_c_picker.'\B2_c_picker

