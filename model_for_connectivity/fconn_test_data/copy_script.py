import os
import shutil

source_dir = "/space_lin1/quanta/sub-xxxx/eeg_analysis"
dest_dir = "/space_lin2/nikhil/fconn_copy"

# Iterate over subject IDs from 0001 to 0152
for subject_id in range(1, 153):
    subject_id_str = str(subject_id).zfill(4)  # Zero-padding the subject ID
    
    if subject_id_str == "0003" or subject_id_str == "0096" or subject_id_str == "0119":
        continue  # Skip subject ID 0003
        
    source_file = os.path.join(source_dir.replace("xxxx", subject_id_str), "resting_eeg_fconn.mat")
    dest_file = os.path.join(dest_dir, "resting_eeg_fconn_" + subject_id_str + ".mat")

    # Copy the file
    shutil.copy(source_file, dest_file)
